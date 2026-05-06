import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

# 한글 폰트 초기 설정 함수
def set_korean_font():
    path = "c:/Windows/Fonts/malgun.ttf"
    font = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font)

def draw_horizontal_bar(counter, limit=15):
    """빈도수 상위 단어 막대 그래프 출력"""
    set_korean_font()
    
    data = counter.most_common(limit)
    labels = [item[0] for item in data]
    values = [item[1] for item in data]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    # 그래프 색상을 'skyblue'로 변경
    ax.barh(labels[::-1], values[::-1], color='skyblue')
    ax.set_title(f"TOP {limit} 빈도 단어")
    st.pyplot(fig)

def draw_cloud(counter, max_cnt=100):
    """워드클라우드 생성 및 출력"""
    # 배경색을 'white'로, 폰트 경로를 명시적으로 전달
    cloud_gen = WordCloud(
        font_path='c:/Windows/Fonts/malgun.ttf',
        background_color='white',
        width=1000, height=700,
        max_words=max_cnt
    ).generate_from_frequencies(counter)
    
    fig, ax = plt.subplots()
    ax.imshow(cloud_gen, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)