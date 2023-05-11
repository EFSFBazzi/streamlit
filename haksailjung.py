import streamlit as st
import requests
import xmltodict
import pandas as pd
import streamlit.components.v1 as components
st.set_page_config(
    page_title='구암고 1학기 학사일정',
    page_icon='🏫',
    layout='wide'
)

신청주소 = 'https://open.neis.go.kr/hub/SchoolSchedule?'
문서타입 = 'Type=&'
인증키 = 'KEY=271fb6e0fdf64a0fb32461b729d2c990&'
페이지수 = 'pIndex=1&'
페이지당신청수 = 'pSize=100&'
시도교육청코드 = 'ATPT_OFCDC_SC_CODE=D10&'
표준학교코드='SD_SCHUL_CODE=7240056&'
학사시작일자 = 'AA_FROM_YMD=20230301&'
학사종료일자 = 'AA_TO_YMD=20230809&'

URL = 신청주소+문서타입+인증키+페이지수+페이지당신청수+시도교육청코드+표준학교코드+학사시작일자+학사종료일자

response = requests.get(URL)
response = response.content

xmlObject = xmltodict.parse(response)
dict_data = xmlObject['SchoolSchedule']['row']
df = pd.DataFrame(dict_data)


df = df[['AA_YMD','EVENT_NM','TW_GRADE_EVENT_YN']]
df = df[df['TW_GRADE_EVENT_YN']=='Y']

st.write(df[['AA_YMD','EVENT_NM']])


components.html('''
<div class="table-responsive">
  <table class="table align-middle">
    <thead>
      <tr>
        ...
      </tr>
    </thead>
    <tbody>
      <tr>
        ...
      </tr>
      <tr class="align-bottom">
        ...
      </tr>
      <tr>
        <td>...</td>
        <td>...</td>
        <td class="align-top">This cell is aligned to the top.</td>
        <td>...</td>
      </tr>
    </tbody>
  </table>
</div>
''')


