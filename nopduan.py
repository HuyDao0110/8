import streamlit as st

with st.sidebar:
	image = 'pmc.jpg'
	st.image(image, caption='Phương Mỹ Chi')
	st.write('Ca sĩ: Phương Mỹ Chi')
	st.write('Cô là một nữ ca sĩ, nhạc sĩ kiêm diễn viên người Việt Nam. Khởi đầu sự nghiệp từ năm 2013, cô bắt đầu nổi danh từ khi tham gia và đạt giải á quân của mùa đầu tiên trong chương trình Giọng hát Việt nhí. Năm 2023, sau khi thành công với các bài hát dân ca Nam Bộ Việt Nam, Chi cho ra mắt album phòng thu thứ tư và cũng là album nhạc pop đầu tiên trong sự nghiệp, Vũ trụ cò bay, bao gồm các bài hát do chính cô sáng tác. Album đã đạt được thành công lớn về mặt thương mại, được công chúng và các nhà phê bình âm nhạc đánh giá cao.')

st.title('Bài hát yêu thích')
st.write('Vũ trụ có anh')
audio = open('vtca.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.title('MV yêu thích')
st.write('Bóng phù hoa')
video = 'https://www.youtube.com/watch?v=BmrdGQ0LRRo'
st.video(video, format='video/mp4')

