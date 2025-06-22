
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius berupa tingginya tingkat dropout—banyak siswa yang tidak menyelesaikan pendidikan mereka.

Manajemen ingin mengetahui sejak dini siswa-siswa yang berisiko tinggi untuk dropout agar dapat dilakukan intervensi melalui bimbingan khusus. Untuk itu, mereka membutuhkan sistem prediksi dropout berbasis data serta dashboard untuk memonitor performa siswa.

## Permasalahan Bisnis

Dropout yang tinggi menurunkan reputasi institusi dan menambah beban operasional. Jika siswa yang berisiko dropout dapat diidentifikasi lebih awal, institusi dapat merancang strategi pendampingan atau solusi akademis. Oleh karena itu, diperlukan model machine learning untuk memprediksi potensi dropout dan dashboard pemantauan yang mendukung pengambilan keputusan.

## Cakupan Proyek

* Analisis Data Siswa: Mengeksplorasi data historis siswa untuk memahami pola-pola yang berkaitan dengan risiko dropout, seperti performa akademik awal, latar belakang sosial ekonomi, dan kebiasaan pembayaran uang kuliah.
* Pembuatan Model Prediksi: Membangun model klasifikasi menggunakan Logistic Regression (dengan class_weight=balanced) untuk memprediksi status siswa: Graduate, Dropout, atau Enrolled.
* Pembuatan Business Dashboard: Membangun dashboard menggunakan Metabase untuk memvisualisasikan distribusi status siswa dan faktor-faktor utama yang berkaitan dengan dropout.
* Evaluasi dan Rekomendasi: Menganalisis performa model dan memberikan saran intervensi berdasarkan output prediksi.

## Persiapan

Sumber data:
Dataset yang digunakan dalam proyek ini dapat diakses melalui GitHub:

data asli melalui link eksternal:
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

kita bisa mengakses dengan cara kode berikut :
df = pd.read_csv('https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv', sep=';')

df.info()
print(df)
print(df.describe())

dataset juga di simpan didalam direktori proyek
a590-Belajar-Penerapan-Data-Science\a590_proyek_akhir\dataset.csv

Setup environment:

a. struktur proyek

berikut struktur proyek yang sudah dibuat di dalam folder proyek submission1
pastikan posisi terminal sudah sesuai.

SUBMISSIONAKHIR/
│
└── a590-Belajar-Penerapan-Data-Science/
    ├── .ipynb_checkpoints/
    ├── a590_proyek_akhir/
    │   ├── .ipynb_checkpoints/
    │   ├── dataset.csv
    │   ├── fitur_model_dropout.pkl
    │   ├── metabase.db.mv.db
    │   ├── model_dropout.pkl
    │   ├── notebook.ipynb
    │   ├── prediction.py
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── reskinopriandi03-dashboard.png
    │   ├── reskinopriandi03-video.webm
    │   ├── scaler_dropout.pkl
    │   └── upload_dataset.py
    │
    ├── venv/
    │
    └── README.md

b. mengaktifkan venv

untuk memudahkan dalam menjalankan dan pengembangan, maka aktifkan virtuan environment yang sudah ada di dalam folder proyek

pastikan terminal berada di dalam folder submissionAkhir\a590-Belajar-Penerapan-Data-Science>
jalankan skrip berikut untuk membuat venv :
python -m venv venv

untuk mengaktifkan venv:
 .\venv\Scripts\Activate

c. instalasi dependensi dari requriements.txt

untuk menyamakan kebutuhan teknologi di dalam proyek kita, maka buat file baru  bernama requirements.txt sejajar dengan direktori notebook.ipynb

di dalam file requirements.txt tulis kode berikut :
ipykernel==6.29.5
ipython==9.2.0
ipywidgets==8.1.7
joblib==1.5.0
jupyter==1.1.1
matplotlib==3.10.3
matplotlib-inline==0.1.7
notebook==7.4.2
numpy==2.2.5
pandas==2.2.3
scikit-learn==1.6.1
seaborn==0.13.2
tqdm==4.67.1

kemudian save dan di terminal jalankan kode berikut :

pip install -r requirements.txt

setelah environment selesai, pada terminal jalankan :

jupyter notebook

maka kita akan diarahkan ke jendela browser jupyter notebook kemudian pilih file notebook.ipynb

jalankan semua kode pada notebook.ipynb

## Business Dashboard

Dashboard dibuat menggunakan Metabase dan menampilkan:
• Distribusi dropout per jurusan.
• dropout, enrolled atau graduate berdasarkan marital status yang dikelompokan menjadi hidup berpasangan atau sendiri.
• Visualisasi jumlah siswa per negara asal

untuk menjalankan dashboard, kita perlu menjalankan aplikasi  docker desktop.

Jika file metabase.db.mv.db belum ada, buat file kosong terlebih dahulu:

New-Item D:\submissionAkhir\a590-Belajar-Penerapan-Data-Science\a590_proyek_akhir\metabase.db.mv.db

setelah file metabase.db.mv.db jadi.

jalankan kode berikut di terminal

docker run -d -p 3000:3000 --name subAkhir metabase/metabase

tunggu beberapa menit

setelah docker desktop aktif,  di terminal jalankan :

docker start subAkhir

pada jendela browser ketik  :

http://localhost:3000/

kemudian login :

Username: root@mail.com
Password: root123

dashboard berada pada :

collection>our analytics>students dashboard

Screenshot dashboard terlampir pada direktori proyek:

a590-Belajar-Penerapan-Data-Science\a590_proyek_akhir\reskinopriandi03-dashboard.png

video rekapan dashboard terlampir pada file di dalam direktori proyek:

a590-Belajar-Penerapan-Data-Science\a590_proyek_akhir\reskinopriandi03-video.webm

## Menjalankan Sistem Machine Learning

setelah kode notebook.ipynb selesai dijalankan, kembali ke vscode proyek,

* Pastikan model yang telah dilatih (model_dropout.pkl) dan scaler (scaler_dropout.pkl) tersedia di direktori proyek
* buat file prediction.py sejajar dengan direktori model_dropout.pkl, scaler_dropout.pkl, fitur_model_dropout.pkl agar mudah dijalankan
* di dalam prediction.py buat kode berikut :

import joblib

import pandas as pd

model = joblib.load('model_dropout.pkl')

scaler = joblib.load('scaler_dropout.pkl')

fitur_model = joblib.load('fitur_model_dropout.pkl')

data_baru = pd.DataFrame([{

    'Age_at_enrollment': 19,

    'Admission_grade': 160.0,

    'Curricular_units_1st_sem_grade': 13.0,

    'Curricular_units_2nd_sem_grade': 12.5,

    'Curricular_units_1st_sem_approved': 5,

    'Curricular_units_2nd_sem_approved': 4,

    'Curricular_units_1st_sem_enrolled': 6,

    'Curricular_units_2nd_sem_enrolled': 6,

    'Curricular_units_1st_sem_evaluations': 6,

    'Curricular_units_2nd_sem_evaluations': 5,

    'Curricular_units_1st_sem_credited': 0,

    'Curricular_units_2nd_sem_credited': 0,

    'Previous_qualification_grade': 170.0,

    'Unemployment_rate': 7.5,

    'Inflation_rate': 1.2,

    'GDP': 2.0,

    'Gender_1': 1,

    'Marital_status_1': 1,

    'Application_mode_1': 0,

    'Application_order': 1,

    'Daytime_evening_attendance_1': 1,

    'Previous_qualification_1': 0,

    'Nacionality_1': 1,

    'Mothers_qualification_1': 1,

    'Fathers_qualification_1': 1,

    'Mothers_occupation_1': 0,

    'Fathers_occupation_1': 0,

    'Displaced_1': 0,

    'Educational_special_needs_1': 0,

    'Debtor_1': 0,

    'Tuition_fees_up_to_date_1': 1,

    'Scholarship_holder_1': 0,

    'International_1': 0,

    'Course_33': 0,

    'Course_9119': 1,  # Informatics Engineering

    'Course_9147': 0,

}])

for col in fitur_model:

    if col notin data_baru.columns:

    data_baru[col] = 0

data_baru = data_baru[fitur_model]

data_baru_scaled = scaler.transform(data_baru)

prediksi = model.predict(data_baru_scaled)

label_map = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}

print("Hasil prediksi:", label_map.get(prediksi[0], "Tidak diketahui"))

## Conclusion

Model Logistic Regression yang dibangun dalam proyek ini berhasil mencapai akurasi sebesar 72.09%, dengan performa yang cukup baik dalam mengidentifikasi pelajar yang berisiko dropout (kelas 1). Dengan recall sebesar 76% dan precision sebesar 77% untuk kelas dropout, model ini berpotensi digunakan sebagai alat bantu deteksi dini dalam sistem akademik.

Temuan dari dashboard visualisasi juga memberikan konteks penting bagi pengambilan keputusan kebijakan. Meskipun mahasiswa berasal dari berbagai negara, sekitar 97% berasal dari Portugal, sehingga strategi intervensi sebaiknya tetap mempertimbangkan karakteristik lokal.

Analisis terhadap status pernikahan menunjukkan bahwa pelajar yang hidup berpasangan atau memiliki tanggungan (married, facto union) memiliki tingkat dropout yang lebih tinggi dibandingkan mereka yang hidup sendiri atau tanpa tanggungan (single, widower, divorced, legally separated). Hal ini mengindikasikan bahwa tanggung jawab rumah tangga dapat menjadi faktor risiko dropout, dan patut menjadi perhatian dalam perumusan kebijakan dukungan mahasiswa.

Secara keseluruhan, proyek ini tidak hanya membangun model prediktif, tetapi juga membuka wawasan untuk pendekatan yang lebih personal dan kontekstual terhadap isu dropout dalam pendidikan tinggi.

## Rekomendasi Action Items

Berdasarkan hasil model dan analisis data yang dilakukan, berikut adalah beberapa langkah strategis yang dapat diambil untuk mengurangi angka dropout:

Program Dukungan untuk Mahasiswa Berpasangan: Mengingat mahasiswa yang hidup berpasangan menunjukkan tingkat dropout lebih tinggi, kampus dapat menyediakan program bantuan seperti konseling keluarga, fleksibilitas jadwal, atau dukungan finansial bagi mereka yang memiliki tanggungan.

Pendeteksian Dini dan Intervensi Proaktif: Gunakan model prediksi ini untuk mengidentifikasi mahasiswa berisiko secara dini. Intervensi bisa berupa pendekatan personal oleh dosen wali, pemberian beasiswa berbasis risiko, atau sistem peringatan akademik.

Peningkatan Dukungan Akademik dan Sosial: Bangun sistem peer mentoring, komunitas belajar, dan layanan kesehatan mental agar mahasiswa merasa lebih didukung secara holistik.

Penyesuaian Kebijakan Berdasarkan Konteks Lokal: Dengan mayoritas mahasiswa berasal dari Portugal (±97%), kebijakan kampus harus mempertimbangkan norma budaya dan sosial lokal untuk menjamin efektivitas program dukungan.

Evaluasi Model Berkala & Iterasi: Lakukan pemantauan performa model secara periodik. Gunakan data terbaru dan pertimbangkan untuk menerapkan model lain (Random Forest, Gradient Boosting) atau teknik balancing seperti SMOTE untuk meningkatkan akurasi dan generalisasi model.
