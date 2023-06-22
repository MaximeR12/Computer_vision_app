import streamlit as st
from PIL import Image
# Titre de l'application
from ultralytics import YOLO

modele= YOLO("best.pt")


# Titre de l'application
st.title("Prédiction d'image")

# Interface utilisateur pour télécharger l'image
img = st.file_uploader("Sélectionnez une image", type=['png', 'jpg', 'jpeg'])

# Vérifier si une image a été téléchargée
predictions = modele(img)
    
# Afficher les résultats de la prédiction
st.subheader("Résultats de la prédiction :")
for i, pred in enumerate(predictions.pred):
        st.write(f"Prédiction {i+1}:")
        st.write(f"Classe : {pred['class']}")
        st.write(f"Confiance : {pred['confidence']}")
        st.write(f"Coordonnées de la boîte englobante : {pred['bbox']}")
        st.image(pred['image'], use_column_width=True)