
==============================
Projet IA : Système de recommandation de films
==============================

Objectif
-----------
Ce projet s'inscrit dans le cadre de l'utilisation du filtre collaboratif.

Technologies utilisées
--------------------------
- Python 3.9
- pandas
- scikit-learn (pour la similarité cosinus)
- Streamlit (interface utilisateur interactive)

Fichiers inclus
------------------
- projet.py : Script principal Streamlit de l'application
- README.txt : Ce fichier d'information

Lancer le projet
-------------------

Lance l'application :
   streamlit run projet.py

Fonctionnalités
-------------------
- Deux boutons dans l'interface :
  1. Créer un profil : l'utilisateur entre son nom et donne une note à des films de son choix.
  2. Voir les recommandations : choisir un utilisateur existant pour afficher les films qui lui sont recommandés.

- Le système repose sur une matrice utilisateur/film et une mesure de similarité cosinus.

Auteur : Macha DZIRI
Date : Mars 2025