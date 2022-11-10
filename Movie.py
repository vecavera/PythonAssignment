#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


#Isprobavanje dobijanja informacija o jednom filmu

api_key = '8f0d9811'
title = 'Focus'
year = '2015'
movieInfo = requests.get('http://www.omdbapi.com/?apikey='+api_key+'&t='+title+'&y='+year).json()
movieInfo


# In[3]:


#Ucitavanje imena filmova dok se ne prosledi niska "end"
titles = []

print("Input movie titles or end")
while True:
    line = input()
    if (line == 'end'):
        break;
    titles.append(line)


# In[4]:


#Dohvatanje informacija o unetim filmovima
movies = []
for title in titles:
    info =  requests.get('http://www.omdbapi.com/?apikey='+api_key+'&t='+title).json()
    movies.append(info)


# In[5]:


#Ispisivanje filmova
for movie in movies:
    print(movie)


# In[6]:


#DataFrame radi lakseg filtriranja
import pandas as pd


# In[7]:


df = pd.DataFrame(movies)
df


# In[8]:


df.dropna()


# In[9]:


#Unosenje IMDB rejtinga i zanra
imdb_rating = input("Input IMDB rating")
genre = input("Input genre")


# In[10]:


#Izbacivanje redova kod kojih nije naveden uneti zanr
for i,genreRow in enumerate (df['Genre']):
    if genre not in genreRow:
        df.drop(i,inplace=True)        


# In[11]:


df


# In[12]:


#Promena tipa kolone imdbRating iz object u float radi filtriranja po vrednosti vecoj ili jednakoj od unete
df['imdbRating']=pd.to_numeric(df['imdbRating'])


# In[13]:


df.dtypes


# In[14]:


#Filtriranje po koloni imdbRating 
df_filtered = df[df['imdbRating'] >= pd.to_numeric(imdb_rating)]


# In[15]:


df_filtered


# In[16]:


#Ispisivanje rezultata u datoteku out.txt
df_filtered.to_csv('out.txt', header=False, index = False)

