import streamlit as st
import random

# 웹앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라줍니다.")

# 추천할 점심 메뉴 목록 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", 
    "초밥", "라멘", "짜장면", "짬뽕", 
    "햄버거", "파스타", "쌀국수", "순대국밥", 
    "비빔밥", "샌드위치", "떡볶이", "부대찌개"
]

# 버튼 클릭 시 실행될 동작
if st.button("오늘 뭐 먹지? 🎲"):
    # 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(lunch_menus)
    
    # 결과 출력
    st.balloons() # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요 😋")
