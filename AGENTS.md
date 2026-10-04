# AGENTS.md — JUITA RPI Reproducibility

## Tujuan repo

Repo ini mendukung revisi dan reproduksibilitas paper JUITA:
“Restoring Distributional Properties of Ceiling-Compressed Student
Evaluation of Teaching Data via Relative Performance Index”.

Keputusan editor: RESUBMIT FOR REVIEW.

Keputusan penulis:
- EDOM institusional tetap menjadi dataset utama.
- Tidak mengganti studi utama dengan dataset Sukirno atau UCI.
- Dataset eksternal hanya digunakan jika mendukung pertanyaan ilmiah
  yang jelas dan memiliki struktur data yang sesuai.
- Repo ini menangani preprocessing, analisis statistik, simulasi,
  contoh perhitungan, tabel, gambar, naskah, dan revision matrix.
- ILAD merupakan repo aplikasi dashboard yang terpisah:
  https://github.com/syamsudintekno/ILAD
- Jangan mengubah ILAD otomatis ketika bekerja di repo ini.

Komunikasi kepada Sam menggunakan bahasa Indonesia.
Naskah, gambar, tabel publikasi, dan tanggapan reviewer menggunakan
bahasa Inggris.

Bersikap kritis dan berbasis bukti. Jangan mengarang data, referensi,
hasil pengujian, persetujuan etik, maupun informasi institusional.

## Status awal: wajib diverifikasi ulang

Audit percakapan pada 4 Oktober 2026 menemukan:
- 1.105 rekaman agregat, 370 string nama unik, dan 33 prodi.
- Tersedia 20 skor butir agregat.
- Respons individual mahasiswa tidak tersedia.
- Jumlah responden dan kolom periode evaluasi tidak tersedia.
- Satu nilai P4 tidak numerik.
- Total rekaman rusak tersebut hanya menjumlahkan 19 butir numerik.
- Label generik “DOSEN DPL” muncul pada tiga rekaman.
- Skenario eksklusi tiga rekaman generik dan satu rekaman rusak
  menghasilkan 1.101 rekaman dan 369 kelompok nama.
- Identitas dosen belum diverifikasi terhadap roster institusi.
- Banyak NIP kosong atau berformat notasi ilmiah.
- Shapiro–Wilk belum dihitung ulang untuk cohort yang dikoreksi.

Audit dan simulasi awal dihitung melalui JavaScript dalam percakapan.
Jangan menyebutnya hasil eksekusi Python, Colab, atau pipeline repo.

Angka tersebut adalah temuan sementara, bukan hasil final yang harus
dipaksakan. Baca sumber aktual, catat versi/hash, dan hitung ulang.
Jangan hardcode N=369 sebagai hasil wajib.

## Perlindungan sumber dan data

- Sumber asli read-only; jangan menimpa atau mengoreksi langsung.
- Jangan commit data EDOM asli, nama, NIP, identitas mahasiswa,
  atau tabel penghubung kode–nama.
- Repo berstatus publik pada pemeriksaan awal. Jangan menganggap
  repositori privat ketika menyiapkan file atau commit.
- Buat .gitignore sebelum memasukkan data lokal sensitif.
- Periksa output notebook, metadata, gambar, log, dan commit diff.
- Simpan pemetaan identitas secara lokal dan terpisah.
- Contoh publik default menggunakan data sintetis berlabel jelas.
- Anonimisasi tidak otomatis memberikan izin publikasi data institusi.
- Jangan memasukkan URL unduhan privat, token, atau kredensial.
- Jangan mengirim data pribadi sebagai query pencarian eksternal.

## Kontrak data dan preprocessing

Urutan kerja:
1. Baca snapshot sumber tanpa mengubahnya.
2. Validasi header, encoding, tipe data, nilai hilang, rentang skor,
   dan duplikasi pasangan nama–prodi.
3. Cocokkan identitas dengan roster institusi bila tersedia.
4. Identifikasi label non-individual berdasarkan aturan eksplisit.
5. Telusuri nilai rusak ke sumber resmi.
6. Koreksi hanya jika tersedia nilai terverifikasi dan provenance.
7. Jika tidak dapat dipulihkan, gunakan complete-case exclusion
   pada seluruh rekaman sebagai skenario terdokumentasi.
8. Hitung ulang total dari 20 butir valid.
9. Agregasikan butir per dosen dari rekaman lengkap.
10. Bentuk dimensi, kemudian jalankan analisis dan Rankit.

Aturan:
- Jangan menganggap nilai hilang sebagai nol.
- Jangan menebak P4 menggunakan rerata, median, atau total yang cacat.
- Pertahankan skor rendah yang valid.
- Jangan membuang outlier hanya untuk mendapatkan normalitas.
- Jangan menggabungkan orang berdasarkan kemiripan nama saja.
- NIP yang rusak bukan kunci identitas terverifikasi.
- Rekaman prodi bukan respons mahasiswa individual.
- Jangan menyebut rekaman sebagai kelas tanpa dokumentasi sumber.
- Tanpa jumlah responden, gunakan bobot sama antarrekaman prodi;
  jelaskan bahwa ini bukan rerata berbobot jumlah mahasiswa.
- Gunakan rekaman yang konsisten untuk seluruh dimensi.
- Dokumentasikan eksklusi, koreksi, dan dampaknya terhadap cohort.
- Jangan menebak periode data dari tanggal file atau tahun naskah.

Keluaran preprocessing:
- Dataset kerja bersih yang disimpan lokal.
- Kamus variabel.
- Log perubahan dan eksklusi.
- Rekonsiliasi jumlah rekaman dan identitas.
- Manifest sumber, config, dan versi kode.

## Pemetaan dimensi

Pemetaan institusi yang harus diverifikasi terhadap instrumen:
- Pedagogical: P1–P6.
- Professional: P7–P11.
- Personality: P12–P16.
- Social: P17–P20.

Skor dimensi dihitung dari rerata butir pada agregat dosen.

## Formulasi kerja RPI

Untuk dosen i dan dimensi k:
- d_ik: skor dimensi.
- r_ik: ascending midrank dalam dimensi.
- N: jumlah entitas pada cohort analisis.
- p_ik = (r_ik - 0.375) / (N + 0.25).
- z_ik = Phi_inverse(p_ik).
- C_i = sum_k(w_k * z_ik).
- RPI_i = 50 + 10 * C_i.
- Bobot kerja: w_k = 0.25.

Validasi bobot: finite, nonnegative, dan jumlahnya 1.

Formulasi kerja mengikuti konvensi Blom yang diperiksa, bukan otomatis
(r - 0.5)/N. Verifikasi rujukan primer sebelum menulis atribusi.
N + 0.25 berasal dari N + 1 - 2*0.375.

Konstanta 50 dan 10 menentukan lokasi dan skala tampilan.
SD komposit RPI tidak otomatis 10.

Jangan menstandardisasi C secara diam-diam. Perubahan formulasi harus
dicatat dan seluruh hasil terkait dihitung ulang.

Rankit dijalankan setelah preprocessing, agregasi, dan pembentukan
dimensi. Rankit bukan tahap pembersihan distribusi mentah.

## Pembanding yang adil

Gunakan tiga skor:
1. Jumlah rerata 20 butir: bobot dimensi efektif
   0.30, 0.25, 0.25, 0.20.
2. Mentah berbobot dimensi sama:
   X_i = 20 * sum_k(0.25 * d_ik).
3. RPI berbobot dimensi sama.

Perbandingan utama pengaruh transformasi: (2) versus (3).
Perbandingan (1) versus (3) mencampurkan transformasi dan bobot.

Untuk butir 1–5, skor mentah tersebut memiliki rentang teoritis
20–100. Jangan menyebutnya 0–100 tanpa formula rescaling.

Tetapkan sebelum analisis:
- Spearman: midranks.
- Kendall: tau-b.
- Perpindahan posisi: descending minimum rank untuk ties.
- Kuadran: median; nilai sama dengan median masuk kelompok high.
- Presisi dan toleransi numerik: eksplisit dan teruji.
- Jangan membulatkan untuk memaksakan kesepakatan hasil.

## Batas interpretasi ilmiah

- Bedakan upper-range concentration, ceiling effect teramati,
  dan mekanisme kehilangan informasi laten.
- Ambang >=85 dan ketidaknormalan tidak membuktikan ceiling effect.
- Periksa maksimum teoritis, ties, variasi, dan distribusi pada
  tingkat butir, dimensi, dan komposit.
- Jangan memindahkan kriteria klinis tanpa justifikasi.
- Normalisasi marginal merupakan konsekuensi Rankit.
- Normalitas komposit tetap perlu diperiksa.
- Rankit tidak memulihkan informasi yang hilang atau membedakan ties.
- Transformasi distribusi bukan bukti peningkatan validitas,
  ketepatan penilaian dosen, atau fairness.
- Alpha agregat bukan reliabilitas respons individual mahasiswa.
- Laporkan level analisis, N, butir, dan missing-value policy.
- Alpha tinggi tidak meniadakan masalah pengukuran.
- Korelasi dimensi agregat tidak membuktikan halo effect mahasiswa.
- Spearman tinggi tidak menjamin seluruh posisi dosen stabil.
- Nilai RPI bersifat cohort-relative.
- Nilai 50 bukan standar kelulusan atau kinerja absolut.
- Perbandingan waktu/institusi memerlukan reference calibration
  atau equating yang dapat dipertanggungjawabkan.
- Tanpa data berulang, longitudinal monitoring merupakan potensi
  pengembangan, bukan hasil empiris.
- Label kuadran harus deskriptif, tanpa klaim koreksi bias.

## Analisis wajib

- Rekonsiliasi data dan cohort.
- Deskriptif, skewness, excess kurtosis, IQR, maksimum, dan ties.
- Alpha dengan level agregasi eksplisit.
- Pearson antardimensi.
- Skor mentah, rank, p, z, C, dan RPI.
- Spearman, Kendall tau-b, perpindahan posisi, persentil, dan kuadran.
- Shapiro–Wilk pada cohort final jika tetap digunakan.
- Jangan membawa W/p dari cohort lama.
- Sensitivitas terhadap preprocessing dan perubahan pembobotan.

Worked examples harus menunjukkan:
input agregat, jumlah rekaman, skor dimensi, rank, p, z, C, RPI,
dan posisi untuk beberapa kode anonim.

## Simulasi korelasi moderat

Tujuan: menguji sensitivitas kesepakatan ranking, bukan membuktikan
validitas pengukuran.

Desain awal:
- Gaussian copula dengan marginal empiris empat dimensi dipertahankan.
- Kombinasi baris baru adalah sintetis.
- Latent correlation: 0.30, 0.50, 0.70, 0.98.
- Laporkan Pearson aktual yang dihasilkan.
- N mengikuti cohort yang dibekukan.
- Awal: 200 pengulangan, seed 20261004.
- Catat generator PRNG dan prosedur sampling.
- Bobot mentah dan RPI sama.
- Laporkan Spearman dan perpindahan posisi.
- Interval antar-pengulangan bukan confidence interval populasi.

Generator berbeda tidak menjamin angka identik dengan audit chat.
Jelaskan perbedaan implementasi; jangan memaksakan hasil.

## Checklist reviewer

| ID | Pekerjaan |
|---|---|
| A1 | Verifikasi judul referensi, nama jurnal lengkap, dan gaya IEEE |
| A2a | Tambahkan 3–5 referensi relevan untuk ceiling dan untuk transformasi |
| A2b | Jelaskan jenis transformasi dan perbedaan studi pembanding |
| A3a | Diagram: preprocessing → agregasi → dimensi → Rankit → komposit → RPI |
| A3b | Label Q1–Q4 dan definisi kuadran konsisten |
| A4a | Jelaskan 0.375 dan 0.25 dengan rujukan primer |
| A4b | Jelaskan 50, 10, dan SD aktual |
| A5a–e | Contoh input agregat → Rankit → RPI untuk beberapa dosen anonim |
| A6 | Matched weights, korelasi moderat, perpindahan posisi, literatur |
| A7 | Contoh visualisasi/persentil; batasi klaim longitudinal |
| B1 | Operasionalisasi ceiling yang defensibel |
| B2 | Level dan prosedur reliabilitas |
| B3 | Formulasi RPI lengkap dan reproducible |
| B4 | Bedakan normalisasi dari validitas |
| B5 | Moderasi interpretasi halo effect |
| B6 | Jelaskan cohort relativity dan batas perbandingan |
| B7 | Perbaiki diagram dan bahasa Inggris |

B1–B7 adalah kategori internal untuk komentar naratif Reviewer B,
bukan nomor resmi reviewer. Simpan komentar asli ketika tersedia.

## Ketentuan editorial JUITA

- Baca author guidelines, template, dan surat keputusan.
- Gunakan IMRaD dan sitasi IEEE.
- Ketentuan jurnal mengatasi default gaya APA untuk naskah ini.
- Seluruh teks publikasi, termasuk gambar, menggunakan English.
- Maksimum 10 halaman menurut surat editor.
- Verifikasi apakah matrix termasuk batas halaman; jangan menebak.
- Sorot revisi secara konsisten.
- Jangan menimpa submitted manuscript.
- Lampirkan Matrix of Revision Note pada akhir naskah.
- Isi matrix: komentar → respons → perubahan → bukti → lokasi final.
- Nomor halaman diisi setelah layout final diverifikasi.
- Jangan menyatakan komentar selesai jika bukti/output belum ada.
- Sitasi JUITA harus relevan secara substantif.
- Nama, urutan penulis, afiliasi, dan email mengikuti submission
  yang terverifikasi.

## Struktur repo

Buat folder ketika diperlukan:
- README.md: tujuan, environment, input contract, reproduksi.
- data/README.md: schema tanpa data sensitif.
- src/: preprocessing, scoring, diagnostics, simulation.
- notebooks/: eksplorasi yang memakai fungsi src/.
- configs/: cohort, bobot, ties, seed, parameter.
- results/: output publik yang diizinkan dan manifest.
- manuscript/: draft revisi.
- revision/: protocol, decision log, reviewer matrix.
- tests/: pengujian substantif pipeline.

Gunakan Python dengan environment terkunci untuk pipeline utama
setelah runtime tersedia. Notebook tidak boleh memiliki rumus berbeda
atau bergantung pada state tersembunyi.

Setiap run mencatat:
input hash, config, dependencies, commit, timestamp, counts, dan output.

CI memakai data sintetis dan tidak membutuhkan data EDOM privat.

## Verifikasi dan cara bekerja

Uji substantif:
- Parsing sel invalid dan aturan eksklusi.
- Agregasi dan pemetaan dimensi.
- Bobot dan matched-weight comparator.
- Ties, arah ranking, dan p dalam (0,1).
- Ketergantungan SD RPI pada covariance.

Bandingkan keluaran baru dengan arsip dan jelaskan selisih.
Jangan mengklaim pengujian yang belum dijalankan.

Urutan prioritas:
1. Input contract, .gitignore, dan aturan preprocessing.
2. Rekonsiliasi identitas, nilai rusak, label generik, dan periode.
3. Pipeline empiris serta sensitivitas dengan provenance.
4. Pembekuan dataset dan formulasi.
5. Worked examples, tabel, gambar, dan simulasi.
6. Revisi naskah, referensi, dan revision matrix.
7. Pemeriksaan format dan konsistensi semua angka.

Lanjutkan pekerjaan reversible yang telah diminta tanpa konfirmasi
rutin. Jika fakta institusional belum diketahui, kerjakan bagian
independen lalu tanyakan informasi minimum yang diperlukan.

Catat keputusan, status, dan blockers dalam repo; jangan bergantung
pada ingatan chat.

Jangan melakukan submission jurnal, mengubah visibility/sharing,
mempublikasikan data institusi, atau mengubah ILAD tanpa instruksi
penulis untuk tindakan tersebut.
## Preferensi bahasa dan pengamanan berkas lokal

Untuk penyuntingan paper, gunakan bahasa manusiawi, lugas, runtut,
dan formal. Bangun alur masalah, alasan pemilihan metode, hasil, serta
makna hasil. Pembahasan menafsirkan angka, bukan mengulang tabel.
Pertahankan istilah teknis yang lebih tepat dalam bahasa Inggris.
Pertahankan fakta, persamaan, sitasi, ketidakpastian, dan batas klaim.
Tidak adanya perbedaan signifikan bukan bukti kesetaraan.

Rujukan gaya pengguna:
F:/My Drive/kuliahS3/Dissertation_Writing/03_Papers/syarat_lulus/submit 2/IJC_Difficulty_Control_Rekomendasi_Pendidikan_Bahasa_Indonesia.pdf
Gunakan hanya sebagai contoh gaya dan alur, bukan sumber fakta atau
alasan memperkuat klaim. Ketentuan English untuk publikasi JUITA tetap berlaku.

Simpan seluruh data institusional dan turunannya di data/ atau private/.
Simpan roster dan pemetaan identitas di private/. Folder results/ dan
notebooks/ diabaikan secara default karena dapat memuat data privat.
Output yang telah ditinjau dan diizinkan untuk publikasi ditempatkan di
public_results/. Contoh sintetis ditempatkan di examples/synthetic/ dan
harus diberi label sintetis. Pengecualian .gitignore bukan izin publikasi.
Jangan menggunakan git add -f untuk melewati perlindungan data privat.

Sebelum commit, periksa git status, git diff --cached, dan git ls-files,
termasuk isi notebook, metadata, log, serta arsip. .gitignore tidak
melindungi berkas yang sudah terlacak dan tidak menghapus riwayat Git.
Jika data sensitif ditemukan terlacak, hentikan publikasi dan laporkan
lokasinya tanpa menampilkan identitas; jangan menulis ulang riwayat
atau menghapus sumber asli secara otomatis.