import streamlit as st
import mylib.myTextAnalyzer as ta
import mylib.mySTVisualizer as sv

# 페이지 제목 설정
st.set_page_config(page_title="영화 리뷰 분석기", layout="wide")
st.title("다음 영화 리뷰 감성 키워드 분석")

# 파일 경로 (본인의 경로에 맞게 수정)
CSV_PATH = r"D:\Lecture\TextMining26\Apps\WordFregProj\data\daum_movie_review.csv"

# 데이터 로딩 및 분석
with st.spinner('데이터 분석 중...'):
    raw_text = ta.fetch_data(CSV_PATH, 'review')
    word_freq = ta.get_word_counts(raw_text)

# 화면 분할 (왼쪽: 막대그래프, 오른쪽: 워드클라우드)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 단어 빈도 순위")
    sv.draw_horizontal_bar(word_freq, 20)

with col2:
    st.markdown("### 리뷰 키워드 클라우드")
    sv.draw_cloud(word_freq, 60)