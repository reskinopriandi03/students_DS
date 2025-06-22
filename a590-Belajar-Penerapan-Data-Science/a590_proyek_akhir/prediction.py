import joblib
import pandas as pd

# === Load model, scaler, dan urutan fitur ===
model = joblib.load('model_dropout.pkl')
scaler = joblib.load('scaler_dropout.pkl')
fitur_model = joblib.load('fitur_model_dropout.pkl')

# === Input data baru (satu siswa) ===
data_baru = pd.DataFrame([{
    # Contoh nilai numerik (diisi sesuai konteks realistis)
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

    # Dummy variables hasil encoding kategorikal (contoh konfigurasi satu siswa)
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

    # Course contoh (pastikan sesuai dengan encoding Anda)
    'Course_33': 0,
    'Course_9119': 1,  # Informatics Engineering
    'Course_9147': 0,

    # Tambahkan kolom lainnya sesuai daftar fitur
    # Semua fitur yang tidak ada dalam dictionary akan ditambahkan secara otomatis di bawah
}])

# === Tambahkan fitur yang belum ada dan isi dengan 0 ===
for col in fitur_model:
    if col not in data_baru.columns:
        data_baru[col] = 0

# === Urutkan kolom sesuai urutan saat training ===
data_baru = data_baru[fitur_model]

# === Scaling fitur numerik ===
data_baru_scaled = scaler.transform(data_baru)

# === Prediksi ===
prediksi = model.predict(data_baru_scaled)

# === Interpretasi prediksi ===
label_map = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
print("Hasil prediksi:", label_map.get(prediksi[0], "Tidak diketahui"))
