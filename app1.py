import os
import gdown

MODEL_PATH = "similarity.pkl"
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1_kGQusNvwK9oPUn2-x4lzOTOi6Ez8W7y"
    print("Downloading model file...")
    gdown.download(url, MODEL_PATH, quiet=False)

import streamlit as st
import pickle
import pandas as pd
import requests


import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("TMDB API response:", data)  # <--- ADD THIS LINE
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return "https://via.placeholder.com/500x750?text=Poster+Error"



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from tmdb api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
   names, posters = recommend(selected_movie_name)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
       st.header(names[0])
       st.image(posters[0])
   with col2:
       st.header(names[1])
       st.image(posters[1])
   with col3:
       st.header(names[2])
       st.image(posters[2])
   with col4:
       st.header(names[3])
       st.image(posters[3])
   with col5:
       st.header(names[4])
       st.image(posters[4])
