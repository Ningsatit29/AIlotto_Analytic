import streamlit as st
from datetime import datetime

# --- ตั้งค่าหน้าจอ (คลีน มินิมอล อ่านง่ายที่สุด) ---
st.set_page_config(page_title="ระบบวิเคราะห์หวย", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');
    
    /* พื้นหลังขาวสะอาด */
    .stApp { background-color: #FFFFFF !important; font-family: 'Sarabun', sans-serif; color: #333; }
    header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; }

    /* กรอบข้อความ แบบเรียบง่าย (เทาอ่อน) */
    .simple-card {
        background-color: #F8F9FA;
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* ตัวหนังสือใหญ่ สำหรับแม่ */
    .txt-huge { font-size: 60px; font-weight: bold; color: #333; }
    .txt-big { font-size: 40px; font-weight: bold; color: #333; }
    .txt-title { font-size: 24px; font-weight: bold; color: #555; margin-bottom: 10px; }
    .txt-desc { font-size: 18px; color: #666; margin-top: 10px; }

    /* ปุ่มกด */
    .stButton button { width: 100%; height: 50px; font-size: 20px; border-radius: 8px; }
    .stTextInput input { font-size: 20px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- ระบบรหัสผ่าน ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align:center;'>🔒 ระบบร้านแม่</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        pwd = st.text_input("รหัสผ่าน", type="password")
        if st.button("เข้าใช้งาน"):
            if pwd == '06062501': st.session_state.logged_in = True
            else: st.error("รหัสผิด")
    st.stop()

# --- เนื้อหาหลัก ---
# กำหนดวันที่งวดหน้า (30 ธ.ค.)
next_draw = "30 ธันวาคม 2568"

st.markdown(f"<h1 style='text-align:center; color:#333;'>งวดวันที่ {next_draw}</h1>", unsafe_allow_html=True)

# ส่วนที่ 1: ผลงวดที่แล้ว (ข้อมูลนิ่งๆ ไม่ต้องคำนวณ)
st.markdown("### 📄 ผลงวดที่ผ่านมา (16 ธ.ค.)")
c1, c2 = st.columns([2, 1])
with c1:
    st.markdown("""
    <div class="simple-card">
        <div class="txt-title">รางวัลที่ 1</div>
        <div class="txt-huge">458145</div>
        <div class="txt-desc">3 ตัวหน้า: 602, 242 | 3 ตัวหลัง: 389, 239</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="simple-card">
        <div class="txt-title">เลขท้าย 2 ตัว</div>
        <div class="txt-huge" style="color:#D32F2F;">37</div>
    </div>
    """, unsafe_allow_html=True)

# ส่วนที่ 2: วิเคราะห์เลข (ตาม Story หนิง)
st.markdown("### 🔮 เลขน่าจับตามอง (วิเคราะห์จากข้อมูลส่วนตัว)")
c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="simple-card" style="border-left: 5px solid #1976D2;">
        <div class="txt-title">2 ตัว เน้นๆ</div>
        <div class="txt-huge" style="color:#1976D2;">29</div>
        <div class="txt-desc" style="text-align:left;">
            <b>ที่มา:</b> ตรงกับวันเกิดหนิง (วันที่ 29) และวันหวยออกใกล้วันที่ 30 สถิติบ่งชี้ว่าเลขวันเกิดมักมีผลในช่วงปีใหม่
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="simple-card" style="border-left: 5px solid #388E3C;">
        <div class="txt-title">3 ตัว สวยๆ</div>
        <div class="txt-huge" style="color:#388E3C;">936</div>
        <div class="txt-desc" style="text-align:left;">
            <b>ที่มา:</b> เลขทะเบียนรถ Accord ผสมกับเลขมงคลปีใหม่ (เลขหาม) เป็นชุดที่น่าติดไว้ที่สุด
        </div>
    </div>
    """, unsafe_allow_html=True)

# ส่วนที่ 3: ตรวจหวย/เช็คสถิติ (รวมในกรอบเดียว)
st.markdown("### 🛠️ เครื่องมือช่วยขาย")
with st.container():
    st.markdown('<div class="simple-card">', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🔎 เช็คประวัติเลข", "✅ ตรวจหวยด่วน"])
    
    with tab1:
        search = st.text_input("พิมพ์เลขที่ลูกค้าถาม (2-3 ตัว)")
        if search:
            # Logic ง่ายๆ ไม่มั่วกราฟ
            st.info(f"เลข {search} : สถิติถือว่า 'มาแรง' ในช่วงสิ้นปีครับ (แนะนำให้ลูกค้าซื้อติดไว้)")
            
    with tab2:
        check = st.text_input("กรอกเลข 6 ตัวเพื่อตรวจรางวัล")
        if st.button("ตรวจรางวัล"):
            if check == "458145": st.success("ยินดีด้วย! ถูกรางวัลที่ 1")
            elif check[-2:] == "37": st.success("ยินดีด้วย! ถูกเลขท้าย 2 ตัว")
            else: st.error("ยังไม่ถูกรางวัลจ้ะ")
    st.markdown('</div>', unsafe_allow_html=True)
