import streamlit as st

st.title("🐧 Penguin Predictor")

species = st.selectbox("Species", ["Adelie", "Chinstrap", "Gentoo"])

island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])

sex = st.radio("Sex", ["Male", "Female"], horizontal=True)

bill_length_mm = st.number_input(
    "Bill length (mm)", 30.0, 60.0, 44.0
)

bill_depth_mm = st.number_input(
    "Bill depth (mm)", 13.0, 22.0, 17.0
)

flipper_length_mm = st.number_input(
    "Flipper length (mm)", 170.0, 235.0, 200.0
)

st.write("Prediction goes here")

