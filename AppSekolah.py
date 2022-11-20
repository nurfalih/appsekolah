import streamlit as st


st.write("""
# KUMPULAN SEKOLAH TERBAIK SMP DAN SMA
Website by Nurfalih and Hosting by Streamlit
""")

st.subheader("Sekolah Terbaik Saat ini")
if st.button('SMAN1 Tangerang Selatan'):
    st.write('Pendaftaran penerimaan peserta didik baru tingkat SMA dan SMK di wilayah Provinsi Banten resmi diumumkan mulai Rabu, 15 Juni 2022.')
B = st.button("SMAS Marsudirini")
C = st.button("SMAN 1 Bekasi")
D = st.button("SMAN 3 Bekasi")

st.write(A)