import streamlit as st

# ==========================================
# 1. ตั้งค่าธีม: ACADEMIC (BLACK & RED)
# ==========================================
st.set_page_config(page_title="Statistical Analysis", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');

    /* พื้นหลังขาว ตัวหนังสือดำ เน้นแดง */
    .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Sarabun', sans-serif !important;
        color: #000000 !important;
    }
    
    header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; }

    /* หัวข้อใหญ่แบบวิชาการ */
    h1 {
        font-size: 50px !important;
        font-weight: 800 !important;
        color: #000000 !important;
        text-align: center;
        border-bottom: 5px solid #D32F2F; /* ขีดเส้นแดง */
        padding-bottom: 20px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }
    
    h2 {
        font-size: 36px !important;
        font-weight: 700 !important;
        color: #D32F2F !important; /* หัวข้อรองสีแดง */
        border-left: 8px solid #000000;
        padding-left: 20px;
        margin-top: 40px;
    }

    /* กรอบข้อความ (Report Box) */
    .report-box {
        border: 3px solid #000000;
        padding: 30px;
        background-color: #FFFFFF;
        margin-bottom: 20px;
    }
    
    /* ตัวเลขเน้นๆ */
    .num-primary {
        font-size: 100px !important;
        font-weight: 900;
        color: #D32F2F; /* แดง */
        text-align: center;
        line-height: 1;
    }
    
    .num-secondary {
        font-size: 60px !important;
        font-weight: 800;
        color: #000000; /* ดำ */
        text-align: center;
    }
    
    /* คำอธิบาย */
    .text-desc {
        font-size: 24px !important;
        color: #333333;
        margin-top: 15px;
        line-height: 1.5;
    }

    /* Input & Button (เหลี่ยมๆ ทางการ) */
    .stTextInput input {
        font-size: 28px !important;
        text-align: center;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        color: #000000 !important;
    }
    .stButton button {
        font-size: 28px !important;
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 0px !important;
        height: 60px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ระบบรหัสผ่าน (SYSTEM ACCESS)
# ==========================================
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<br><br><h1 style='border:none;'>SYSTEM ACCESS REQUIRED</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.markdown("<div class='report-box' style='text-align:center;'>", unsafe_allow_html=True)
        pwd = st.text_input("ENTER SECURITY CODE", type="password")
        if st.button("AUTHENTICATE"):
            if pwd == '06062501': st.session_state.logged_in = True
            else: st.error("ACCESS DENIED")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 3. เนื้อหาหลัก (ONE PAGE REPORT)
# ==========================================
target_date = "30 ธันวาคม 2568"

st.markdown(f"<h1>ANALYTICAL REPORT: {target_date}</h1>", unsafe_allow_html=True)

# --- PART 1: REFERENCE DATA (งวดที่แล้ว) ---
st.markdown("<h2>1. REFERENCE DATA (อ้างอิง: 16 ธ.ค.)</h2>", unsafe_allow_html=True)

c1, c2 = st.columns([2, 1])
with c1:
    st.markdown("""
    <div class="report-box">
        <div style="font-size:30px; font-weight:bold;">รางวัลที่ 1 (1st Prize)</div>
        <div class="num-secondary">458145</div>
        <div class="text-desc">
            <b>3-Digit Prefix:</b> 602, 242<br>
            <b>3-Digit Suffix:</b> 389, 239
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="report-box">
        <div style="font-size:30px; font-weight:bold; text-align:center;">เลขท้าย 2 ตัว</div>
        <div class="num-primary" style="font-size:80px !important;">37</div>
    </div>
    """, unsafe_allow_html=True)

# --- PART 2: PREDICTIVE ANALYSIS (ผลวิเคราะห์) ---
st.markdown("<h2>2. PREDICTIVE ANALYSIS (ผลวิเคราะห์เชิงสถิติ)</h2>", unsafe_allow_html=True)

col_ana1, col_ana2 = st.columns(2)

with col_ana1:
    st.markdown("""
    <div class="report-box" style="border-top: 10px solid #D32F2F;">
        <div style="font-size:32px; font-weight:bold;">SET A: 2-DIGIT</div>
        <div class="num-primary">29</div>
        <div class="text-desc" style="text-align:justify;">
            <b>VARIABLE:</b> Personal Date (วันเกิด)<br>
            <b>LOGIC:</b> ความสัมพันธ์เชิงเวลาระหว่างวันเกิด (29) และวันสิ้นปี (30) มีค่าสหสัมพันธ์ (Correlation) สูงที่สุดในกลุ่มตัวอย่าง
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_ana2:
    st.markdown("""
    <div class="report-box" style="border-top: 10px solid #000000;">
        <div style="font-size:32px; font-weight:bold;">SET B: 3-DIGIT</div>
        <div class="num-primary" style="color:#000000;">936</div>
        <div class="text-desc" style="text-align:justify;">
            <b>VARIABLE:</b> Asset ID (ทะเบียนรถ)<br>
            <b>LOGIC:</b> ปรากฏการณ์ Palindrome Effect (เลขหาม/เลขสลับ) มักเกิดขึ้นบ่อยครั้งในงวดสุดท้ายของปี (Year-End Statistics)
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PART 3: VERIFICATION (เครื่องมือตรวจสอบ) ---
st.markdown("<h2>3. VERIFICATION SYSTEM (ตรวจสอบสถานะ)</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='report-box'>", unsafe_allow_html=True)
    c_check1, c_check2 = st.columns([3, 1])
    
    with c_check1:
        check_num = st.text_input("INPUT 6-DIGIT NUMBER", max_chars=6)
    
    with c_check2:
        st.markdown("<br>", unsafe_allow_html=True)
        btn = st.button("VERIFY")
        
    if btn:
        if check_num == "458145":
            st.success("STATUS: 1ST PRIZE MATCHED (ถูกรางวัลที่ 1)")
        elif check_num and check_num[-2:] == "37":
            st.success("STATUS: 2-DIGIT MATCHED (ถูกเลขท้าย 2 ตัว)")
        else:
            st.error("STATUS: NO MATCH FOUND (ไม่พบข้อมูลการถูกรางวัล)")
    st.markdown("</div>", unsafe_allow_html=True)
