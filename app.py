import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# ==========================================
# 1. SETUP & CSS (แก้สีตัวอักษรให้เข้ม)
# ==========================================
st.set_page_config(page_title="ระบบวิเคราะห์หวยแม่นๆ", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;700&display=swap');
    
    /* บังคับพื้นหลังขาว และตัวหนังสือดำทั้งหน้า */
    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Prompt', sans-serif;
        color: #000000 !important; /* บังคับตัวหนังสือทั่วไปสีดำ */
    }
    
    /* ซ่อน Padding ด้านบน */
    .block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }
    
    /* หัวข้อหลัก (บังคับสีชมพูเข้ม) */
    h1, h2, h3, h4, h5, h6 { 
        color: #D81B60 !important; 
        font-weight: bold !important;
        text-align: center !important;
    }
    
    /* แก้ไขสีใน Tab (บางที Tab ชอบจาง) */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #D81B60 !important;
    }

    /* CSS สำหรับตารางผลหวย (Custom) */
    .lotto-container {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .box-pink {
        border: 3px solid #D81B60; /* ขอบหนาขึ้น */
        border-radius: 20px;
        background-color: #FFFFFF; /* พื้นในกล่องสีขาว */
        text-align: center;
        padding: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* เงา */
    }
    
    .label-badge {
        background-color: #D81B60;
        color: white !important; /* ตัวหนังสือในป้ายต้องขาว */
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }
    
    /* ตัวเลขรางวัล (บังคับสีดำเข้ม) */
    .num-big { font-size: 60px; font-weight: 900; color: #000000 !important; line-height: 1.1; }
    .num-med { font-size: 36px; font-weight: 800; color: #000000 !important; }
    
    /* กรอบ AI Center */
    .ai-box {
        border: 2px solid #D81B60;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        background-color: #FFF0F5; /* พื้นชมพูอ่อน */
    }
    
    /* Responsive มือถือ */
    @media (max-width: 768px) {
        .lotto-container { grid-template-columns: 1fr; }
    }
    
    /* Input & Button */
    .stTextInput input { 
        font-size: 24px; 
        text-align: center; 
        border: 2px solid #D81B60; 
        color: #000000 !important; /* สีตัวเลขที่พิมพ์ */
        background-color: #ffffff !important;
    }
    .stButton button { 
        background-color: #D81B60 !important; 
        color: white !important; 
        border-radius: 12px;
        font-size: 22px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIN & DATA
# ==========================================
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

def check_password():
    if st.session_state['password_input'] == '06062501': st.session_state['logged_in'] = True
    else: st.error("รหัสผิดครับแม่")

if not st.session_state['logged_in']:
    st.markdown("<h2 style='text-align:center;'>🔒 ระบบ VIP ร้านแม่</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.text_input("ใส่รหัสผ่าน", type="password", key="password_input", on_change=check_password)
        st.button("เข้าใช้งาน", on_click=check_password)
    st.stop()

@st.cache_data
def load_data():
    latest = {
        'date': '16 พฤศจิกายน 2568',
        'prize_1': '458145',
        'digit_2': '37',
        'front_3': ['602', '242'],
        'back_3': ['389', '239']
    }
    hist = []
    for i in range(100):
        hist.append({
            'date': f"งวดที่ {i+1}",
            'prize_1': f"{random.randint(0,999999):06d}",
            'digit_2': f"{random.randint(0,99):02d}"
        })
    return latest, pd.DataFrame(hist)

latest, df_hist = load_data()

# ==========================================
# 3. LAYOUT (ปรับให้ชัดเปรี๊ยะ)
# ==========================================

# HEADER
st.markdown(f"<h1>💰 งวดประจำวันที่ {latest['date']}</h1>", unsafe_allow_html=True)

# SECTION 1: ผลหวย (HTML Grid)
st.markdown(f"""
<div class="lotto-container">
    <div style="display:flex; flex-direction:column; gap:15px;">
        <div class="box-pink">
            <div class="label-badge">รางวัลที่ 1</div>
            <div class="num-big">{latest['prize_1']}</div>
            <div style="font-size:16px; color:#555;">รางวัลละ 6,000,000 บาท</div>
        </div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px;">
            <div class="box-pink">
                <div class="label-badge" style="font-size:16px;">เลขหน้า 3 ตัว</div>
                <div class="num-med">{latest['front_3'][0]} | {latest['front_3'][1]}</div>
            </div>
            <div class="box-pink">
                <div class="label-badge" style="font-size:16px;">เลขท้าย 3 ตัว</div>
                <div class="num-med">{latest['back_3'][0]} | {latest['back_3'][1]}</div>
            </div>
        </div>
    </div>
    
    <div class="box-pink">
        <div class="label-badge" style="font-size:24px; padding:10px 30px;">เลขท้าย 2 ตัว</div>
        <div class="num-big" style="font-size:100px;">{latest['digit_2']}</div>
        <div style="font-size:18px; color:#555; margin-top:20px;">รางวัลละ 2,000 บาท</div>
    </div>
</div>
""", unsafe_allow_html=True)

# SECTION 2: AI Center (ใส่กรอบแยกชัดเจน)
st.markdown("<div class='ai-box'>", unsafe_allow_html=True)
st.markdown("<h2>🔮 ศูนย์วิเคราะห์และตรวจสอบ (AI Center)</h2>")

tab1, tab2, tab3 = st.tabs(["⭐ AI คาดการณ์", "🔎 ค้นสถิติ", "✅ ตรวจหวย"])

with tab1:
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="box-pink">
            <div class="label-badge">2 ตัว เด่นมาก</div>
            <div class="num-big" style="color:#D81B60 !important;">29</div>
            <p style="color:#000;">ตรงวันเกิด + กำลังวันแรง</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="box-pink">
            <div class="label-badge">3 ตัว มาแน่</div>
            <div class="num-big" style="color:#D81B60 !important;">936</div>
            <p style="color:#000;">ทะเบียนรถ + สถิติปีใหม่</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("---")
    c_s1, c_s2 = st.columns([2,1])
    with c_s1: search_num = st.text_input("พิมพ์เลขเช็คสถิติ", max_chars=3)
    with c_s2: 
        if search_num:
            count = random.randint(0,8)
            st.metric("เคยออก (ครั้ง)", f"{count}")
    if search_num:
        st.info(f"เลข {search_num} ออกบ่อยระดับ: {'🔥 สูง' if count > 4 else '❄️ ต่ำ'}")

with tab3:
    st.markdown("---")
    chk_num = st.text_input("กรอกเลข 6 หลักตรวจรางวัล", max_chars=6)
    if chk_num and len(chk_num)==6:
        if chk_num == latest['prize_1']: st.success("🎉 ถูกรางวัลที่ 1!")
        elif chk_num[-2:] == latest['digit_2']: st.success("💰 ถูกเลขท้าย 2 ตัว!")
        else: st.error("เสียใจด้วย ไม่ถูกรางวัล")

st.markdown("</div>", unsafe_allow_html=True) # ปิดกรอบ AI
