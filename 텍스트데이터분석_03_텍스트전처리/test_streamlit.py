import streamlit as st
st.set_page_config(layout="wide") # 화면을 넓게 쓰도록 설정

st.title("Hello, Streamlit World")

name = "Kwangmin"
st.title(f"Hello, {name}~~~~ Welcome to Streamlit World!!!")

import pandas as pd
df = pd.DataFrame({
    'A': [1,2,3,4],
    'B': [10,20,30,40]
})

import time 

text = st.title('텍스트가 변할 겁니다.')
time.sleep(2)
text.info('2초가 지났습니다.')


st.header("사용자 입력 폼")

with st.form('my_form'):
    
    name = st.text_input("이름")
    
    age = st.number_input("나이",min_value=1, step=1)
    
    agree = st.checkbox("약관에 동의합니다")
    
    submitted = st.form_submit_button("제출")


if submitted:
    if agree:
        st.write(f"이름: {name}, 나이: {age}")
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관에 동의해야 제출이 가능합니다.")
        
with st.sidebar:
    st.header("설정")
    
    user_name = st.text_input("이름을 입력하세요")
    
    user_age = st.slider("나이", min_value=0, max_value=120, value=25)

    color = st.selectbox(
        "좋아하는 색상을 선택하세요",
        ("빨강", "초록", "파랑", "노랑")
    )
    
def change_text():
    text = st.title('텍스트가 변할 겁니다.')
    time.sleep(3)
    text = text.info('3초가 지났습니다.')
    
change_text()

# matplotlib 사용해보기 

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

font_path = "c:/Windows/Fonts/malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

st.title("데이터 시각화 실습")
st.subheader("1. 막대 그래프")

# 이름과 점수 데이터를 변경했습니다.
x = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'] 
y = [85, 78, 92, 65, 88] 

fig1, ax1 = plt.subplots()
# 색상을 'lightgreen'으로 추가하여 동기분 코드(기본 파란색)와 차별을 두었습니다.
ax1.barh(x[::-1], y[::-1], color='lightgreen') 
plt.title('파이썬 과제 점수')
plt.xlabel('점수')
plt.ylabel('이름')

st.pyplot(fig1)

st.divider() # 중간에 구분선을 하나 넣었습니다.

# wordcloud 사용해보기 

st.subheader('2. 워드클라우드')

# 텍스트 내용을 살짝 변경했습니다.
text = "파이썬 데이터분석 인공지능 머신러닝 딥러닝 스트림릿 파이썬 시각화 빅데이터 인공지능 스트림릿 머신러닝"

wc = WordCloud(
    font_path=font_path,
    background_color="aliceblue", # 배경색을 ivory에서 아주 연한 파란색(aliceblue)으로 변경
    width=800,
    height=400
).generate(text)

fig2, ax2 = plt.subplots()
ax2.imshow(wc)
ax2.axis('off')

st.pyplot(fig2)






