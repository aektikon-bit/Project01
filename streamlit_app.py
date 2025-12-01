import streamlit as st
import random

# ตั้งค่า page
st.set_page_config(page_title="🎯 เกมทายตัวเลข", page_icon="🎯", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 เกมทายตัวเลข 🎯</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ทายตัวเลขระหว่าง <b>1 ถึง 10</b>!</p>", unsafe_allow_html=True)

# สร้างตัวเลขลับและรอบ
if 'ตัวเลขลับ' not in st.session_state:
    st.session_state.ตัวเลขลับ = random.randint(1, 10)
if 'รอบ' not in st.session_state:
    st.session_state.รอบ = 1

# รับเลขจากผู้เล่น
ทาย = st.number_input("ใส่ตัวเลขของคุณ", min_value=1, max_value=10, step=1)

# ปุ่มทาย
if st.button("ทายเลย!"):
    if ทาย == st.session_state.ตัวเลขลับ:
        # แสดง emoji ใหญ่กลางหน้าจอ
        st.markdown(
            "<h1 style='text-align: center; font-size:100px;'>🎉</h1>", 
            unsafe_allow_html=True
        )
        st.success(f"ถูกต้อง! ตัวเลขคือ {st.session_state.ตัวเลขลับ} 🎯")
        st.session_state.ตัวเลขลับ = random.randint(1, 10)
        st.session_state.รอบ = 1
    else:
        st.markdown(
            "<h1 style='text-align: center; font-size:100px;'>❌</h1>", 
            unsafe_allow_html=True
        )
        st.error(f"ผิดแล้ว! ตัวเลขที่ถูกคือ {st.session_state.ตัวเลขลับ} 😅")
        st.session_state.รอบ += 1

# แสดงรอบปัจจุบัน
st.info(f"คุณอยู่ในรอบที่ {st.session_state.รอบ}")
