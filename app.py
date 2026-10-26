import streamlit as st

st.title("Contoh Program Streamlit")
with st.form(key="my_form"):
    Nama = st.text_input("Nama Lengkap")
    Jenis_Kelamin = st.radio("Jenis Kelamin", ("Lanang", "Women"))
    submit = st.form_submit_button(label="Kirim")
