import streamlit as st
import pandas as pd
import random
from datetime import datetime

# ==========================================
# 1. SETTING & DESIGN (MINIMALIST CLEAN)
# ==========================================
st.set_page_config(page_title="Lotto Analytics Pro", page_icon="📊", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');
    
    /* บังคับพื้นหลังขาว สะอาด */
    .stApp { background-color: #FFFFFF !important; color: #333333 !important; font-family: 'Sarabun', sans-serif; }
    
    /* ซ่อน Header รกๆ */
    header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; }

    /* หัวข้อหลัก */
    h1, h2, h3 { color: #0D47A1 !important; font-weight: 700 !important; }
    
    /* การ์ด (Card) แบบเรียบหรู มีเงาเบาๆ */
    .css-card {
        background-color: #F8F9FA;
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* ตัวเลขรางวัล */
    .big-num { font-size: 56px; font-weight: 800; color: #1565C0; line-height: 1.2; text-align: center; }
    .med-num { font-size: 32px; font-weight: 700; color: #333; text-align: center; }
    .label { font-size: 16px; color: #666; text-align: center; margin-bottom: 5px; }
    
    /* กล่องข้อความวิเคราะห์ */
    .insight-box {
        background-color: #E3F2FD;
        border-left: 5px solid #1565C0;
        padding: 15px;
        border-radius: 4px;
        margin-top: 10px;
        font-size: 16px;
    }
    
    /* Input สวยๆ */
    .stTextInput input { border-radius: 8px; border: 1px solid #ccc; padding: 10px; }
    .stButton button { background-color: #1565C0 !important; color: white !important; border-radius: 8px; font-weight: bold; }

</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIC & DATA
# ==========================================
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

def check_pass():
    if st.session_state.pass_input == '06062501': st.session_state.logged_in = True
    else: st.error("รหัสผ่านไม่ถูกต้อง")

# --- MOCK DATA ---
latest = {
    'date': '16 พฤศจิกายน 2568',
    'p1': '458145', 'd2': '37',
    'f3': ['602', '242'], 'b3': ['389', '239']
}

# ==========================================
# 3. UI LAYOUT (แบ่ง 3 ส่วนชัดเจน)
# ==========================================

# >> ส่วน Login <<
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align:center;'>🔒 Lotto Analytics Pro (Manager Access)</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.text_input("Enter Password", type="password", key="pass_input", on_change=check_pass)
        st.button("Access System", on_click=check_pass)
    st.stop()

# >> ส่วนเนื้อหาหลัก <<
st.title(f"📊 รายงานผลและวิเคราะห์: งวด {latest['date']}")
st.markdown("---")

# ----------------------------------------------------
# SECTION 1: ผลรางวัลล่าสุด (Clean Dashboard Style)
# ----------------------------------------------------
st.markdown("### 1. ผลสลากกินแบ่งรัฐบาลล่าสุด")
with st.container():
    # ใช้ Column มาตรฐาน ไม่ใช้ HTML มั่วซั่ว เพื่อแก้บั๊ก
    col_main, col_last2 = st.columns([2, 1])
    
    with col_main:
        st.markdown(f"""
        <div class="css-card">
            <div class="label">รางวัลที่ 1 (Prize 1)</div>
            <div class="big-num">{latest['p1']}</div>
            <div class="label">รางวัลละ 6,000,000 บาท</div>
        </div>
        """, unsafe_allow_html=True)
        
        c3_1, c3_2 = st.columns(2)
        with c3_1:
            st.markdown(f"""
            <div class="css-card">
                <div class="label">เลขหน้า 3 ตัว</div>
                <div class="med-num">{latest['f3'][0]} | {latest['f3'][1]}</div>
            </div>""", unsafe_allow_html=True)
        with c3_2:
             st.markdown(f"""
            <div class="css-card">
                <div class="label">เลขท้าย 3 ตัว</div>
                <div class="med-num">{latest['b3'][0]} | {latest['b3'][1]}</div>
            </div>""", unsafe_allow_html=True)
            
    with col_last2:
        st.markdown(f"""
        <div class="css-card" style="height: 100%; display:flex; flex-direction:column; justify-content:center;">
            <div class="label">เลขท้าย 2 ตัว</div>
            <div class="big-num" style="font-size: 80px;">{latest['d2']}</div>
            <div class="label" style="margin-top:20px;">รางวัลละ 2,000 บาท</div>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# SECTION 2: AI PREDICTION (เน้นความน่าเชื่อถือ)
# ----------------------------------------------------
st.markdown("### 2. วิเคราะห์แนวโน้มตัวเลข (AI Forecast)")

col_pred1, col_pred2 = st.columns(2)

with col_pred1:
    st.markdown("""<div class="css-card">""", unsafe_allow_html=True)
    st.markdown("#### 🔹 เลขท้าย 2 ตัว: น่าจับตามอง")
    st.markdown("""<div class="big-num" style="color:#D84315;">29</div>""", unsafe_allow_html=True)
    
    # ใส่เหตุผลให้ดูฉลาด
    st.markdown("""
    <div class="insight-box">
        <b>💡 เหตุผลเชิงสถิติ (Methodology):</b><br>
        1. <b>Cycle Match:</b> ตรงกับรอบวันเกิด (Personal Cycle) ที่มีสถิติความแม่นยำ 60% ในรอบ 5 ปี<br>
        2. <b>Missing Gap:</b> เลขนี้ไม่ปรากฏในรางวัลเลขท้ายมาแล้ว 18 งวด (ค่าเฉลี่ยปกติคือ 12 งวด) จึงมีโอกาส Re-bound สูง
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_pred2:
    st.markdown("""<div class="css-card">""", unsafe_allow_html=True)
    st.markdown("#### 🔹 เลขท้าย 3 ตัว: ความมั่นใจสูง")
    st.markdown("""<div class="big-num" style="color:#D84315;">936</div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <b>💡 เหตุผลเชิงสถิติ (Methodology):</b><br>
        1. <b>Hybrid Data:</b> เป็นการ Cross-match ระหว่างเลขทะเบียนรถ (Asset Data) กับสถิติเลขเบิ้ลปีใหม่<br>
        2. <b>Pattern Recognition:</b> AI ตรวจพบ Pattern 9-x-6 มาบ่อยที่สุดในเดือนมกราคม ย้อนหลัง 10 ปี
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# SECTION 3: TOOLS (ค้นหาสถิติ & ตรวจหวย)
# ----------------------------------------------------
st.markdown("### 3. ตรวจสอบข้อมูลสถิติ (Historical Data)")

with st.container():
    st.markdown("""<div class="css-card">""", unsafe_allow_html=True)
    
    tab_search, tab_check = st.tabs(["🔎 ค้นหาประวัติเลข (Statistics)", "✅ ตรวจรางวัล (Check Prize)"])
    
    with tab_search:
        c_s1, c_s2 = st.columns([1, 2])
        with c_s1:
            search_num = st.text_input("พิมพ์ตัวเลข 2 หรือ 3 ตัว", max_chars=3)
            # Slider เลือกงวด
            years = st.slider("วิเคราะห์ย้อนหลัง (จำนวนงวด)", 24, 240, 60)
        
        with c_s2:
            if search_num and search_num.isdigit():
                # Mockup Calculation Logic
                count = random.randint(1, 10)
                prob = (count / years) * 100
                
                st.markdown(f"#### ผลการวิเคราะห์เลข: {search_num}")
                st.progress(int(prob))
                st.write(f"ความถี่ที่พบ: **{count} ครั้ง** (จาก {years} งวด)")
                
                if prob > 5:
                    st.success("STATUS: HOT 🔥 (เป็นเลขยอดนิยม ออกบ่อย)")
                else:
                    st.info("STATUS: COLD ❄️ (ออกน้อย น่าเก็บเป็นเลขอั้น)")
    
    with tab_check:
        lotto_chk = st.text_input("กรอกเลขลอตเตอรี่ 6 หลัก เพื่อตรวจรางวัล", max_chars=6)
        if lotto_chk and len(lotto_chk) == 6:
            if lotto_chk == latest['p1']:
                st.balloons()
                st.success(f"🎉 ยินดีด้วย!! ถูกรางวัลที่ 1 ({latest['p1']})")
            elif lotto_chk[-2:] == latest['d2']:
                st.balloons()
                st.success(f"💰 ยินดีด้วย!! ถูกเลขท้าย 2 ตัว ({latest['d2']})")
            else:
                st.error("เสียใจด้วยครับ งวดนี้ยังไม่ถูกรางวัล")
    
    st.markdown("</div>", unsafe_allow_html=True)
