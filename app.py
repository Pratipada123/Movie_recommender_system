import streamlit as st
import pickle
import pandas as pd

movie=pickle.load(open('Movies_recommender.pkl','rb'))
movielist=movie['title'].values
st.title('Movie Recommender System')

#def fetch_poster(movie_id):
    

# we create the same function as 'find'
def find(movie_name):
    movie_index=movie[movie['title']==movie_name].index[0]
    similar_movie=distance[movie_index]
    movie_list=sorted(list(enumerate(similar_movie)),reverse=True,key=lambda x:x[1])[1:6]


    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        # Fetch poster from API
        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies

distance=pickle.load(open('Distance.pkl','rb'))

selected_movie = st.selectbox(
    "Choose a Movie!!",movielist)

if st.button('Recommend'):
    recommendations=find(selected_movie)
    for i in recommendations:
        st.write(i)