import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index = new_movies[new_movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []


    for i in movies_list:
        recommended_movies.append(new_movies.iloc[i[0]].title)
    return recommended_movies

movie_dict=pickle.load(open('movies.pkl','rb'))
new_movies=pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation system')

Selected_Movie_Name = st.selectbox(
    'Select what you like',new_movies['title'].values)


if st.button('Recommend Movie'):
    recommendations = recommend(Selected_Movie_Name)
    for i in recommendations:
        st.write(i)