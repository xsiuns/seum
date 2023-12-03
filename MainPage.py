import streamlit as st
import pandas as pd
import numpy as np

# from selenium import webdriver


# driver = webdriver.Chrome(executable_path=r'd:\\chromedriver.exe')



st.title('My first app Title🍑')

#Image

st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=30)
st.image('./auto_report_image.png', width=500)
st.header('큰제목 입력!')
st.subheader('작은제목 입력!')
st.caption('*** 캡션 입력! Code Test ***')

sp_code = '''
def hello():
    print('Hello, Streamlit!')
'''
st.code(sp_code, language='python')

#input text
user_input = st.text_input('사용자의 입력을 받는다', '기본값')
st.write('사용자의 입력값은', user_input, '입니다.')

st.text('텍스트 입력!')

#matirx(3,3,5)
st.write('3행 3열의 랜덤 행렬')
st.write(np.random.randn(3,3))



st.markdown(' **마크다운 입력!** ')
st.markdown(':blue[$\sqrt{a^2 + b^2 = c^2}$] 와같이 수식도 입력 가능!')

st.latex(r'\sqrt{a^2 + b^2 = c^2}')


df = pd.DataFrame({
    '1열': [1, 2, 3, 4],
    '2열': [10, 20, 30, 40]
})


st.caption('*** 캡션 입력! DataFrame Test ***')
st.dataframe(df, use_container_width=True)