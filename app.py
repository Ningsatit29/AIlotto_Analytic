import streamlit as st
import random
from datetime import datetime
import os

# ==========================================
# 1. ตั้งค่าหน้าจอ (Theme สีสะอาดตา)
# ==========================================
st.set_page_config(page_title="โปรแกรมคู่คิดร้านแม่", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');
    
    .stApp { 
        font-family: 'Sarabun', sans-serif !important;
        background-color: #FAFAFA !important; 
    }
    header {visibility: hidden;}
    .block-container { padding-top: 20px !important; }

    /* การ์ดต่างๆ */
    .mom-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
        border: 2px solid #F8BBD0; 
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* ตัวเลข */
    .num-huge { font-size: 80px; font-weight: 900; color: #C2185B; line-height: 1; }
    .num-big { font-size: 55px; font-weight: 800; color: #1976D2; }
    .num-med { font-size: 40px; font-weight: 700; color: #424242; }
    
    /* ป้ายกำกับ */
    .label-badge {
        background-color: #FCE4EC;
        color: #880E4F;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 20px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* กล่องแทนรูปภาพ (กรณีไม่มีรูป) */
    .placeholder-box {
        background-color: #E3F2FD;
        border: 2px dashed #1976D2;
        border-radius: 15px;
        padding: 40px;
        text-align: center;
        color: #1565C0;
        font-size: 20px;
    }
    .placeholder-icon { font-size: 60px; display: block; margin-bottom: 10px; }

    /* Input & Button */
    .stTextInput input { font-size: 24px !important; text-align: center; border-radius: 15px; padding: 15px; }
    .stButton button { font-size: 24px !important; border-radius: 15px; height: 60px; background-color: #C2185B !important; color: white !important; }

</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ระบบรหัสผ่าน
# ==========================================
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<br><br><h1 style='text-align:center; color:#C2185B;'>🔒 ระบบช่วยขายร้านแม่ (VIP)</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        pwd = st.text_input("ใส่รหัสผ่านตรงนี้จ้ะ", type="password")
        if st.button("เข้าใช้งาน"):
            if pwd == '06062501': st.session_state.logged_in = True
            else: st.error("รหัสผิดจ้ะแม่")
    st.stop()

# ==========================================
# 3. ข้อมูล & หน้าจอหลัก
# ==========================================
last_draw = "16 ธันวาคม 2568" 
next_draw = "30 ธันวาคม 2568" 

st.title(f"💰 งวดส่งท้ายปี: {next_draw}")

# --- ส่วนที่ 1: ผลงวดเก่า ---
st.markdown(f"## 1. ย้อนรอยงวดที่แล้ว ({last_draw})")
with st.container():
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class="mom-card">
            <div class="label-badge">รางวัลที่ 1</div>
            <div class="num-big">458145</div>
            <div style="font-size:18px; color:#666; margin-top:10px;">
                3 ตัวหน้า: 602, 242 | 3 ตัวหลัง: 389, 239
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="mom-card">
            <div class="label-badge">เลขท้าย 2 ตัว</div>
            <div class="num-huge">37</div>
        </div>
        """, unsafe_allow_html=True)

# --- ส่วนที่ 2: เลขเด็ดงวดนี้ ---
st.markdown(f"## 2. 🔮 แนวทางเลขเด็ด (งวด {next_draw})")
c_rec1, c_rec2 = st.columns(2)

with c_rec1:
    st.markdown("""
    <div class="mom-card" style="border: 3px solid #E91E63;">
        <div class="label-badge" style="background:#F48FB1; color:white;">2 ตัว มาแรงที่สุด</div>
        <div class="num-huge" style="color:#E91E63;">29</div>
        <div style="text-align:left; margin-top:15px; font-size:18px;">
           <b>ทำไมต้องเลขนี้?</b><br>
           "เลขนี้คือ <b>วันเกิดของหนิงเอง (วันที่ 29)</b> ครับแม่ แล้วบังเอิญมากที่งวดนี้หวยออกใกล้วันที่ 30 พอดี เป๊ะปังมาก!"
        </div>
    </div>
    """, unsafe_allow_html=True)

with c_rec2:
    st.markdown("""
    <div class="mom-card" style="border: 3px solid #1976D2;">
        <div class="label-badge" style="background:#64B5F6; color:white;">3 ตัว สวยมาก</div>
        <div class="num-huge" style="color:#1976D2;">936</div>
        <div style="text-align:left; margin-top:15px; font-size:18px;">
           <b>ที่มาของเลขนี้?</b><br>
           "อันนี้มาจาก <b>ทะเบียนรถ Accord (เลข 9)</b> ผสมกับเลขมงคลปีใหม่ครับ ถ้าแม่จะเชียร์ลูกค้า บอกเลยว่า <b>'เลขพาลูกกลับบ้าน'</b>"
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ส่วนที่ 3: มุมครอบครัว (แบบฉลาด - ไม่มีรูปก็สวยได้) ---
st.markdown("## 📸 มุมครอบครัวสุขสันต์")

# ฟังก์ชันแสดงผลแบบฉลาด (Smart Display)
def show_smart_content(col, filename, caption, icon):
    with col:
        # เช็คว่ามีไฟล์รูปไหม (รองรับ jpg/png)
        if os.path.exists(filename + ".jpg"):
            st.image(filename + ".jpg", caption=caption, use_container_width=True)
        elif os.path.exists(filename + ".png"):
            st.image(filename + ".png", caption=caption, use_container_width=True)
        else:
            # ถ้าไม่มีรูป ให้แสดงกล่องน่ารักๆ แทน (จะได้ไม่ Error)
            st.markdown(f"""
            <div class="placeholder-box">
                <span class="placeholder-icon">{icon}</span>
                <div><b>{caption}</b></div>
                <div style="font-size:16px; color:#888;">(ไว้เอารูปมาใส่ทีหลังได้นะครับ)</div>
            </div>
            """, unsafe_allow_html=True)

c_img1, c_img2, c_img3 = st.columns(3)
show_smart_content(c_img1, "mom", "แม่สุดสวย", "👩")
show_smart_content(c_img2, "us", "แม่กับหนิง", "👩‍👦")
show_smart_content(c_img3, "family", "ครอบครัวของเรา", "👨‍👩‍👦‍👦")

# --- ส่วนที่ 4: เครื่องมือช่วยขาย ---
st.markdown("## 3. 🛠️ เครื่องมือช่วยแม่ขาย")
tab1, tab2 = st.tabs(["🔎 เช็คประวัติเลข", "✅ ตรวจหวยด่วน"])

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    num = st.text_input("ลูกค้าถามหาเลขไหน? (พิมพ์เลย)")
    if st.button("วิเคราะห์"):
        st.success(f"เลข {num} : กำลังมาแรงเลยแม่ เชียร์ขายได้เลย!")

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    chk = st.text_input("กรอกเลข 6 ตัวตรวจรางวัล")
    if st.button("ตรวจรางวัล"):
        if chk == "458145": st.success("🎉 ถูกรางวัลที่ 1 รวยแล้ว!!")
        elif chk[-2:] == "37": st.success("💰 ถูกเลขท้าย 2 ตัว!!")
        else: st.error("ไม่ถูกจ้า งวดหน้าเอาใหม่")
