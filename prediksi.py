import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Muat model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Untuk masukkan css
def load_custom_css():
    with open("style/custom.css", "r") as css_file:
        st.markdown('<style>{}</style>'.format(css_file.read()), unsafe_allow_html=True)

# Buat aplikasi Streamlit
def app():
    
    # css
    load_custom_css()

    st.markdown("""
    <div style="text-align:center">
        <h1>PREDIKSI DIABETES</h1>
    </div>
""", unsafe_allow_html=True)

    # Menginisialisasi variabel input 
    nama = ""
    alamat = ""
    jenis_kelamin = ""
    pregnancies = 0
    glucose = 0
    blood_pressure = 0
    skin_thickness = 0
    insulin = 0
    bmi = 0.0
    dpf = 0.0
    age = 0

    st.write("#")

    # Inisialisasi diab_diagnosis
    diab_diagnosis = ''

    # Membuat formulir untuk input pengguna
    with st.form('user_input'):

    # Tambahkan fields untuk identitas
        st.markdown("""
    <div style="text-align:center">
        <h2>Identitas Pasien</h2>
    </div>
""", unsafe_allow_html=True)
        
        # Menambahkan label untuk Nama, Alamat, dan Jenis Kelamin
        st.markdown('<label for="nama" class="stLabel">Nama</label>', unsafe_allow_html=True)
        nama = st.text_input('', key="nama")
        st.markdown('<label for="alamat" class="stLabel">Alamat</label>', unsafe_allow_html=True)
        alamat = st.text_area('', key="alamat")
        st.markdown('<label for="jenis_kelamin" class="stLabel">Jenis Kelamin</label>', unsafe_allow_html=True)
        jenis_kelamin = st.selectbox('', ['Pria', 'Wanita'], key="jenis_kelamin")

        # bagian data pasien
        st.markdown("<h2 style='text-align: center;'>Data Pasien</h2>", unsafe_allow_html=True)
        st.write("\n")  # untuk membuat jarak

        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
            glucose = st.number_input('Glucose Level', min_value=0, step=1)
            blood_pressure = st.number_input('Blood Pressure', min_value=0, step=1)
            skin_thickness = st.number_input('Skin Thickness', min_value=0, step=1)
        with col2:
            insulin = st.number_input('Insulin Level', min_value=0, step=1)
            bmi = st.number_input('BMI', min_value=0.0)
            dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0)
            age = st.number_input('Age', min_value=0, step=1)

        # Menambahkan tombol tes diabetes
        submit_button = st.form_submit_button(label='Tes Diabetes')

     # Untuk Prediksi
    if submit_button:
        if not nama or not alamat:
            st.error('Silakan isi Identitas Anda dengan benar.')
        else:
            
            # Melakukan prediksi
            diab_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

            if (diab_prediction[0] == 0):
                diab_diagnosis = 'Anda Tidak Menderita diabetes'
            else:
                diab_diagnosis = 'Anda Menderita diabetes'

    # Menampilkan hasil diagnosis
    st.title('HASIL PREDIKSI')

    # Menampilkan hasil diagnosis di kotak hijau
    if diab_diagnosis:

           background_color = "#007acc" if diab_diagnosis == "Anda Menderita Diabetes" else "#007acc"
           text_color = "white"
           st.markdown(
                f"""
                <div style="background-color:{background_color}; padding:15px; border-radius:10px; text-align:center; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <h3 style="color:{text_color}; font-size:24px;">{diab_diagnosis}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Visualisasi data pasien
    st.write("##")
    st.write("---")
    if diab_diagnosis:
        st.markdown('<div style="text-align:center"><h2>Persentase Atribut Kesehatan Pasien</h2></div>', unsafe_allow_html=True)
        data_pasien = {
            'Attribute': ['Number of Pregnancies', 'Glucose Level', 'Blood Pressure', 'Skin Thickness', 'Insulin Level', 'BMI', 'Diabetes Pedigree Function'],
            'Value': [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf]
        }
        df_data_pasien = pd.DataFrame(data_pasien)

        st.markdown('<div id="visualization"></div>', unsafe_allow_html=True)

        fig, ax = plt.subplots()
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#c2c2f0', '#ffb3e6', '#c2f0c2']
        ax.pie(df_data_pasien['Value'], labels=df_data_pasien['Attribute'], autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal') 
        
        st.pyplot(fig)


        # untuk tombol reset
        button_container = st.columns(1)

        if button_container[0].button('Reset'):
            nama = ""
            alamat = ""
            jenis_kelamin = ""
            pregnancies = 0
            glucose = 0
            blood_pressure = 0
            skin_thickness = 0
            insulin = 0
            bmi = 0.0
            dpf = 0.0
            age = 0
            diab_diagnosis = ""
