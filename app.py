import streamlit as st
import pickle
import pandas as pd
from PIL import Image

def recommend(movie):

    movie_index = movies[movies['search_title'] == movie].index[0]
    distances1 = similar1[movie_index]
    distances2 = similar2[movie_index]
    distances3 = similar3[movie_index]

    movies_list1 = sorted(list(enumerate(distances1)),reverse=True, key=lambda x:x[1])[1:4]
    movies_list2 = sorted(list(enumerate(distances2)),reverse=True, key=lambda x:x[1])[1:4]
    movies_list3 = sorted(list(enumerate(distances3)),reverse=True, key=lambda x:x[1])[1:4]

    recommended_movies = []

    for i in movies_list1:
        recommended_movies.append(movies.iloc[i[0]].title)

    for j in movies_list2:
        recommended_movies.append(movies.iloc[j[0]].title)

    for k in movies_list3:
        recommended_movies.append(movies.iloc[k[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similar1 = pickle.load(open('similar1.pkl', 'rb'))
similar2 = pickle.load(open('similar2.pkl', 'rb'))
similar3 = pickle.load(open('similar3.pkl', 'rb'))

image = Image.open('360_F_590754013_CoFRYEcAmLREfB3k8vjzuyStsDbMAnqC.jpg')
st.image(image, use_column_width=False)

st.title('Media Recommender System')

selected_movie_name = st.selectbox(
    "Let's get you some recommendations! Enter a movie you like:",
    movies['search_title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
