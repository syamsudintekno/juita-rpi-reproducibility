"""Synthetic substantive checks; no institutional data is required."""
from copy import deepcopy
import hashlib
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch

import numpy as np
from scipy import stats
from src import rpi_pipeline as pipeline

ROOT = Path(__file__).resolve().parents[1]
COHORT = tomllib.loads((ROOT/'configs/cohort.toml').read_text(encoding='utf-8'))
ANALYSIS = tomllib.loads((ROOT/'configs/analysis.toml').read_text(encoding='utf-8'))


def record(name, program, values):
    return {'name': name, 'program': program, 'items': values,
            'source': {'file': 'synthetic', 'sheet': 'synthetic', 'row': 3}}


class PipelineTests(unittest.TestCase):
    def test_invalid_whole_record_and_valid_low_score(self):
        bad = [4]*20; bad[3] = 'broken'
        kept, excluded = pipeline.prepare([
            record('Synthetic A', 'Program 1', bad),
            record('Synthetic A', 'Program 2', [1]*20),
        ], COHORT)
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]['total'], 20)
        self.assertEqual(excluded[0]['invalid_items'][0]['item'], 4)
        for value in [None, '', True, float('nan'), float('inf'), 0, 5.001, '4,5']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                pipeline.parse_item(value)

    def test_labels_do_not_exclude_named_supervisors_or_near_word(self):
        self.assertEqual(pipeline.exclusion_reason(' tim  Synthetic ', COHORT), 'team_label')
        self.assertEqual(pipeline.exclusion_reason('Pembimbing Skripsi', COHORT), 'generic_supervisor_label')
        self.assertEqual(pipeline.exclusion_reason('DOSEN DPL', COHORT), 'other_generic_label')
        self.assertIsNone(pipeline.exclusion_reason('Timothy Synthetic', COHORT))
        self.assertIsNone(pipeline.exclusion_reason('Synthetic Lecturer Pembimbing', COHORT))

    def test_equal_record_aggregation_and_no_name_merging(self):
        means, names = pipeline.aggregate([
            record('Synthetic A', 'Program 1', [1]*20),
            record('Synthetic A', 'Program 2', [5]*20),
            record('Synthetic B', 'Program 1', [4]*20),
            record('Synthetic A ', 'Program 3', [2]*20),
        ])
        self.assertEqual(len(names), 3)
        a = next(i for i,x in enumerate(names) if x['original_name']=='Synthetic A')
        np.testing.assert_array_equal(means[a], [3]*20)
        self.assertEqual(names[a]['n_records'], 2)

    def test_duplicate_name_program_requires_review(self):
        with self.assertRaises(ValueError):
            pipeline.prepare([record('Synthetic A','Program 1',[4]*20)]*2, COHORT)

    def test_item_mapping_and_matched_weights(self):
        x = np.ones((3,20)); x[0,:6]=5; x[1,:]=3; x[2,:]=4
        result = pipeline.score(x, ANALYSIS)
        np.testing.assert_allclose(result['dimensions'][0], [5,1,1,1])
        self.assertEqual(result['item_sum'][0], 44)
        self.assertEqual(result['matched_raw'][0], 40)
        np.testing.assert_allclose(result['RPI'], 50+10*result['C'])
        for weights in [[1,0,0], [0.5,0.5,0.5,-0.5], [np.nan,0,0,1], [np.inf,0,0,0], [0.2]*4]:
            with self.subTest(weights=weights), self.assertRaises(ValueError):
                pipeline.validate_weights(weights)

    def test_blom_average_ties_descending_min_and_percentiles(self):
        x = np.repeat(np.array([2,2,4,5])[:,None],20,axis=1)
        result = pipeline.score(x, ANALYSIS)
        np.testing.assert_allclose(result['dimension_ranks'][:,0], [1.5,1.5,3,4])
        expected_p=(np.array([1.5,1.5,3,4])-0.375)/4.25
        np.testing.assert_allclose(result['p'][:,0],expected_p)
        np.testing.assert_allclose(result['z'][:,0],stats.norm.ppf(expected_p))
        np.testing.assert_array_equal(result['rank_matched_raw'],[3,3,2,1])
        np.testing.assert_allclose(result['percentile_matched_raw'],[25,25,62.5,87.5])
        self.assertEqual(result['RPI'][0],result['RPI'][1])
        self.assertTrue(((result['p']>0)&(result['p']<1)).all())

    def test_quadrant_equality_is_high_and_constant_metrics_unavailable(self):
        result = pipeline.score(np.full((4,20),3.0), ANALYSIS)
        self.assertEqual(result['quadrants'],['Q1']*4)
        np.testing.assert_allclose(result['RPI'],50)
        self.assertIsNone(pipeline.describe(result['RPI'])['shapiro_p'])
        self.assertIsNone(pipeline.agreement(result['matched_raw'],result['RPI'],result['matched_rank_shift'])['Spearman_rho'])

    def test_composite_sd_depends_on_covariance(self):
        levels=np.array([1,2,3,4])
        aligned=np.repeat(levels[:,None],20,axis=1)
        reversed_pair=aligned.copy(); reversed_pair[:,6:11]=levels[::-1,None]; reversed_pair[:,16:20]=levels[::-1,None]
        a=pipeline.score(aligned,ANALYSIS); b=pipeline.score(reversed_pair,ANALYSIS)
        for result in [a,b]:
            cov=np.cov(result['z'],rowvar=False,ddof=1)
            predicted=10*np.sqrt(max(0,float(result['weights']@cov@result['weights'])))
            self.assertAlmostEqual(np.std(result['RPI'],ddof=1),predicted,places=10)
        self.assertGreater(np.std(a['RPI'],ddof=1),1)
        self.assertLess(np.std(b['RPI'],ddof=1),1e-10)
        self.assertNotAlmostEqual(np.std(a['RPI'],ddof=1),10,places=4)

    def test_alpha_is_computed_at_requested_aggregate_level(self):
        items=np.repeat(np.array([1,2,3])[:,None],20,axis=1)
        self.assertAlmostEqual(pipeline.cronbach_alpha(items),1)
        self.assertIsNone(pipeline.cronbach_alpha(np.ones((3,20))))

    def test_source_parser_stops_at_second_dimension_header(self):
        headers=['No.','Nama Dosen','Program Studi']+[f'Pertanyaan {i}' for i in range(1,21)]
        class Sheet:
            title='Synthetic'
            def iter_rows(self,values_only=True):
                return iter([headers,[1,'Synthetic A','Program 1']+[4]*20,
                             ['No.','Nama Dosen','Program Studi','Pedagogik'],
                             [1,'Synthetic A','Program 1',4]])
        class Workbook:
            def __iter__(self): return iter([Sheet()])
            def close(self): pass
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'fixture.xlsx'; path.write_bytes(b'synthetic mocked payload')
            manifest=[{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}]
            with patch.object(pipeline,'load_workbook',return_value=Workbook()):
                rows,sources=pipeline.read_sources(manifest)
            self.assertEqual(len(rows),1)
            self.assertEqual(sources[0]['records'],1)
            manifest[0]['sha256']='wrong'
            with self.assertRaises(ValueError): pipeline.read_sources(manifest)

    def test_institutional_outputs_cannot_leave_private_directory(self):
        with self.assertRaisesRegex(ValueError,'workspace/private'):
            pipeline.run('nonexistent','nonexistent','nonexistent',ROOT/'public_results')


if __name__=='__main__':
    unittest.main()
