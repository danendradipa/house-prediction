import streamlit as st
import joblib
import pandas as pd

# Load model yang dibuat
model = joblib.load('lr_house.joblib')

st.title("Prediksi Harga Rumah 🏡")
st.header("Masukkan Detail Rumah")

# Input data dari pengguna
lb = st.number_input("Luas Bangunan (m²)", min_value=0)
lt = st.number_input("Luas Tanah (m²)", min_value=0)
kt = st.number_input("Jumlah Kamar Tidur", min_value=0)
km = st.number_input("Jumlah Kamar Mandi", min_value=0)
grs = st.number_input("Jumlah Garasi", min_value=0)

if st.button("Prediksi Harga"):
    if lb <= 0 or lt <= 0 or kt <= 0 or km <= 0:
        st.error("Input tidak valid: Luas bangunan, luas tanah, jumlah kamar tidur, dan jumlah kamar mandi tidak boleh 0.")
    else:
        # Membuat DataFrame untuk input sesuai dengan nama kolom yang digunakan saat training
        input_data = pd.DataFrame([[lb, lt, kt, km, grs]], columns=['lb', 'lt', 'kt', 'km', 'grs'])
        
        # Memprediksi Harga
        predicted_price = model.predict(input_data)
        
        # Menampilkan hasil input dan prediksi
        st.subheader("Detail Input Rumah:")
        st.write(f"Luas Bangunan: **{lb} m²**")
        st.write(f"Luas Tanah: **{lt} m²**")
        st.write(f"Jumlah Kamar Tidur: **{kt}**")
        st.write(f"Jumlah Kamar Mandi: **{km}**")
        st.write(f"Jumlah Garasi: **{grs}**")
        
        # Menampilkan Harga 
        st.success(f"Harga Rumah: **Rp {predicted_price[0]:,.0f}**")
