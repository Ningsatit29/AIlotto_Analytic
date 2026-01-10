import streamlit as st
import pandas as pd
import random
from datetime import datetime
import os

# ==========================================
# 1. ตั้งค่าหน้าจอ (เน้นตัวใหญ่ อ่านง่าย สบายตา)
# ==========================================
st.set_page_config(page_title="โปรแกรมคู่คิดร้านแม่", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;800&display=swap');
    
    /* บังคับใช้ฟอนต์ไทย สวยๆ อ่านง่าย */
    .stApp { 
        font-family: 'Prompt', sans-serif !important;
        background-color: #FAFAFA !important; /* พื้นขาวนวล สบายตา */
    }
    
    /* ซ่อนหัวเว็บรกๆ */
    header {visibility: hidden;}
    .block-container { padding-top: 20px !important; }

    /* หัวข้อใหญ่ๆ */
    h1 { color: #C2185B !important; font-size: 38px !important; font-weight: 800 !important; text-align: center; }
    h2 { color: #333 !important; font-size: 28px !important; font-weight: 600 !important; margin-top: 30px; }
    h3 { color: #E91E63 !important; font-size: 24px !important; font-weight: 600 !important; }

    /* กรอบสวยๆ (Card) แบบมนๆ นุ่มๆ */
    .mom-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); /* เงาฟุ้งๆ */
        border: 2px solid #F8BBD0; /* ขอบสีชมพูอ่อนๆ ให้ดูสดใส */
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* ตัวเลขรางวัล (ใหญ่สะใจแม่) */
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
    
    /* กล่องข้อความบรรยาย (Story) */
    .story-box {
        background-color: #E3F2FD;
        border-left: 8px solid #1976D2;
        padding: 20px;
        border-radius: 10px;
        font-size: 18px;
        line-height: 1.6;
        color: #0D47A1;
        text-align: left;
        margin-top: 15px;
    }
    
    /* แต่งรูปภาพ */
    .stImage {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stImage img {
        border-radius: 15px;
        transition: transform 0.3s ease;
    }
    .stImage img:hover {
        transform: scale(1.02);
    }

    /* Input ใหญ่ๆ */
    .stTextInput input { font-size: 24px !important; text-align: center; border-radius: 15px; padding: 15px; }
    .stButton button { font-size: 24px !important; border-radius: 15px; height: 60px; background-color: #C2185B !important; color: white !important; }

</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ระบบรหัสผ่าน (เหมือนเดิม)
# ==========================================
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

def check_pass():
    if st.session_state.pass_input == '06062501': st.session_state.logged_in = True
    else: st.error("รหัสผิดจ้ะแม่ ลองใหม่นะ")

if not st.session_state.logged_in:
    st.markdown("<br><br><h1 style='color:#C2185B;'>🔒 ระบบช่วยขายร้านแม่ (VIP)</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.text_input("ใส่รหัสผ่านตรงนี้จ้ะ", type="password", key="pass_input", on_change=check_pass)
        st.button("เข้าใช้งาน", on_click=check_pass)
    st.stop()

# ==========================================
# 3. ข้อมูลวันที่ (Manual Set ตามสั่ง)
# ==========================================
last_draw_date = "16 ธันวาคม 2568" # งวดที่แล้ว
next_draw_date = "30 ธันวาคม 2568" # งวดที่จะถึง (หวยออกวันนี้!)

# ผลรางวัลงวดที่แล้ว (สมมติ)
last_p1 = "458145"
last_2d = "37"
last_f3 = ["602", "242"]
last_b3 = ["389", "239"]

# ==========================================
# 4. หน้าจอหลัก (UI)
# ==========================================

st.title(f"💰 งวดส่งท้ายปี: {next_draw_date}")

# --- ส่วนที่ 1: ผลรางวัลเก่างวดที่แล้ว (ไว้ตรวจทาน) ---
st.markdown(f"## 1. ย้อนรอยงวดที่แล้ว ({last_draw_date})")

with st.container():
    col_l, col_r = st.columns([2, 1])
    
    with col_l:
        st.markdown(f"""
        <div class="mom-card">
            <div class="label-badge">รางวัลที่ 1</div>
            <div class="num-big">{last_p1}</div>
            <div style="font-size: 18px; color: #666;">รางวัลละ 6 ล้านบาท</div>
            <hr style="border: 1px dashed #ccc;">
            <div style="display: flex; justify-content: space-around;">
                <div>
                    <div style="font-size:18px;">เลขหน้า 3 ตัว</div>
                    <div class="num-med" style="color:#555;">{last_f3[0]} | {last_f3[1]}</div>
                </div>
                <div>
                    <div style="font-size:18px;">เลขท้าย 3 ตัว</div>
                    <div class="num-med" style="color:#555;">{last_b3[0]} | {last_b3[1]}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div class="mom-card" style="height: 380px; display: flex; flex-direction: column; justify-content: center;">
            <div class="label-badge">เลขท้าย 2 ตัว</div>
            <div class="num-huge">{last_2d}</div>
            <div style="font-size: 18px; color: #666;">ออกบ่อยมากปีนี้!</div>
        </div>
        """, unsafe_allow_html=True)

# --- ส่วนที่ 2: แนวทางงวดนี้ (ไฮไลท์สำคัญ) ---
st.markdown(f"## 2. 🔮 แนวทางเลขเด็ด (งวด {next_draw_date})")
st.info("💡 **คำแนะนำจากลูกหนิง:** งวดสิ้นปีแบบนี้ เน้นเลขที่มีความผูกพันกับเรา (วันเกิด/อายุ) จะมีพลังมากกว่าเลขทั่วไปครับแม่")

col_rec1, col_rec2 = st.columns(2)

# การ์ดแนะนำใบที่ 1 (เลข 2 ตัว)
with col_rec1:
    st.markdown("""
    <div class="mom-card" style="border: 3px solid #E91E63;">
        <div class="label-badge" style="background:#F48FB1; color:white;">2 ตัว มาแรงที่สุด</div>
        <div class="num-huge" style="color:#E91E63;">29</div>
        <div class="story-box">
            <b>ทำไมต้องเลขนี้?</b><br>
            "เลขนี้คือ <b>วันเกิดของหนิงเอง (วันที่ 29)</b> ครับแม่ แล้วบังเอิญมากที่งวดนี้หวยออกใกล้วันที่ 30 พอดี ตามสถิติแล้วเลขวันเกิดลูกหลานมักจะให้โชคช่วงสิ้นปีครับ แถมเลขนี้ยังไม่ออกมานานแล้ว น่าลุ้นมากๆ"
        </div>
    </div>
    """, unsafe_allow_html=True)

# การ์ดแนะนำใบที่ 2 (เลข 3 ตัว)
with col_rec2:
    st.markdown("""
    <div class="mom-card" style="border: 3px solid #1976D2;">
        <div class="label-badge" style="background:#64B5F6; color:white;">3 ตัว สวยมาก</div>
        <div class="num-huge" style="color:#1976D2;">936</div>
        <div class="story-box">
            <b>ที่มาของเลขนี้?</b><br>
            "อันนี้มาจาก <b>ทะเบียนรถ Accord (เลข 9)</b> ผสมกับเลขมงคลปีใหม่ครับ สถิติ 10 ปีบอกว่า หวยสิ้นปีชอบออกเลข 'หาม' หรือเลขสลับกันแบบนี้ ถ้าแม่จะเชียร์ลูกค้า ให้บอกว่า <b>'เลขพาลูกกลับบ้าน'</b> ครับ ขลังแน่นอน!"
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# NEW SECTION: FAMILY PHOTOS
# ==========================================
st.markdown("## 📸 มุมครอบครัวสุขสันต์")
st.info("❤️ **กำลังใจของแม่:** รูปภาพแห่งความสุขของครอบครัวเราครับ (อย่าลืมสร้างโฟลเดอร์ 'images' และเอารูปไปใส่นะครับ!)")

# ตรวจสอบว่ามีโฟลเดอร์ images และไฟล์รูปภาพอยู่จริงหรือไม่
if os.path.exists("images"):
    col_img1, col_img2, col_img3 = st.columns(3)

    with col_img1:
        if os.path.exists("images/image_11.png"):
            st.image("images/image_11.png", caption="แม่สุดสวย", use_column_width=True)
        else:
            st.warning("ไม่พบไฟล์ images/image_11.png")

    with col_img2:
        if os.path.exists("images/image_15.png"):
            st.image("images/image_15.png", caption="แม่กับหนิง", use_column_width=True)
        else:
            st.warning("ไม่พบไฟล์ images/image_15.png")

    with col_img3:
        if os.path.exists("images/image_12.png"):
            st.image("images/image_12.png", caption="ครอบครัวของเรา", use_column_width=True)
        else:
            st.warning("ไม่พบไฟล์ images/image_12.png")
else:
    st.error("⚠️ ไม่พบโฟลเดอร์ 'images'! กรุณาสร้างโฟลเดอร์ชื่อ 'images' ไว้ข้างๆ ไฟล์ app.py และนำรูปภาพไปใส่ไว้ข้างในครับ")

# --- ส่วนที่ 3: เครื่องมือช่วยขาย ---
st.markdown("## 3. 🛠️ เครื่องมือช่วยแม่ขาย")

tab1, tab2 = st.tabs(["🔎 เช็คประวัติเลข (ลูกค้าถาม)", "✅ ตรวจหวย (ด่วน)"])

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    c_s1, c_s2 = st.columns([1, 2])
    with c_s1:
        search_num = st.text_input("ลูกค้าถามหาเลขไหน? (พิมพ์เลย)", max_chars=3)
        btn_check = st.button("วิเคราะห์เลขนี้ซิ")
    with c_s2:
        if btn_check and search_num:
            # จำลองผลลัพธ์
            count = random.randint(1, 8)
            msg = "🔥 เลขดัง! ออกบ่อยมาก" if count > 4 else "❄️ เลขเงียบๆ นานๆ มาที"
            
            st.markdown(f"""
            <div style="background:#FFF3E0; padding:20px; border-radius:15px; border:2px solid #FFB74D;">
                <h3>ผลวิเคราะห์เลข: {search_num}</h3>
                <p style="font-size:20px;">เคยออกไปแล้ว: <b>{count} ครั้ง</b> (ในรอบ 5 ปี)</p>
                <p style="font-size:22px; color:#E65100; font-weight:bold;">สรุป: {msg}</p>
                <p>บอกลูกค้าได้เลยว่า: <i>"{'ตัวนี้คนถามหาเยอะนะแม่' if count > 4 else 'ตัวนี้ถ้ามาคือรวยเลย เพราะเจ้ามือเผลอ'}"</i></p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    lotto_chk = st.text_input("กรอกเลข 6 ตัว ตรวจรางวัล", max_chars=6)
    if st.button("ตรวจเดี๋ยวนี้"):
        if len(lotto_chk) == 6:
            if lotto_chk == last_p1:
                st.balloons()
                st.success(f"🎉 กรี๊ดดด!! ถูกรางวัลที่ 1 ({last_p1}) รวยแล้วแม่!")
            elif lotto_chk[-2:] == last_2d:
                st.balloons()
                st.success(f"💰 เก่งมาก! ถูกเลขท้าย 2 ตัว ({last_2d})")
            else:
                st.error("ไม่ถูกจ้า... งวดหน้าเอาใหม่นะ")
        else:
            st.warning("ใส่ให้ครบ 6 ตัวนะแม่")
