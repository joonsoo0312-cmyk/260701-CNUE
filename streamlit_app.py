import streamlit as st

st.set_page_config(page_title="자기소개 페이지", page_icon="👋", layout="centered")

st.title("👋 안녕하세요!")
st.subheader("나의 간단한 자기소개 페이지")

st.write("여기에 나의 소개를 작성할 수 있는 페이지 템플릿입니다. 아래 내용을 자유롭게 수정하세요.")

with st.expander("📌 기본 정보"):
    st.write("- 이름: 강준수")
    st.write("- 직업/역할: 학생")
    st.write("- 지역: 대한민국")

with st.expander("✨ 소개글"):
    st.write(
        "저는 노래 듣는 것을 좋아하는 사람입니다.\n"
        "저는 음악교육학과입니다."
    )

with st.expander("🛠️ 주요 기술"):
    st.write("- 성악")
    st.write("- Streamlit")
    st.write("- 데이터 분석 / 시각화")

with st.expander("📫 연락처"):
    st.write("- 이메일: joonsoo0312@gmail.com")
    st.write("- 깃허브: github.com/joonsoo0312-cmyk")

st.markdown("---")
st.write("원하는 내용으로 자유롭게 수정하고, 더 많은 섹션을 추가해보세요.")
