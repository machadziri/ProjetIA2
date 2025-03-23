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
-Ouvrir le terminal

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

---

## Projet d'Analyse de Sentiment
===========================

**Objectif**
--------------
Ce projet a pour but de développer un modèle d'analyse de sentiment utilisant le machine learning pour prédire si un texte exprimé est de nature positive ou négative. L'objectif est de permettre à une application d'analyser des retours d'utilisateurs (comme des avis de produits ou des commentaires sur les réseaux sociaux) et de déterminer leur sentiment.

**Technologies utilisées**
--------------------------
- C# (pour le développement de l'application)
- Microsoft ML.NET (pour le machine learning)
- Modèle de régression logistique pour la classification binaire
- Visual Studio Code (environnement de développement)

**Fichiers inclus**
------------------
- `Program.cs` : Script principal qui charge les données, entraîne le modèle et permet la prédiction des sentiments.
- `sentiment_model.zip` : Le modèle de machine learning entraîné.
- `sentiment_data.tsv` : Jeu de données contenant des exemples de texte et leurs sentiments associés.
- `README.md` : Ce fichier d'information.

**Lancer le projet**
-------------------
1. Ouvrir Visual Studio Code ou un terminal avec C# installé.
2. Clonez ce dépôt dans votre environnement local.
3. Chargez le fichier `Program.cs` et exécutez le projet.

**Fonctionnalités**
-------------------
- **Entraînement et évaluation** : Le modèle est formé sur des données de sentiments étiquetées, puis évalué avec des métriques telles que la précision, le score F1, et l'AUC.
- **Prédiction** : L'utilisateur peut entrer un texte, et le modèle prédira si le sentiment est positif ou négatif, avec un score de confiance.

**Exemple d'utilisation**
-------------------------
Entrez un texte pour analyser le sentiment :
- "I love this movie!" -> Sentiment prédit : Positif 😊
- "This product is awful." -> Sentiment prédit : Négatif 😡

**Auteur**
----------
Robin Jung
Mars 2025
