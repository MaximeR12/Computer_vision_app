# Application de vision par ordinateur YOLO-v8


La problématique utilitaire que nous avons posé pour ce projet est de répondre à un compagnie qui se charge d'étudier la popularité des marques sur les réseaux sociaux. A partir des images fournies au modéle, la compganie va pouvoir donner des chiffres de la popularité d'une marque précise sur ces réseaux sociaux.
Notre modele a pour objectif de détecter les canettes/bouteiles des marques "sprite", "pepsi", "mirinda", "7up" dans une image extérieure.
Pour ce faire nous avons utilisé Yolov8 comme modéle de base et les poids ré-entraînés de COCO pour l'initialiser.
L'ensemble de données utilisé pour ce modéle a été récupéré sur Roboflow.

Un transfert d'apprentissage en ré-entraînant notre modèle YOLO-v8 a été effectué sur notre ensemble de données.
Le but est de permettre aux utilisateurs de télécharger une image et  d'obtenir des prédictions (boîtes englobantes et classes).

# Installation

Pour exécuter l'application, suivez les étapes suivantes :

    Cloner le dépôt avec git clone 
    Installer les dépendances requises : pip install -r requirements.txt
    Exécuter l'application : streamlit run app.py

# Utilisation

Une fois l'application en cours d'exécution, vous pouvez y accéder via l'URL fournie. L'interface utilisateur vous permettra d'utiliser les fonctionnalités souhaitées avec le téléchargement d'images pour effectuer des prédictions.
