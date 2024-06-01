# *******************************************************
# Nom ......... : streamlit_app.py
# Rôle ........ : Application de recherche d'une date de naissance dans les décimales de PI et démonstration mathématique 
#                 de la somme des nombres entiers naturels
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 1/06/2024
# Licence ..... : Réalisé dans le cadre du cours de l'Architecture des Machines
# Usage ....... : Exécuter le script avec "streamlit run streamlit_app.py" pour démarrer l'application
# *******************************************************

import streamlit as st
import os
import requests
from datetime import datetime
import locale

# Définir la locale française
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# Fonction pour télécharger et sauvegarder les décimales de PI localement
def telecharger_et_sauvegarder_decimales_pi():
    url = "https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt"
    reponse = requests.get(url)
    with open("pi_decimals.txt", "w") as f:
        f.write(reponse.text[:1000000])  # Sauvegarde le premier million de décimales

# Fonction pour charger les décimales de PI à partir d'un fichier local
def charger_decimales_pi():
    if not os.path.exists("pi_decimals.txt"):
        telecharger_et_sauvegarder_decimales_pi()
    with open("pi_decimals.txt", "r") as f:
        return f.read()

# Charger les décimales de PI une seule fois au début
decimales_pi = charger_decimales_pi().replace(".", "")

# Fonction pour rechercher la date de naissance dans les décimales de PI
def rechercher_date_naissance_dans_pi(date_naissance):
    date_naissance_str = date_naissance.replace("-", "")
    position = decimales_pi.find(date_naissance_str)
    return position

# Fonction pour calculer la somme des premières n décimales de PI
def somme_decimales_pi(n):
    return sum(int(chiffre) for chiffre in decimales_pi[:n])

# Interface Streamlit
st.title("Recherche de Date de Naissance dans les Décimales de PI")

# Entrée utilisateur pour la date de naissance
date_naissance = st.text_input("Entrez votre date de naissance (format AAAAMMJJ):")

if date_naissance:
    position = rechercher_date_naissance_dans_pi(date_naissance)
    if position != -1:
        st.write(f"Votre date de naissance se trouve à la position {position} dans les décimales de PI.")
    else:
        st.write("Votre date de naissance n'a pas été trouvée dans les premiers millions de décimales de PI.")

    # Afficher le jour de la semaine en français
    jour_de_naissance = datetime.strptime(date_naissance, '%Y%m%d').strftime('%A')
    st.write(f"Jour de naissance: {jour_de_naissance.capitalize()}")

# Calculer les sommes des décimales de PI
somme_20_decimales = somme_decimales_pi(20)
somme_144_decimales = somme_decimales_pi(144)

st.write(f"La somme des 20 premières décimales de PI est : {somme_20_decimales}")
st.write(f"La somme des 144 premières décimales de PI est : {somme_144_decimales}")

# Remarque sur les sommes calculées
st.write("Que remarquez-vous ?")
st.write("La somme des 20 premières décimales est beaucoup plus petite que celle des 144 premières, ce qui est attendu étant donné le nombre beaucoup plus élevé de termes additionnés.")

# Intégrer une vidéo
st.write("Voici une vidéo expliquant que la somme de tous les nombres entiers naturels est égale à -1/12:")
st.video("https://www.youtube.com/watch?v=w-I6XTVZXww")
