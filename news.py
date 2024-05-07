url ='https://www.who.int/news-room/fact-sheets/detail/breast-cancer#:~:text=Breast%20cancer%20is%20a%20disease,producing%20lobules%20of%20the%20breast.'

import streamlit as st


def app():
    st.subheader('Ada Berita Apa nih?')
    st.markdown(f'<a href="{url}" target="_blank" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px;">Detail</a>', unsafe_allow_html=True)
