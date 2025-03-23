import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Initialisation des données (on peut mettre ce que l'on veut)
data = {
    'User': [
        'Alice', 'Alice', 'Alice', 'Alice', 'Alice',
        'Bob', 'Bob', 'Bob', 'Bob',
        'Carol', 'Carol', 'Carol', 'Carol', 'Carol',
        'Dave', 'Dave', 'Dave',
        'Eve', 'Eve', 'Eve', 'Eve', 'Eve',
        'Frank', 'Frank', 'Frank', 'Frank',
        'Grace', 'Grace', 'Grace',
        'Hugo', 'Hugo', 'Hugo', 'Hugo'
    ],
    'Movie': [
        'Inception', 'Titanic', 'Avatar', 'Joker', 'Matrix',
        'Inception', 'Titanic', 'Avatar', 'Interstellar',
        'Titanic', 'Avatar', 'Matrix', 'Joker', 'Fight Club',
        'Matrix', 'Joker', 'Interstellar',
        'Inception', 'Avatar', 'Matrix', 'Joker', 'Fight Club',
        'Inception', 'Interstellar', 'Titanic', 'Avatar',
        'Titanic', 'Fight Club', 'Matrix',
        'Avatar', 'Matrix', 'Joker', 'Fight Club'
    ],
    'Rating': [
        5, 4, 4, 5, 3,
        4, 5, 4, 2,
        3, 5, 4, 4, 5,
        3, 4, 2,
        5, 4, 5, 5, 4,
        4, 3, 2, 5,
        4, 5, 3,
        4, 4, 3, 4
    ]
}

# Création de la dataframe (avec les données qu'on a créé juste avant)
df = pd.DataFrame(data)

# On fait une liste de films uniques présents dans la dataframe
all_movies = sorted(df['Movie'].unique())

# On récupère la table pivot
def get_ratings_matrix(df):
    return df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Logique de recommandation
def get_recommendations(user, df):
    ratings_matrix = get_ratings_matrix(df)
    if user not in ratings_matrix.index:
        return pd.Series()
    similarity_df = pd.DataFrame(cosine_similarity(ratings_matrix),
                                 index=ratings_matrix.index,
                                 columns=ratings_matrix.index)
    similar_users = similarity_df[user].sort_values(ascending=False)[1:]
    scores = pd.Series()
    for sim_user, score in similar_users.items():
        user_ratings = ratings_matrix.loc[sim_user]
        for movie, rating in user_ratings.items():
            if ratings_matrix.loc[user, movie] == 0:
                scores[movie] = scores.get(movie, 0) + rating * score
    return scores.sort_values(ascending=False).head(5)

# Partie interface avec Streamlit
st.title("🎥 Système de recommandation de films")

choice = st.sidebar.radio("Choisissez une action :", ["👤 Créer un profil", "🔍 Voir les recommandations"])

if "user_data" not in st.session_state:
    st.session_state.user_data = df.copy()

if choice == "👤 Créer un profil":
    st.subheader("👤 Création d'un nouveau profil")
    new_user = st.text_input("Entrez votre nom :")
    selected_movies = st.multiselect("Quels films souhaitez-vous noter ?", all_movies)

    ratings = {}
    if selected_movies:
        for movie in selected_movies:
            ratings[movie] = st.slider(f"Note pour {movie}", 1, 5, 3)

    if st.button("📅 Enregistrer mon profil"):
        new_entries = pd.DataFrame({
            'User': [new_user] * len(ratings),
            'Movie': list(ratings.keys()),
            'Rating': list(ratings.values())
        })
        st.session_state.user_data = pd.concat([st.session_state.user_data, new_entries], ignore_index=True)
        st.success(f"Profil de {new_user} enregistré avec succès !")

elif choice == "🔍 Voir les recommandations":
    st.subheader("🌟 Recommandations personnalisées")
    users = sorted(st.session_state.user_data['User'].unique())
    selected_user = st.selectbox("Choisissez un utilisateur :", users)
    if selected_user:
        recos = get_recommendations(selected_user, st.session_state.user_data)
        if not recos.empty:
            st.write(f"Films recommandés pour **{selected_user}** :")
            for movie, score in recos.items():
                st.markdown(f"- **{movie}** (score: {round(score, 2)})")
        else:
            st.warning(f"Pas assez de données pour générer des recommandations pour {selected_user}.")
