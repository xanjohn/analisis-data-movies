import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import seaborn as sns


df = pd.read_excel("movies_fix.xlsx")
#print("5 film dengan popularitas teratas")
st.title("""Informasi FILM""")
st.write("""
List Film
""")
st.dataframe(df)

st.write("""## 5 Film Dengan Penonton Terbanyak""")
data_populer = df.groupby('original_title')['popularity'].mean().reset_index()
data_populer.sort_values("popularity")
df_populer = data_populer.nlargest(n=5, columns="popularity")
st.dataframe(df_populer)

tombol1 = st.button("Lihat Grafik Penonton")
if tombol1:
    st.bar_chart(df_populer, x="original_title",y="popularity")
    st.balloons()

st.write("""## 5 Film Dengan Pendapatan Tertinggi """)
df_pendapatan = df.groupby('title')['revenue'].mean().reset_index()
df_pendapatan.sort_values("revenue")
pendapatan_show = df_pendapatan.nlargest(n=5, columns="revenue")
st.dataframe(pendapatan_show)

tombol2 = st.button("Lihat Grafik Pendapatan")
if tombol2:
    st.bar_chart(pendapatan_show, x="title", y="revenue")
    st.balloons()


st.write("""## Pengaruh Budget Terhadap Kesuksesan Film""")
st.write("""*Terhadap Kepopuleran*""")
moviesbybudget=df[['popularity','budget']].sort_values(by="popularity",ascending=False)
moviesbybudget=moviesbybudget.drop_duplicates(subset = "popularity")
moviesbybudget=moviesbybudget.drop_duplicates(subset = "budget")
moviesbybudget=moviesbybudget.head(50)
st.dataframe(moviesbybudget)
tombol3 = st.button("Lihat Grafik")
if tombol3:
    st.bar_chart(moviesbybudget,x="popularity",y="budget")
    st.balloons()

st.write("""*Terhadap Pendapatan Terbanyak*""")
moviesbybudget=df[['budget', 'revenue']].sort_values(by="revenue",ascending=False)
moviesbybudget=moviesbybudget.drop_duplicates(subset = "revenue")
moviesbybudget=moviesbybudget.drop_duplicates(subset = "budget")
moviesbybudget=moviesbybudget.head(50)
st.dataframe(moviesbybudget)
tombol4 = st.button("Lihat Grafik!")
if tombol4:
    st.bar_chart(moviesbybudget,x="revenue",y="budget")
    st.balloons()

st.write("""## Tempat Syuting Film-Film""")
df_movie = pd.read_excel('movies_fix.xlsx')
df_movie_filter = df_movie[['title','LATITUDE', 'LONGITUDE']]
df_lokasi = df_movie[["title","production_countries"]]
df_sample = df_movie_filter.sample(n=50)
st.dataframe(df_lokasi)
st.write("""## Peta Persebaran Lokasi Syuting Film """)
map = folium.Map(location=[df_sample.LATITUDE.mean(), 
                           df_sample.LONGITUDE.mean()], 
                           zoom_start=1, control_scale=True)
for index, location_info in df_sample.iterrows():
    folium.Marker([location_info["LATITUDE"], location_info["LONGITUDE"]], popup=location_info["title"]).add_to(map)


tombol3 = st.button("Lihat Peta")

if tombol3 :
    st_data = st_folium(map)
    st.balloons()
