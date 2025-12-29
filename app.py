import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# ==========================================
# 1. CSS DESIGN (หัวใจสำคัญของหน้านี้)
# ==========================================
st.set_page_config(page_title="ระบบวิเคราะห์หวยแม่นๆ", page_icon="💰", layout="wide")

st.markdown("""
<style>
    /* โหลดฟอนต์ไทยสวยๆ */
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;700&display=swap');
    
    /* พื้นหลังและฟอนต์หลัก */
    .stApp {
        background-color: #FFFFFF; /* พื้นขาว */
        font-family: 'Prompt', sans-serif;
    }
    
    /* หัวข้อหลัก (เช่น 'ผลงวดล่าสุด') */
    h1, h2, h3 {
        color: #D81B60; /* สีชมพูเข้มแบบในรูป */
        font-weight: bold !important;
    }
    h1 { font-size: 42px !important; text-align: center; margin-bottom: 30px; }
    h2 { font-size: 32px !important; }
    
    /* กรอบ Card สีชมพู */
    .pink-card {
        border: 3px solid #D81B60; /* ขอบหนาสีชมพู */
        border-radius: 20px; /* มุมมน */
        padding: 25px;
        margin-bottom: 25px;
        background-color: #FFF0F5; /* พื้นหลังชมพูอ่อนๆ */
        box-shadow: 0 4px 8px rgba(216, 27, 96, 0.2);
    }
    
    /* ตัวเลขรางวัลใหญ่ๆ */
    .lotto-number-big {
        font-size: 60px;
        font-weight: 900;
        color: #000000; /* เลขสีดำ */
        text-align: center;
        letter-spacing: 2px;
    }
    .lotto-number-medium {
        font-size: 40px;
        font-weight: 800;
        color: #000000;
        text-align: center;
    }
    
    /* ป้ายกำกับรางวัล */
    .reward-label {
        font-size: 24px;
        color: #D81B60;
        text-align: center;
        font-weight: bold;
        background-color: #FFC1E3;
        padding: 5px 15px;
        border-radius: 30px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    /* ช่องกรอกข้อมูล */
    .stTextInput input {
        font-size: 24px;
        padding: 15px;
        border: 2px solid #D81B60;
        border-radius: 10px;
        text-align: center;
    }
    
    /* ปุ่มกด */
    .stButton button {
        background-color: #D81B60 !important;
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        padding: 15px 0 !important;
        border: none !important;
    }
    
    /* กล่อง Login */
    .login-box {
        max-width: 500px;
        margin: 100px auto;
        padding: 40px;
        border: 4px solid #D81B60;
        border-radius: 30px;
        text-align: center;
        background-color: #FFF0F5;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIN SYSTEM (รหัสผ่าน)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def check_password():
    if st.session_state['password_input'] == '06062501':
        st.session_state['logged_in'] = True
    else:
        st.error("รหัสผ่านผิดครับแม่! ลองใหม่นะ")

if not st.session_state['logged_in']:
    st.markdown("""
        <div class='login-box'>
            <h1>🔒 ระบบวิเคราะห์หวย (VIP)</h1>
            <p style='font-size: 20px;'>กรุณาใส่รหัสผ่านเพื่อเข้าใช้งาน</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.text_input("", type="password", key="password_input", placeholder="ใส่รหัสที่นี่...", on_change=check_password)
        st.button("เข้าสู่ระบบ", on_click=check_password)
    st.stop()

# ==========================================
# 3. DATA MOCKUP (จำลองข้อมูล)
# ==========================================
@st.cache_data
def load_data():
    # ข้อมูลจำลองงวดล่าสุด (แก้ตรงนี้ให้เป็นงวดจริงได้)
    latest_data = {
        'date': '16 พฤศจิกายน 2568', # วันที่ตามรูปตัวอย่าง
        'prize_1': '458145',
        'digit_2': '37',
        'front_3': ['602', '242'],
        'back_3': ['389', '239']
    }
    
    # ข้อมูลจำลองสำหรับค้นหาสถิติ (200 งวด)
    history_data = []
    dates = pd.date_range(end=datetime.now(), periods=200, freq='SM')
    for date in dates:
        history_data.append({
            'date_str': date.strftime("%d/%m/%Y"),
            'prize_1': f"{random.randint(0, 999999):06d}",
            'digit_2': f"{random.randint(0, 99):02d}",
            'back_3': [f"{random.randint(0, 999):03d}", f"{random.randint(0, 999):03d}"]
        })
    df_history = pd.DataFrame(history_data)
    
    return latest_data, df_history

latest, df_hist = load_data()

# ==========================================
# 4. MAIN LAYOUT (จัดหน้าตามที่ขอ)
# ==========================================

st.markdown("<h1>💰 ผลสลากฯ & ระบบวิเคราะห์อัจฉริยะ 💰</h1>", unsafe_allow_html=True)

# --- ส่วนที่ 1: ผลรางวัลล่าสุด (ตามดีไซน์ในรูป) ---
st.markdown(f"<div class='pink-card' style='text-align:center;'><h2>งวดประจำวันที่ {latest['date']}</h2></div>", unsafe_allow_html=True)

c_p1, c_p2 = st.columns([2, 1])

with c_p1:
    st.markdown("""
    <div class='pink-card' style='text-align:center;'>
        <div class='reward-label'>รางวัลที่ 1</div>
        <div class='lotto-number-big'>{}</div>
        <p style='font-size:20px; color:#666;'>รางวัลละ 6,000,000 บาท</p>
    </div>
    """.format(latest['prize_1']), unsafe_allow_html=True)
    
    c_3digit_1, c_3digit_2 = st.columns(2)
    with c_3digit_1:
         st.markdown("""
        <div class='pink-card' style='text-align:center; padding:15px;'>
            <div class='reward-label' style='font-size:20px;'>เลขหน้า 3 ตัว</div>
            <div class='lotto-number-medium'>{} | {}</div>
        </div>
        """.format(latest['front_3'][0], latest['front_3'][1]), unsafe_allow_html=True)
    with c_3digit_2:
         st.markdown("""
        <div class='pink-card' style='text-align:center; padding:15px;'>
            <div class='reward-label' style='font-size:20px;'>เลขท้าย 3 ตัว</div>
            <div class='lotto-number-medium'>{} | {}</div>
        </div>
        """.format(latest['back_3'][0], latest['back_3'][1]), unsafe_allow_html=True)

with c_p2:
    st.markdown("""
    <div class='pink-card' style='text-align:center; height: 400px; display: flex; flex-direction: column; justify-content: center;'>
        <div class='reward-label'>เลขท้าย 2 ตัว</div>
        <div class='lotto-number-big' style='font-size: 100px;'>{}</div>
        <p style='font-size:20px; color:#666;'>รางวัลละ 2,000 บาท</p>
    </div>
    """.format(latest['digit_2']), unsafe_allow_html=True)

# --- ส่วนที่ 2: AI ทำนาย & ค้นหาสถิติ & ตรวจหวย (รวมกันในกรอบใหญ่) ---
st.markdown("""
<div class='pink-card'>
    <h2 style='text-align:center;'>🔮 ศูนย์วิเคราะห์และตรวจสอบ (AI Center)</h2>
""", unsafe_allow_html=True)

tab_pred, tab_search, tab_check = st.tabs(["⭐ AI คาดการณ์งวดหน้า", "📊 ค้นหาสถิติย้อนหลัง", "✅ ตรวจหวยด่วน"])

# >>> Tab 1: AI คาดการณ์ <<<
with tab_pred:
    st.markdown("### 🎯 เลขเด็ดงวดหน้า (วิเคราะห์จาก Data 10 ปี)")
    c_pred1, c_pred2 = st.columns(2)
    
    with c_pred1:
        st.markdown("""
        <div style='background-color:white; border:2px solid #D81B60; border-radius:15px; padding:20px; text-align:center;'>
            <div class='reward-label'>เลข 2 ตัว น่าจับตา</div>
            <div class='lotto-number-big' style='color:#D81B60;'>29</div>
            <div style='text-align:left; margin-top:20px;'>
                <p style='font-size:18px;'><b>🔍 ที่มา:</b> เป็นเลขมงคลวันเกิด (29) ที่โคจรมาตรงกับกำลังวันในงวดนี้พอดี สถิติบ่งชี้ว่ามีพลังงานสูงมาก</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_pred2:
        st.markdown("""
        <div style='background-color:white; border:2px solid #D81B60; border-radius:15px; padding:20px; text-align:center;'>
            <div class='reward-label'>เลข 3 ตัว มั่นใจสูง</div>
            <div class='lotto-number-big' style='color:#D81B60;'>936</div>
            <div style='text-align:left; margin-top:20px;'>
                <p style='font-size:18px;'><b>🔍 ที่มา:</b> เกิดจากการผสมเลขทะเบียนรถ (9) เข้ากับเลขสถิติที่ออกบ่อยในเดือนนี้ (36) เป็นชุดที่ AI แนะนำให้ติดไว้</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.info("💡 **คำแนะนำ:** งวดนี้เน้นเลขที่เกี่ยวกับตัวเอง (วันเกิด/ทะเบียนรถ) จะมีดวงมากกว่าเลขกระแสครับ!")

# >>> Tab 2: ค้นหาสถิติ <<<
with tab_search:
    st.markdown("### 🔎 เช็คประวัติเลขฮิต")
    c_s1, c_s2 = st.columns([2, 1])
    with c_s1:
        search_num = st.text_input("พิมพ์เลขที่ชอบ (2 หรือ 3 ตัว)", max_chars=3, placeholder="เช่น 89")
    with c_s2:
        lookback = st.selectbox("ย้อนหลังกี่งวด?", options=[50, 100, 200], index=0)
    
    if search_num and search_num.isdigit():
        subset = df_hist.head(lookback)
        count = 0
        if len(search_num) == 2:
            count = subset[subset['digit_2'] == search_num].shape[0]
        else:
            count = subset[subset['prize_1'].str.endswith(search_num)].shape[0] # เช็คท้ายรางวัลที่ 1
            
        st.markdown(f"""
        <div style='text-align:center; margin-top:20px;'>
            <p style='font-size:24px;'>ผลการค้นหาเลข: <span style='color:#D81B60; font-weight:bold;'>{search_num}</span> (ใน {lookback} งวดล่าสุด)</p>
            <div class='lotto-number-big' style='font-size:80px; color:#D81B60;'>เคยออก {count} ครั้ง</div>
        </div>
        """, unsafe_allow_html=True)

# >>> Tab 3: ตรวจหวย <<<
with tab_check:
    st.markdown("### ✅ กรอกปุ๊บ รู้ผลปั๊บ")
    check_input = st.text_input("พิมพ์เลขลอตเตอรี่ 6 หลัก", max_chars=6, placeholder="เช่น 458145")
    
    if check_input and len(check_input) == 6:
        is_win = False
        win_msg = []
        if check_input == latest['prize_1']:
            is_win =True; win_msg.append(f"🎉 ถูกรางวัลที่ 1! ({latest['prize_1']})")
        if check_input[-2:] == latest['digit_2']:
            is_win =True; win_msg.append(f"💰 ถูกเลขท้าย 2 ตัว! ({latest['digit_2']})")
        if check_input[:3] in latest['front_3']:
             is_win =True; win_msg.append(f"💵 ถูกเลขหน้า 3 ตัว! ({check_input[:3]})")
        if check_input[-3:] in latest['back_3']:
             is_win =True; win_msg.append(f"💵 ถูกเลขท้าย 3 ตัว! ({check_input[-3:]})")
             
        if is_win:
            st.balloons()
            st.success("ยินดีด้วยครับ!! คุณถูกรางวัล")
            for msg in win_msg: st.markdown(f"## {msg}")
        else:
            st.error("เสียใจด้วยครับ ไม่ถูกรางวัลในงวดนี้")

st.markdown("</div>", unsafe_allow_html=True) # ปิดกรอบใหญ่ AI Center
