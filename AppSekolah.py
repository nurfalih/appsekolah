import streamlit as st


st.write("""
# KUMPULAN SEKOLAH TERBAIK SMP DAN SMA
Website by Nurfalih and Hosting by Streamlit
""")

st.subheader("Sekolah Terbaik Saat ini")
from PIL import Image
image = Image.open('![](../../Downloads/SMAN1Tangerang..jpg)')

st.image(image, caption='Sekolah SMAN 1 Tangerang Selatan')