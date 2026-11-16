import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="오늘의 점심 추천기", page_icon="🍽️", layout="centered"
)

# 제목 및 설명
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "초밥",
    "비빔밥",
    "칼국수",
    "짜장면",
    "짬뽕",
    "햄버거",
    "파스타",
    "쌀국수",
    "순대국밥",
    "마라탕",
    "떡볶이 & 튀김",
    "샐러드 & 샌드위치",
]

# 구분선
st.divider()

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 점심 메뉴 추천받기", use_container_width=True, type="primary"):
    selected_menu = random.choice(lunch_menus)

    # 풍선 애니메이션 효과
    st.balloons()

    # 결과 출력
    st.success(f"오늘의 추천 점심 메뉴는 **[{selected_menu}]** 입니다! 맛있게 드세요 😋")
