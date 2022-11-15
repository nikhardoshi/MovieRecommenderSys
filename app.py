import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests


similarity=pickle.load(open(r'C:\Users\nikso\OneDrive\Desktop\mlproject\similarity.pkl','rb'),buffers=None)
list=pickle.load(open(r'C:\Users\nikso\OneDrive\Desktop\mlproject\movies_dict.pkl','rb'),buffers=None)
movies=pd.DataFrame.from_dict(list)

def fetch_poster(i):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(i))
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recomm(movie):
  mov_index=movies[movies['title']==movie].index[0]
  sim=similarity[mov_index]
  movlist=sorted((enumerate(sim)),reverse=True,key=lambda x:x[1])[1:6]
  
  rec_movie=[]
  posters=[]
  for i in movlist:
    # print(i[0])
    movie_id=movies.iloc[i[0]]['movie_id']
    rec_movie.append(movies.iloc[i[0]]['title'])
    posters.append(fetch_poster(movie_id))
  return rec_movie,posters

st.title('Select your movie')

selected_movie_name = st.selectbox(
     'Here is a list just for you',
     movies['title'].values)

if st.button('Recommend'):
     recom,poster=recomm(selected_movie_name)
     
     col1, col2, col3, col4, col5 = st.columns(5)

     with col1:
          st.text(recom[0])
          st.image(poster[0])

     with col2:
          st.text(recom[1])
          st.image(poster[1])

     with col3:
          st.text(recom[2])
          st.image(poster[2])

     with col4:
          st.text(recom[3])
          st.image(poster[3])

     with col5:
          st.text(recom[4])
          st.image(poster[4])

