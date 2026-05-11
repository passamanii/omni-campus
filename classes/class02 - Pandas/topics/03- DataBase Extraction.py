#%% Importanto a database de animes

import pandas as pd
import zipfile, io, requests

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'
r = requests.get(url, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
anime_data = pd.read_csv("MyAnimeList-Database-master/data/anime.csv")
anime_list = pd.read_csv("MyAnimeList-Database-master/data/animelist.csv")
anime_synopsis = pd.read_csv("MyAnimeList-Database-master/data/anime_with_synopsis.csv")

#--------------------------------------------

#%% Manipulando a database

#Coluna Específica
print(anime_data["Score"])

#Colunas Específicas
print(anime_data[["Name", "Score"]])

#Exemplo:
cols = ["MAL_ID", "Name", "Score", "Genres", "Type", "Aired"]
anime_data_extracted = anime_data[cols]
anime_data_extracted.head()

#Linhas Específicas
anime_data_extracted[0:20]
