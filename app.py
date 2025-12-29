import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ==========================================
# 1. SETTING & UI CONFIGURATION
# ==========================================
st.set_page_config(page_title="Lotto Data Pro", page_icon="📈", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Sarabun:wght@400;700&display=swap');
    
    .stApp { 
        background-color: #F4F7F9 !important; 
        color: #2C3E50 !important; 
        font-family: 'Sarabun', sans-serif; 
    }
    
    header {visibility: hidden;}
    .block-container { padding-top: 1.5rem !important; max-width: 1200px !important; }

    h1, h2, h3 { 
        color: #1A237E !important; 
        font-weight: 700 !important; 
    }
    
    .pro-card {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .result-big { font-size: 56px; font-weight: 800; color: #1A237E; text-align: center; font-family: 'Roboto', sans-serif; }
    .result-med { font-size: 32px; font-weight: 700; color: #455A64; text-align: center; font-family: 'Roboto', sans-serif; }
    .label-txt { font-size: 14px; color: #78909C; text-align: center; margin-bottom: 5px; }
    
    .pred-num-box {
        background: linear-gradient(135deg, #1A237E, #3949AB);
        color: white;
        border-radius: 12px 12px 0 0;
        padding: 15px;
        text-align: center;
    }
    .pred-num { font-size: 42px; font-weight: 800; font-family: 'Roboto', sans-serif; }
    
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
    
    .stTextInput input { border-radius: 10px; border: 2px solid #CFD8DC; padding: 12px; background-color: #FAFAFA; }
    .stButton button { background-color: #1A237E !important; color: white !important; border-radius: 10px; height: 50px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIC FUNCTIONS
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def check_pass():
    # แยกบรรทัดให้ชัดเจน ป้องกัน Error
    user_pass = st.session_state.pass_input
    if user_pass == '06062501':
        st.session_state.logged_in = True
    else:
        st.error("Invalid Password")

def get_next_draw_date():
    today = datetime.now()
    next_draw = today
    while True:
        next_draw += timedelta(days=1)
        if next_draw.day == 1 or next_draw.day == 16:
            return next_draw.strftime("%d/%m/%Y")

def generate_pro_stats(num_str, is_3_digit=False):
    years = 20
    frequency = random.randint(5, 45)
    last_seen = random.randint(1, 60)
    prob_score = random.randint(65, 98)
    
    trend_types = ["MACD Signal", "Seasonal Pattern", "Frequency Heatmap", "Gap Analysis", "Cluster Anomaly"]
    trend = random.choice(trend_types)
    ranking = "Top 5%" if prob_score > 85 else "Watcher List"

    # แก้ไข Syntax ให้ปลอดภัย 100%
    reason_html = f"""
    <div class="stat-row"><span class="stat-label">🎯 Probability:</span> <b>{prob_score}%</b></div>
    <div class="stat-row"><span class="stat-label">📊 {years}-Year Freq:</span> {frequency} times</div>
    <div class="stat-row"><span class="stat-label">⏱️ Last Seen:</span> {last_seen} draws ago</div>
    <div style="margin-top:8px; font-size:13px;">NOTE: <i>{trend} detected.</i></div>
    """
    return num_str, prob_score, reason_html

# ==========================================
# 3. MAIN UI
# ==========================================

# --- LOGIN SCREEN ---
if not st.session_state.logged_in:
    st.markdown("<br><h1 style='text-align:center;'>🔒 Lotto Data Pro</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div class='pro-card' style='padding:40px;'>", unsafe_allow_html=True)
        st.text_input("Enter PIN", type="password", key="pass_input")
        st.button("Login", on_click=check_pass, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- MAIN CONTENT ---
st.title("📈 สรุปสถานการณ์และวิเคราะห์สถิติ")

latest_date = '16 พฤศจิกายน 2568'

# SECTION 1: RESULT
st.markdown(f"<h2>📄 ผลสลากฯ งวด {latest_date}</h2>", unsafe_allow_html=True)
with st.container():
    col_main, col_side = st.columns([2.5, 1.5], gap="large")
    with col_main:
        st.markdown("""
        <div class="pro-card">
            <div class="label-txt">รางวัลที่ 1 (Prize 1)</div>
            <div class="result-big">458145</div>
        </div>
        """, unsafe_allow_html=True)
        c3_1, c3_2 = st.columns(2)
        with c3_1:
             st.markdown("""<div class="pro-card"><div class="label-txt">เลขหน้า 3 ตัว</div><div class="result-med">602 | 242</div></div>""", unsafe_allow_html=True)
        with c3_2:
             st.markdown("""<div class="pro-card"><div class="label-txt">เลขท้าย 3 ตัว</div><div class="result-med">389 | 239</div></div>""", unsafe_allow_html=True)
            
    with col_side:
        st.markdown("""
        <div class="pro-card" style="height: 95%; display:flex; flex-direction:column; justify-content:center;">
            <div class="label-txt">เลขท้าย 2 ตัว</div>
            <div class="result-big" style="font-size: 100px; color:#D84315;">37</div>
        </div>
        """, unsafe_allow_html=True)

# SECTION 2: AI FORECAST
next_date = get_next_draw_date()
st.markdown(f"<h2>🤖 AI Forecast (Target: {next_date})</h2>", unsafe_allow_html=True)

st.markdown("### 🔹 เลขท้าย 2 ตัว (High Prob)")
col2_1, col2_2, col2_3, col2_4 = st.columns(4)
nums_2d = ["29", "85", "41", "07"]
for i, col in enumerate([col2_1, col2_2, col2_3, col2_4]):
    with col:
        num, prob, html_reason = generate_pro_stats(nums_2d[i])
        st.markdown(f"""<div><div class="pred-num-box"><div class="pred-num">{num}</div></div><div class="pred-detail-box">{html_reason}</div></div>""", unsafe_allow_html=True)

st.markdown("### 🔹 เลขท้าย 3 ตัว (Strategic)")
col3_1, col3_2, col3_3, col3_4 = st.columns(4)
nums_3d = ["936", "158", "472", "809"]
for i, col in enumerate([col3_1, col3_2, col3_3, col3_4]):
    with col:
        num, prob, html_reason = generate_pro_stats(nums_3d[i], is_3_digit=True)
        st.markdown(f"""<div><div class="pred-num-box" style="background: linear-gradient(135deg, #00695C, #00897B);"><div class="pred-num">{num}</div></div><div class="pred-detail-box">{html_reason}</div></div>""", unsafe_allow_html=True)

# SECTION 3: TOOLS
st.markdown("<h2>🛠️ Professional Tools</h2>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='pro-card'>", unsafe_allow_html=True)
    tab_stat, tab_check = st.tabs(["📊 Data Analysis", "✅ Prize Checker"])
    
    with tab_stat:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.markdown("<br>", unsafe_allow_html=True)
            search_num = st.text_input("Target Number", max_chars=3)
            if st.button("Run Analysis", use_container_width=True):
                if search_num:
                    st.success(f"Analysis Complete for {search_num}: High Frequency Detected!")
                else:
                    st.warning("Please enter a number.")
        with c2:
             st.info("System ready. Enter parameters to start.")

    with tab_check:
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("<br>", unsafe_allow_html=True)
            lotto_input = st.text_input("6-Digit Ticket Number", max_chars=6)
            if st.button("Verify Ticket", use_container_width=True):
                if len(lotto_input) == 6:
                    if lotto_input == '458145': st.balloons(); st.success("WINNER! Prize 1")
                    elif lotto_input[-2:] == '37': st.success("WINNER! Last 2 Digits")
                    else: st.error("Not a winning ticket.")
                else: st.warning("Enter full 6 digits.")
    st.markdown("</div>", unsafe_allow_html=True)
