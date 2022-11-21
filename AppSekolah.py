import streamlit as st


st.write("""
# KUMPULAN SEKOLAH TERBAIK SMP DAN SMA
Website by Nurfalih and Hosting by Streamlit
""")

option = st.selectbox(
    'Tipe sekolah yang kamu sukai',
    ('Swasta', 'Negeri', 'International'))

st.write('Anda memilih sekolah:', option)

st.subheader("Sekolah Terbaik Saat ini")
if st.button('SMAN1 Tangerang Selatan'):
    st.write('Pendaftaran penerimaan peserta didik baru tingkat SMA dan SMK di wilayah Provinsi Banten resmi diumumkan mulai Rabu, 15 Juni 2022.')
if st.button('SMAS Marsudirini'):
    st.write('Berapa biaya masuk SMA Dirgantara? Orangtua atau wali murid yang memilih sekolah terbaik ketiga nasional versi LTMPT ini pasti juga mencari informasi terkait hal ini. Ternyata, sampai angkatan ke-4 atau kelas X tahun 2021, tidak ada biaya masuk SMA Pradita Dirgantara yang dikenakan.')
if st.button("SMAN 1 Bekasi"):
    st.write('Jadwal PPDB Proses seleksi realtime : 27 – 30 Juni 2022. Verifikasi faktual berkas : 04 – 06 Juli 2022. Pengumuman : 08 Juli 2022. Pendaftaran Ulang : 11 - 12 Juli 2022.')
if st.button("SMAN 3 Bekasi"):
    st.write('Sesuai hasil akhir Rapat Evaluasi PPDB yg dilaksanakan hari ini Rabu, 11 Mei 2022 yg dipimpin Kabid Pembinaan SMK selaku Ketua Panitia PPDB Disdik Provsu, maka jadwal pendaftaran Tahap I Zona II akan dibuka mulai besok, Kamis, 12 Mei 2022.')
