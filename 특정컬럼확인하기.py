"""
[문제 설명]
한국언론진흥재단에서 제공하는 뉴스 빅데이터 메타데이터 CSV 파일을 활용하여 
'통합 분류1' 컬럼의 빈도수를 확인 분석관점 넓혀보기
. 또한, 콘솔에 시리즈 구조와 데이터를 확인할 수 있도록 출력하는 부분도 포함되어야 합니다.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv' 
df = pd.read_csv(file_path, encoding='cp949')


category_counts = df["통합 분류1"].value_counts().head(10)  

print("=== [콘솔 확인] 통합 분류1  카테고리 시리즈 ===")
print(category_counts)
print("데이터 타입:", type(category_counts))
print("====================================================\n")


available_dates = df["일자"].dropna()

first_date = available_dates.min()
last_date = available_dates.max()  # 기간 확인하기 위함.

print("=== [콘솔 확인] 데이터 분석 기간 ===")
print(f"최초 날짜 (시작일): {first_date}")
print(f"마지막 날짜 (종료일): {last_date}")
print("====================================================\n")