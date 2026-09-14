import streamlit as st

from init_db import init_database

init_database()

st.set_page_config(
    page_title="Мониторинг успеваемости",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Мониторинг посещаемости студентов")

page = st.sidebar.radio(
    "Раздел",
    [
        "Главная",
        "Студенты",
        "Дисциплины",
        "Посещаемость",
        "Практические работы",
        "Отчёты"
    ]
)

if page == "Главная":
    st.header("Главная")
    st.write(
        "Система учёта посещаемости и выполнения "
        "практических работ студентов."
    )

elif page == "Студенты":
    st.header("Студенты")

elif page == "Дисциплины":
    st.header("Дисциплины")

elif page == "Посещаемость":
    st.header("Посещаемость")

elif page == "Практические работы":
    st.header("Практические работы")

elif page == "Отчёты":
    st.header("Отчёты")