############################
#   Importation du modèle  #
############################
from ultralytics import YOLO

model = YOLO("models/best_v2.pt")

############################
#      Streamlit app       #
############################
import streamlit as st
from PIL import Image

st.title("Soda brand detector")
st.write("By Emmanuel & Maxime")
uploaded_files = st.file_uploader("Entrez un image", type=["png", "jpeg", "jpg"], accept_multiple_files=True)
if uploaded_files :
    for file in uploaded_files:         # Boucle for pour ouvrir toutes les images si on en a plusieurs
        image_base = Image.open(file)   # Utilisation la librairie PIL pour transformer l'image
        st.image(image_base)            # L'image non moidifiée/prédite s'affiche
        result = model(image_base)      # Prediction effectuée sur l'image
        st.image(result[0].plot())      # la prediction est une liste mais la methode plot sert a retransformer en image

