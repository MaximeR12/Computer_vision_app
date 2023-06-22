############################
#   Importation du modèle  #
############################
from ultralytics import YOLO

model = YOLO("models/bestl.pt")

############################
#      Streamlit app       #
############################
import streamlit as st


st.title("Application Streamlit avec File Uploader")
uploaded_file = st.file_uploader("Choisissez un fichier", type=["png", "jpeg", "jpg"])
if uploaded_file is not None:
    resultat = model(uploaded_file)
    st.write(resultat)

