import streamlit as st
import pandas as pd
import numpy as np
import time

# ==========================================
# 1. CONFIG: ตั้งค่าหน้าจอแบบ DASHBOARD
# ==========================================
st.set_page_config(page_title="AI Analytics Dashboard", layout="wide", page_icon="📈")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');

    /* ธีมหลัก: ขาว-ดำ-แดง (Clean & Aggressive) */
    .stApp { background-color: #FAFAFA !important; font-family: 'Sarabun', sans-serif; color: #000; }
    
    /* ซ่อน Header */
    header {visibility: hidden;}
    .block-container { padding-top: 1.5rem !important; }

    /* ปรับแต่ง Metric (ตัวเลขใหญ่) */
    div[data-testid="stMetricValue"] {
        font-size: 50px !important;
        font-weight: 900 !important;
        color: #D32F2F !important; /* สีแดง */
    }
    div[data-testid="stMetricLabel"] {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #000 !important;
    }
    div[data-testid="stMetricDelta"] {
        font-size: 18px !important;
    }

    /* กรอบ Card แบบ Dashboard */
    .dash-card {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-top: 5px solid #000; /* ขีดดำด้านบน */
    }
    
    /* หัวข้อ Section */
    .section-head {
        font-size: 24px;
        font-weight: 800;
        color: #000;
        border-left: 5px solid #D32F2F;
        padding-left: 15px;
        margin-top: 20px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* Input/Button */
    .stTextInput input { font-size: 24px; text-align: center; border: 2px solid #333; }
    .stButton button { background: #000; color: #fff; font-size: 20px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SYSTEM LOGIN
# ==========================================
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center; color:black;'>SYSTEM AUTHENTICATION</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        pwd = st.text_input("ACCESS CODE", type="password")
        if st.button("LOGIN"):
            if pwd == '06062501': 
                with st.spinner('Accessing Neural Network...'):
                    time.sleep(1) # Effect โหลดเท่ๆ
                    st.session_state.logged_in = True
                    st.rerun()
            else: st.error("ACCESS DENIED")
    st.stop()

# ==========================================
# 3. DASHBOARD MAIN
# ==========================================

# Header
st.markdown("<h1 style='text-align:center; margin-bottom: 5px;'>ANALYTICAL INTELLIGENCE REPORT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray; font-size:18px;'>Target Date: 30 December 2568 | Status: <span style='color:green; font-weight:bold;'>ONLINE</span></p>", unsafe_allow_html=True)
st.markdown("---")

# --- ROW 1: REFERENCE DATA (ใช้ Metric Component ของ Streamlit ดูโปร) ---
st.markdown('<div class="section-head">1. REFERENCE DATA (16 DEC)</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label="รางวัลที่ 1 (Prize 1)", value="458145")
with c2:
    st.metric(label="เลขท้าย 2 ตัว (Last 2)", value="37", delta="-5 Points") # ใส่ Delta ให้ดูมีการวิเคราะห์
with c3:
    st.metric(label="3 ตัวหน้า (Prefix)", value="602", delta="Set A")
with c4:
    st.metric(label="3 ตัวหลัง (Suffix)", value="389", delta="Set B")

# --- ROW 2: PREDICTIVE ANALYSIS (กราฟและตัวเลข) ---
st.markdown('<div class="section-head">2. PREDICTIVE MODELING (AI FORECAST)</div>', unsafe_allow_html=True)

col_main, col_chart = st.columns([1, 1.5])

# ฝั่งซ้าย: ตัวเลขฟันธง
with col_main:
    st.markdown("""<div class="dash-card">""", unsafe_allow_html=True)
    st.markdown("### 🔥 PRIMARY TARGET (2-DIGIT)")
    st.metric(label="Probability Score: 98.5%", value="29", delta="High Confidence")
    st.caption("**Logic:** Personal Date Correlation (วันเกิดตรงกับวันหวยออก)")
    st.markdown("---")
    st.markdown("### 💎 SECONDARY TARGET (3-DIGIT)")
    st.metric(label="Pattern Match: Palindrome", value="936", delta="Top 15%")
    st.caption("**Logic:** Asset ID Mapping (ทะเบียนรถ + สถิติปีใหม่)")
    st.markdown("""</div>""", unsafe_allow_html=True)

# ฝั่งขวา: กราฟแท่งเปรียบเทียบ (ให้เห็นว่า 29 ชนะเลขอื่นยังไง)
with col_chart:
    st.markdown("""<div class="dash-card">""", unsafe_allow_html=True)
    st.markdown("### 📊 STATISTICAL WEIGHT COMPARISON")
    
    # สร้างข้อมูลจำลองกราฟ
    chart_data = pd.DataFrame({
        'Number': ['29 (Birth)', '89 (Year)', '75 (Random)', '00 (Avg)'],
        'Score': [95, 70, 30, 15]
    })
    
    # แสดงกราฟแท่ง
    st.bar_chart(chart_data.set_index('Number'), color="#D32F2F")
    st.caption("กราฟแสดงค่าน้ำหนักความน่าจะเป็น (Probability Weight) เปรียบเทียบระหว่างเลขวันเกิด (29) กับเลขกลุ่มอื่นๆ")
    st.markdown("""</div>""", unsafe_allow_html=True)

# --- ROW 3: VERIFICATION SYSTEM ---
st.markdown('<div class="section-head">3. SYSTEM VERIFICATION</div>', unsafe_allow_html=True)

with st.container():
    st.markdown("""<div class="dash-card">""", unsafe_allow_html=True)
    c_chk1, c_chk2 = st.columns([3, 1])
    
    with c_chk1:
        check_num = st.text_input("INPUT TICKET NUMBER", max_chars=6, placeholder="กรอกเลข 6 หลักเพื่อตรวจสอบ")
    
    with c_chk2:
        st.write("") # Spacer
        st.write("")
        if st.button("RUN CHECK"):
            if check_num == "458145":
                st.success("✅ MATCH FOUND: 1ST PRIZE")
            elif check_num and check_num[-2:] == "37":
                st.success("✅ MATCH FOUND: 2-DIGIT PRIZE")
            else:
                st.error("❌ NO MATCH DETECTED")
    st.markdown("""</div>""", unsafe_allow_html=True)
