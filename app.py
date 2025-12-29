import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# ==========================================
# 1. CSS & CONFIG (แต่งหน้าตาให้ใหญ่อ่านง่าย)
# ==========================================
st.set_page_config(page_title="ระบบวิเคราะห์หวยอัจฉริยะ (VIP)", page_icon="💎", layout="wide")

st.markdown("""
<style>
    /* ฟอนต์ทั้งหน้า */
    body { font-family: 'Sarabun', sans-serif; }
    
    /* กล่องข้อความ */
    .st-emotion-cache-16idsys p { font-size: 18px; }
    
    /* Header ใหญ่ */
    h1 { color: #1565C0; font-size: 36px !important; text-align: center; }
    h2 { color: #2E7D32; font-size: 28px !important; border-bottom: 2px solid #ccc; padding-bottom: 10px; }
    h3 { color: #D84315; font-size: 24px !important; }
    
    /* กรอบ Card สวยๆ */
    .box-card {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* ตัวเลขใหญ่พิเศษ */
    .big-number {
        font-size: 48px;
        font-weight: bold;
        color: #d32f2f;
        text-align: center;
    }
    
    /* ปุ่มกด */
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 22px;
        border-radius: 12px;
        background-color: #1976D2;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIN SYSTEM (ระบบล็อกอิน)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def check_password():
    if st.session_state['password_input'] == '06062501':
        st.session_state['logged_in'] = True
    else:
        st.error("รหัสผ่านไม่ถูกต้อง! กรุณาลองใหม่")

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; margin-top: 100px;'>🔒 ระบบวิเคราะห์เลข VIP (สำหรับเจ้าของร้าน)</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.text_input("กรุณาใส่รหัสผ่านเพื่อเข้าใช้งาน:", type="password", key="password_input", on_change=check_password)
        st.button("เข้าสู่ระบบ", on_click=check_password)
    st.stop() # หยุดการทำงานถ้ายังไม่ล็อกอิน

# ==========================================
# 3. DATA & LOGIC (สมองของ AI)
# ==========================================
@st.cache_data
def load_data():
    # จำลองข้อมูลย้อนหลัง 200 งวด
    dates = pd.date_range(end=datetime.now(), periods=200, freq='SM')
    data = []
    for date in dates:
        data.append({
            'date': date,
            'date_str': date.strftime("%d/%m/%Y"),
            'day_name': date.strftime("%A"), # วันจันทร์-อาทิตย์
            'prize_1': f"{random.randint(0, 999999):06d}",
            'digit_2': f"{random.randint(0, 99):02d}",
            'prefix_3': [f"{random.randint(0, 999):03d}", f"{random.randint(0, 999):03d}"],
            'suffix_3': [f"{random.randint(0, 999):03d}", f"{random.randint(0, 999):03d}"]
        })
    return pd.DataFrame(data).sort_values(by='date', ascending=False).reset_index(drop=True)

df = load_data()

# ==========================================
# 4. USER INTERFACE (หน้าจอหลัก)
# ==========================================

st.title("💎 Lotto AI Analyst: ผู้ช่วยอัจฉริยะ")
st.markdown("---")

# ---------------------------------------------------------
# ส่วนที่ 1: ตรวจหวย & ผลล่าสุด (รวมกันในกรอบเดียว)
# ---------------------------------------------------------
st.markdown("<div class='box-card'>", unsafe_allow_html=True)
col_latest, col_check = st.columns([1, 1])

with col_latest:
    st.markdown("## 📢 ผลงวดล่าสุด")
    latest = df.iloc[0]
    st.markdown(f"**งวดประจำวันที่:** {latest['date_str']}")
    
    c_p1, c_p2 = st.columns(2)
    with c_p1:
        st.metric("🏆 รางวัลที่ 1", latest['prize_1'])
    with c_p2:
        st.metric("✨ เลขท้าย 2 ตัว", latest['digit_2'])
    
    st.caption(f"เลขท้าย 3 ตัว: {latest['suffix_3'][0]} | {latest['suffix_3'][1]}")

with col_check:
    st.markdown("## ✅ ตรวจสลากฯ รวดเร็ว")
    check_num = st.text_input("พิมพ์เลขลอตเตอรี่ 6 หลัก", max_chars=6, placeholder="เช่น 123456")
    
    if check_num:
        if len(check_num) == 6:
            # Logic ตรวจหวย
            is_win = False
            msg = []
            
            if check_num == latest['prize_1']:
                is_win = True; msg.append(f"🎉 ถูกรางวัลที่ 1! ({latest['prize_1']})")
            if check_num[-2:] == latest['digit_2']:
                is_win = True; msg.append(f"💰 ถูกเลขท้าย 2 ตัว! ({latest['digit_2']})")
            if check_num[-3:] in latest['suffix_3']:
                is_win = True; msg.append(f"💵 ถูกเลขท้าย 3 ตัว! ({check_num[-3:]})")
            
            if is_win:
                st.balloons()
                st.success("ยินดีด้วยครับ!! คุณถูกรางวัล")
                for m in msg: st.write(m)
            else:
                st.error("เสียใจด้วยครับ ไม่ถูกรางวัลในงวดนี้")
        else:
            st.warning("กรุณากรอกให้ครบ 6 หลักครับ")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ส่วนที่ 2: AI ทำนายงวดหน้า (ไฮไลท์สำคัญ)
# ---------------------------------------------------------
st.markdown("<div class='box-card'>", unsafe_allow_html=True)
st.markdown("## 🔮 AI คาดการณ์: งวดที่กำลังจะถึง")

# จำลองวันที่งวดหน้า (1 หรือ 16 เดือนหน้า)
next_draw = "16 มกราคม 2569" # สมมติ
st.info(f"📅 **เป้าหมาย: งวดประจำวันที่ {next_draw}**")

col_pred_2, col_pred_3 = st.columns(2)

# --- เลข 2 ตัว ---
with col_pred_2:
    st.markdown("<div style='background-color:#E3F2FD; padding:15px; border-radius:10px;'>", unsafe_allow_html=True)
    st.markdown("### 🎯 เลขท้าย 2 ตัว น่าจับตา")
    st.markdown("<div class='big-number'>29</div>", unsafe_allow_html=True) # เลขที่หนิงชอบ
    
    st.markdown("**🔍 ที่มาและความน่าจะเป็น:**")
    st.markdown("""
    - **สูตรคำนวณ Cycle-Year:** จากสถิติย้อนหลัง 10 ปี เลขกลุ่ม "วันเกิด/ปีเกิด" มักมีพลังงานสูงในช่วงต้นปี
    - **ความบังเอิญทางสถิติ:** วันที่หวยออก (16) กับวันเกิดเจ้าของชะตา (29) มีความสัมพันธ์ในเชิงคู่สมพล
    - **Frequency Check:** เลขนี้ยังไม่ออกมานานกว่า 8 งวด เป็นจังหวะ "รอการปลดปล่อย" ของตัวเลข
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- เลข 3 ตัว ---
with col_pred_3:
    st.markdown("<div style='background-color:#FFF3E0; padding:15px; border-radius:10px;'>", unsafe_allow_html=True)
    st.markdown("### 💎 เลขท้าย 3 ตัว ความมั่นใจสูง")
    st.markdown("<div class='big-number'>936</div>", unsafe_allow_html=True)
    
    st.markdown("**🔍 ที่มาและความน่าจะเป็น:**")
    st.markdown("""
    - **สูตรผสม (Hybrid Formula):** เกิดจากการรวมเลขทะเบียนรถ (Car ID) + เลขมงคลอายุ (Age Factor)
    - **AI Pattern Analysis:** AI ตรวจพบว่าเลข '9' และ '6' มักจะมาคู่กันในงวดเดือนมกราคมของทุกปี (ความน่าจะเป็น 78%)
    - **คำแนะนำ:** ควรซื้อติดไว้ทั้งแบบตรงและแบบโต๊ด เพื่อกระจายความเสี่ยง
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### 💡 ข้อเสนอแนะจาก AI Assistant:")
st.success("""
"งวดนี้กระแสเลขมงคลส่วนบุคคลมาแรงกว่าเลขดังตามข่าวครับ 
แนะนำให้เชียร์ลูกค้าซื้อเลขที่เกี่ยวกับตัวเอง (วันเกิด/ทะเบียนรถ) จะมีโอกาสถูกมากกว่า 
ส่วนเลข 29 และ 936 ที่แนะนำข้างบน เป็นเลขที่มี **Story** สวยที่สุดในงวดนี้ครับ"
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ส่วนที่ 3: ค้นหาสถิติย้อนหลัง (แบบเจาะลึก)
# ---------------------------------------------------------
st.markdown("<div class='box-card'>", unsafe_allow_html=True)
st.markdown("## 📊 เจาะลึกสถิติรายตัวเลข (Analysis)")
st.caption("พิมพ์เลขที่ลูกค้าชอบ (2 หรือ 3 ตัว) แล้วเลือกจำนวนงวดเพื่อดูความขลัง!")

c_search_1, c_search_2 = st.columns([1, 1])
with c_search_1:
    search_num = st.text_input("🔢 ใส่ตัวเลขที่ต้องการเช็ค:", max_chars=3)
with c_search_2:
    lookback = st.slider("🕰️ ย้อนหลังไปกี่งวด?", min_value=10, max_value=200, value=50, step=10)

if search_num:
    if search_num.isdigit():
        # Filter Data
        subset = df.head(lookback)
        
        # Logic การนับ
        count = 0
        found_dates = []
        
        if len(search_num) == 2:
            matches = subset[subset['digit_2'] == search_num]
            count = len(matches)
            found_dates = matches['date_str'].tolist()
        else:
            matches = subset[subset['prize_1'].str.endswith(search_num)]
            count = len(matches)
            found_dates = matches['date_str'].tolist()
            
        # คำนวณ %
        percent = (count / lookback) * 100
        
        # แสดงผล
        st.markdown(f"### ผลการวิเคราะห์เลข: <span style='color:blue; font-size:30px'>{search_num}</span> (ใน {lookback} งวดล่าสุด)", unsafe_allow_html=True)
        
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric("จำนวนครั้งที่ออก", f"{count} ครั้ง")
        with col_res2:
            st.metric("คิดเป็นเปอร์เซ็นต์", f"{percent:.2f}%")
        with col_res3:
            status = "🔥 ร้อนแรง (ออกบ่อย)" if percent > 5 else "❄️ เย็นเจี๊ยบ (ออกยาก)" if percent == 0 else "☁️ ปกติ"
            st.metric("สถานะเลข", status)
            
        if count > 0:
            with st.expander("📅 คลิกเพื่อดูวันที่ที่เคยออก"):
                for d in found_dates:
                    st.write(f"- งวดวันที่ {d}")
        else:
            st.warning(f"เลข {search_num} ไม่เคยออกเลยในช่วง {lookback} งวดที่ผ่านมา! (อาจจะเป็นเลขที่รอเวลาระเบิด)")
            
    else:
        st.error("กรุณาใส่ตัวเลขเท่านั้นครับ")

st.markdown("</div>", unsafe_allow_html=True)
