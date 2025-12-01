import streamlit as st
import random

# ตั้งค่า title และ icon
st.set_page_config(page_title="🎯 เกมทายตัวเลข", page_icon="🎯", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 เกมทายตัวเลข 🎯</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ทายตัวเลขระหว่าง <b>1 ถึง 10</b>!</p>", unsafe_allow_html=True)

# สร้างตัวเลขลับและรอบใน session_state
if 'ตัวเลขลับ' not in st.session_state:
    st.session_state.ตัวเลขลับ = random.randint(1, 10)
if 'รอบ' not in st.session_state:
    st.session_state.รอบ = 1

# ช่องกรอกตัวเลข
ทาย = st.number_input("ใส่ตัวเลขของคุณ", min_value=1, max_value=10, step=1)

# ปุ่มทาย
if st.button("ทายเลย!"):
    if ทาย == st.session_state.ตัวเลขลับ:
        st.success(f"🎉 ถูกต้อง! คุณทายถูกในรอบที่ {st.session_state.รอบ}!")
        # สุ่มเลขใหม่และรีเซ็ตรอบ
        st.session_state.ตัวเลขลับ = random.randint(1, 10)
        st.session_state.รอบ = 1
    else:
        st.warning(f"❌ ผิดแล้ว! ลองใหม่ 😅")
        st.session_state.รอบ += 1

# แสดงรอบปัจจุบัน
st.info(f"คุณอยู่ในรอบที่ {st.session_state.รอบ}")
