#%%
import pandas as pd
import requests, zipfile, io

#--------------------------------------------

#%% Specify the url with data

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

#--------------------------------------------

#%% read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

#--------------------------------------------

#%%

anime_data = pd.read_csv("MyAnimeList-Database-master/data/anime.csv")
anime_list = pd.read_csv("MyAnimeList-Database-master/data/animelist.csv")
anime_synopsis = pd.read_csv("MyAnimeList-Database-master/data/anime_with_synopsis.csv")

#--------------------------------------------

#%% Apenas para ter noção do que se trata

anime_data.head()

#--------------------------------------------

#%% Informações detalhadas sobre os dados

anime_data.info()

#--------------------------------------------

#%% Estatísticas sobre os dados

anime_data.describe()

#--------------------------------------------