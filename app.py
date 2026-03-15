import streamlit as st
import pickle
import requests

songs_df = pickle.load(open('songs.pkl', 'rb'))
songs_list = songs_df['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(song):
    song_index = songs_df[songs_df['title'] == song].index[0]
    distances = similarity[song_index]
    songs_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs = []
    recommended_artists = []
    for i in songs_sorted:
        recommended_songs.append(songs_df.iloc[i[0]].title)
        recommended_artists.append(songs_df.iloc[i[0]].track_artist)
    return recommended_songs, recommended_artists


st.title('🎵 Music Recommender System')

selected_song = st.selectbox('Select a song', songs_list)

if st.button('Recommend'):
    names, artists = recommend(selected_song)
    cols = st.columns(5)
    for col, name, artist in zip(cols, names, artists):
        with col:
            st.text(name)
            st.caption(artist)