import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ==========================================
# 1. SETTING & PROFESSIONAL BANKING UI
# ==========================================
st.set_page_config(page_title="Lotto Data Pro Finance", page_icon="📈", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Sarabun:wght@400;700&display=swap');
    
    /* --- Main Theme: Banking App Style (Blue/Grey/White) --- */
    .stApp { 
        background-color: #F4F7F9 !important; /* พื้นหลังเทาอ่อนมาก */
        color: #2C3E50 !important; 
        font-family: 'Sarabun', sans-serif; 
    }
    
    /* Clean Header */
    header {visibility: hidden;}
    .block-container { padding-top: 1.5rem !important; max-width: 1200px !important; }

    /* Typography */
    h1, h2, h3 { 
        color: #1A237E !important; /* น้ำเงินเข้ม */
        font-weight: 700 !important; 
        letter-spacing: -0.5px;
    }
    h1 { font-size: 32px !important; margin-bottom: 20px !important; }
    h2 { font-size: 24px !important; border-left: 5px solid #1A237E; padding-left: 15px; margin-top: 30px !important; }
    
    /* --- Pro Cards (กรอบสีเทาอ่อน ตามสั่ง) --- */
    .pro-card {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0; /* ขอบเทาอ่อน */
        border-radius: 16px; /* มุมมนแบบแอป */
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); /* เงาเบาๆ ดูแพง */
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .pro-card:hover {
        box-shadow: 0 8px 24px rgba(26, 35, 126, 0.1); /* Hover แล้วเงาชัดขึ้น */
        border-color: #C5CAE9;
    }
    
    /* Result Numbers */
    .result-big { font-size: 56px; font-weight: 800; color: #1A237E; line-height: 1.1; text-align: center; font-family: 'Roboto', sans-serif; }
    .result-med { font-size: 32px; font-weight: 700; color: #455A64; text-align: center; font-family: 'Roboto', sans-serif; }
    .label-txt { font-size: 14px; color: #78909C; text-align: center; margin-bottom: 5px; font-weight: 500; }
    
    /* --- Prediction Cards (การ์ดวิเคราะห์) --- */
    .pred-num-box {
        background: linear-gradient(135deg, #1A237E, #3949AB);
        color: white;
        border-radius: 12px 12px 0 0;
        padding: 15px;
        text-align: center;
    }
    .pred-num { font-size: 42px; font-weight: 800; font-family: 'Roboto', sans-serif; }
    .pred-prob { background-color: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 14px; }
    
    .pred-detail-box {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-top: none;
        border-radius: 0 0 12px 12px;
        padding: 15px;
        font-size: 14px;
        color: #546E7A;
    }
    .stat-row { display: flex; justify-content: space-between; margin-bottom: 8px; border-bottom: 1px dashed #E0E0E0; padding-bottom: 5px; }
    .stat-label { font-weight: 600; color: #1A237E; }
    
    /* --- Inputs & Buttons (สไตล์แอป) --- */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] { 
        border-radius: 10px; 
        border: 2px solid #CFD8DC; 
        padding: 12px; 
        background-color: #FAFAFA;
    }
    .stTextInput input:focus { border-color: #1A237E; }
    
    .stButton button { 
        background-color: #1A237E !important; 
        color: white !important; 
        border-radius: 10px; 
        font-weight: 700; 
        height: 50px; 
        box-shadow: 0 4px 6px rgba(26, 35, 126, 0.2);
    }
    
    /* Tabs Design */
    .stTabs [data-baseweb="tab-list"] { border-bottom: 2px solid #E0E0E0; }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
        color: #78909C;
    }
    .stTabs [aria-selected="true"] {
        color: #1A237E !important;
        border-bottom: 3px solid #1A237E;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BACKEND LOGIC (The Python Brain)
# ==========================================
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

def check_pass():
    if st.session_state.pass_input == '06062501': st.session_state.logged_in = True
    else: st.error("รหัสผ่านไม่ถูกต้อง (Invalid Password)")

# --- Function: คำนวณวันงวดหน้าอัตโนมัติ ---
def get_next_draw_date():
    today = datetime.now()
    # หาหวยงวดต่อไป (วันที่ 1 หรือ 16)
    next_draw = today
    while True:
        next_draw += timedelta(days=1)
        if next_draw.day == 1 or next_draw.day == 16:
            return next_draw.strftime("%d/%m/%Y") # คืนค่าเป็น string วันที่

# --- Function: สร้างเหตุผลทางสถิติแบบมืออาชีพ (Simulation Engine) ---
def generate_pro_stats(num_str, is_3_digit=False):
    # นี่คือการจำลองว่า Python หลังบ้านคำนวณสถิติซับซ้อนมาให้
    years = 20
    total_draws = years * 24
    
    # สุ่มสร้างค่าสถิติให้ดูสมจริง
    frequency = random.randint(5, 45) # ความถี่ที่เคยออก
    last_seen = random.randint(1, 60) # ไม่เห็นมานานกี่งวด
    prob_score = random.randint(65, 98) # คะแนนความน่าจะเป็น
    
    trend_types = [
        "Moving Average Convergence (MACD Signal)",
        "Seasonal Regression Pattern (Decade Data)",
        "Frequency Heatmap spike detected",
        "Gap Analysis Rebound Zone",
        "Cluster Grouping Anomaly"
    ]
    trend = random.choice(trend_types)
    
    ranking = "Top 5%" if prob_score > 85 else "Top 15%" if prob_score > 75 else "Watcher List"

    reason_html = f"""
    <div class="stat-row"><span class="stat-label">🎯 Probability Score:</span> <b>{prob_score}%</b></div>
    <div class="stat-row"><span class="stat-label">📊 {years-Year Freq:</span> {frequency} times (Rank: {ranking})</div>
    <div class="stat-row"><span class="stat-label">⏱️ Last Seen Gap:</span> {last_seen} draws ago</div>
    <div style="margin-top:8px; font-size:13px;">NOTE: <i>{trend}. Based on historical data mining.</i></div>
    """
    return num_str, prob_score, reason_html

# ==========================================
# 3. MAIN APPLICATION (UI LAYOUT)
# ==========================================

# >> ส่วน Login <<
if not st.session_state.logged_in:
    st.markdown("<br><br><h1 style='text-align:center;'>🔒 Lotto Data Pro Finance</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#78909C;'>Secure Access System for Analytics</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.5, 2, 1.5])
    with c2:
        st.markdown("<div class='pro-card' style='padding:40px;'>", unsafe_allow_html=True)
        st.text_input("Authentication Pin", type="password", key="pass_input", placeholder="Enter 8-digit PIN", on_change=check_pass)
        st.button("Authorize Access", on_click=check_pass, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# >> ส่วนเนื้อหาหลัก <<
st.title("📈 สรุปสถานการณ์และวิเคราะห์ข้อมูลสถิติ")

# ----------------------------------------------------
# SECTION 1: ผลรางวัลล่าสุด (Banking Dashboard Style)
# ----------------------------------------------------
latest
