import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=a3d824c43680b12d67e5dd68af68cf60&language=en-US".format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w185/" + data['poster_path']

def recommend(movie): # In this function if you will give it one movie it will return back with five recommended movie.
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies=[]
        recommended_movies_posters=[]
        for i in movies_list:
            movie_id = movies.iloc[i[0]].id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id)) # fetch poster from API
        return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open("movies_dict_model_wellpre.sav",'rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity_model_pre.sav",'rb'))
st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Since You Have Watched this',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
