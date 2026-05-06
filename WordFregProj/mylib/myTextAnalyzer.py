import pandas as pd
from collections import Counter
from konlpy.tag import Okt

def fetch_data(file_path, target_column):
    """CSV에서 특정 열 데이터를 리스트로 반환"""
    df = pd.read_csv(file_path)
    return df[target_column].tolist()

def get_word_counts(text_list, top_n=None):
    """형태소 분석을 통한 단어 빈도 계산"""
    analyzer = Okt()
    
    # 분석에서 제외할 불용어 설정
    stop_list = ['영화', '정말', '진짜', '보고', '보는', '하고', '있다', '재밌다']
    # 추출할 품사 지정
    target_pos = ['Noun', 'Adjective', 'Verb']
    
    parsed_words = []
    for comment in text_list:
        # 단어의 원형(stem=True)을 추출하여 '하다', '있다' 등으로 통일
        for word, tag in analyzer.pos(str(comment), stem=True):
            if tag in target_pos and len(word) > 1 and word not in stop_list:
                parsed_words.append(word)
                
    return Counter(parsed_words)