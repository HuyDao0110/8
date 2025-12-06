import streamlit as st
from PIL import Image

with st.sidebar:
    st.image("pmc/pmc.jpg", caption="Phương Mỹ Chi")
    st.write("Ca sĩ: Phương Mỹ Chi")
    st.write("Cô là một nữ ca sĩ, nhạc sĩ kiêm diễn viên người Việt Nam...")

st.title("Bài hát yêu thích")
st.write("Vũ trụ có anh")
with open("vtca/vtca.mp3", "rb") as audio_file:
    st.audio(audio_file.read(), format="audio/mp3")

st.title("MV yêu thích")
st.write("Bóng phù hoa")
st.video("https://www.youtube.com/watch?v=BmrdGQ0LRRo")
