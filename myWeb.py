import streamlit as st
st.set_page_config(
    page_title='구암고 2학년 선택과목조사',
    page_icon='🔞'
)
st.header('**20721 안현준**')
st.header('TEST')
number = st.number_input('반을 입력하세요',step=1,min_value=1,max_value=9)
number2 = st.number_input('번호를 입력하세요',step=1,min_value=1,max_value=30)
title = st.text_input('이름을 작성하세요')
st. subheader('수학1,확률과통계,문학,독서는 **공동교육과정**입니다')

과목 = st.radio("당신은 :blue[**이과**]인가요, :green[**문과**]인가요?",('이과','문과'))

if 과목 == '이과':
    options = st.selectbox('1학기 수학선택과목을 선택하세요.',('수학2','미적분'))
    st.write(':red[2학기에는 **선택하지 않은** 과목을 수강하게 됩니다.]')

    science = st.multiselect('과학탐구과목을 선택하세요.(3개선택)',['물리','화학','생명','지구과학'],max_selections=3)

    외국어 = st.selectbox('제2외국어과목을 선택하세요', ('중국어', '일본어'))

    if st.button('제출'):
        if 과목:
            if science:
                st.image('what.jpg')

            else:
                st.write(':red[과학탐구과목 선택하세요!]')

else:
    문과 = st.selectbox('1학기 국어선택과목을 선택하세요.',('화법과작문','언어와매체'))
    st.write(':red[2학기에는 **선택하지 않은** 과목을 수강하게 됩니다.]')

    social = st.multiselect('사회탐구과목을 선택하세요.(3개선택)',['한국지리','세계지리','세계사','동아시아사','경제',
                                              '정치와법','생활과윤리','윤리와사상'],max_selections=3)
    외쿡어 = st.selectbox('제2외국어과목을 선택하세요', ('중국어', '일본어'))

    if st.button('제출'):
        if social:
            st.image('what.jpg')

        else:
            st.write(':red[사회탐구과목 선택하세요!]')





      


