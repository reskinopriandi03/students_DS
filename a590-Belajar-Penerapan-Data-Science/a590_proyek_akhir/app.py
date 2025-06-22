import streamlit as st
import joblib
import pandas as pd

st.title("Prediksi Risiko Dropout Mahasiswa")

# Load model, scaler, dan fitur
model = joblib.load('model_dropout.pkl')
scaler = joblib.load('scaler_dropout.pkl')
fitur_model = joblib.load('fitur_model_dropout.pkl')

# Mapping untuk opsi dropdown
marital_status_map = {
    1: "Single",
    2: "Married",
    3: "Widower",
    4: "Divorced",
    5: "Facto Union",
    6: "Legally Separated"
}

country_map = {
    1: "Portugal",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Guinean",
    24: "Mozambican",
    25: "Cape Verdean",
    26: "Sao Tomean",
    32: "Brazilian",
    41: "Romanian",
    62: "Moldova (Republic of)",
    100: "Turkish",
    101: "Russian",
    103: "Mexican",
    105: "Ukrainian",
    108: "Chilean",
    109: "Venezuelan"
}

# Form input pengguna
st.header("Masukkan Data Mahasiswa")
input_data = {}

# Contoh input numerik
input_data['Age_at_enrollment'] = st.number_input("Umur saat masuk", min_value=15, max_value=60, value=19)
input_data['Admission_grade'] = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=160.0)
input_data['Curricular_units_1st_sem_grade'] = st.number_input("Nilai Semester 1", min_value=0.0, max_value=20.0, value=13.0)
input_data['Curricular_units_2nd_sem_grade'] = st.number_input("Nilai Semester 2", min_value=0.0, max_value=20.0, value=12.5)
input_data['Previous_qualification_grade'] = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, value=170.0)
input_data['Unemployment_rate'] = st.number_input("Unemployment Rate", min_value=0.0, max_value=100.0, value=7.5)
input_data['Inflation_rate'] = st.number_input("Inflation Rate", min_value=0.0, max_value=100.0, value=1.2)
input_data['GDP'] = st.number_input("GDP", min_value=-10.0, max_value=20.0, value=2.0)

# Marital Status (dropdown)
marital_status = st.selectbox("Status Pernikahan", options=list(marital_status_map.keys()), format_func=lambda x: marital_status_map[x])
for i in range(1, 7):
    input_data[f'Marital_status_{i}'] = 1 if marital_status == i else 0

# Country (dropdown)
country = st.selectbox("Asal Negara", options=list(country_map.keys()), format_func=lambda x: f"{x} - {country_map[x]}")
for i in country_map.keys():
    input_data[f'Nacionality_{i}'] = 1 if country == i else 0

# Contoh input kategorikal biner
input_data['Gender_1'] = st.selectbox("Jenis Kelamin", options=[0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
input_data['Application_mode_1'] = st.selectbox("Application Mode 1", options=[0, 1])
input_data['Application_order'] = st.number_input("Application Order", min_value=1, max_value=10, value=1)
input_data['Daytime_evening_attendance_1'] = st.selectbox("Daytime/Evening Attendance", options=[0, 1], format_func=lambda x: "Daytime" if x == 1 else "Evening")
input_data['Previous_qualification_1'] = st.selectbox("Previous Qualification 1", options=[0, 1])
input_data['Mothers_qualification_1'] = st.selectbox("Ibu Lulusan Perguruan Tinggi", options=[0, 1])
input_data['Fathers_qualification_1'] = st.selectbox("Ayah Lulusan Perguruan Tinggi", options=[0, 1])
input_data['Mothers_occupation_1'] = st.selectbox("Ibu Bekerja", options=[0, 1])
input_data['Fathers_occupation_1'] = st.selectbox("Ayah Bekerja", options=[0, 1])
input_data['Displaced_1'] = st.selectbox("Displaced", options=[0, 1])
input_data['Educational_special_needs_1'] = st.selectbox("Kebutuhan Khusus", options=[0, 1])
input_data['Debtor_1'] = st.selectbox("Debtor", options=[0, 1])
input_data['Tuition_fees_up_to_date_1'] = st.selectbox("Uang Kuliah Lunas", options=[0, 1])
input_data['Scholarship_holder_1'] = st.selectbox("Penerima Beasiswa", options=[0, 1])
input_data['International_1'] = st.selectbox("Mahasiswa Internasional", options=[0, 1])

# Course (dropdown)
course_map = {
    33: "Course 33",
    9119: "Informatics Engineering",
    9147: "Course 9147"
}
course = st.selectbox("Program Studi", options=list(course_map.keys()), format_func=lambda x: course_map[x])
for i in course_map.keys():
    input_data[f'Course_{i}'] = 1 if course == i else 0

# Input numerik lain (bisa disesuaikan dengan fitur model Anda)
input_data['Curricular_units_1st_sem_approved'] = st.number_input("Mata Kuliah Lulus Semester 1", min_value=0, max_value=10, value=5)
input_data['Curricular_units_2nd_sem_approved'] = st.number_input("Mata Kuliah Lulus Semester 2", min_value=0, max_value=10, value=4)
input_data['Curricular_units_1st_sem_enrolled'] = st.number_input("Mata Kuliah Diambil Semester 1", min_value=0, max_value=10, value=6)
input_data['Curricular_units_2nd_sem_enrolled'] = st.number_input("Mata Kuliah Diambil Semester 2", min_value=0, max_value=10, value=6)
input_data['Curricular_units_1st_sem_evaluations'] = st.number_input("Evaluasi Semester 1", min_value=0, max_value=10, value=6)
input_data['Curricular_units_2nd_sem_evaluations'] = st.number_input("Evaluasi Semester 2", min_value=0, max_value=10, value=5)
input_data['Curricular_units_1st_sem_credited'] = st.number_input("SKS Diakui Semester 1", min_value=0, max_value=10, value=0)
input_data['Curricular_units_2nd_sem_credited'] = st.number_input("SKS Diakui Semester 2", min_value=0, max_value=10, value=0)

# Prediksi jika tombol ditekan
if st.button("Prediksi"):
    df = pd.DataFrame([input_data])
    # Pastikan semua fitur ada
    for col in fitur_model:
        if col not in df.columns:
            df[col] = 0
    df = df[fitur_model]
    df_scaled = scaler.transform(df)
    pred = model.predict(df_scaled)
    label_map = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
    st.success(f"Hasil prediksi: **{label_map.get(pred[0], 'Tidak diketahui')}**")