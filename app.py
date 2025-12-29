import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# ==========================================
# 1. SETUP & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Lotto AI - ผู้ช่วยแม่ค้าลอตเตอรี่",
    page_icon="🎰",
    layout="wide"
)

st.markdown("""
<style>
    .big-font { font-size:24px !important; font-weight: bold; }
    .win-text { color: #2e7d32; font-weight: bold; font-size: 20px; }
    .loss-text { color: #c62828; font-weight: bold; font-size: 20px; }
    .stButton>button { width: 100%; border-radius: 20px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA GENERATION (จำลองข้อมูล)
# ==========================================
@st.cache_data
def load_data():
    dates = pd.date_range(end=datetime.now(), periods=120, freq='SM') 
    data = []
    
    for date in dates:
        # จำลองเลขรางวัล (เปลี่ยนตรงนี้เป็นเลขจริงได้ถ้าขยัน)
        prize_1 = f"{random.randint(0, 999999):06d}"
        digit_2 = f"{random.randint(0, 99):02d}"
        
        # 3 ตัวหน้า 2 ชุด, 3 ตัวหลัง 2 ชุด
        f3_1 = f"{random.randint(0, 999):03d}"
        f3_2 = f"{random.randint(0, 999):03d}"
        b3_1 = f"{random.randint(0, 999):03d}"
        b3_2 = f"{random.randint(0, 999):03d}"
        
        data.append({
            'date': date,
            'day': date.day,
            'month': date.month,
            'year': date.year + 543,
            'prize_1': prize_1,
            'digit_2': digit_2,
            'front_3': [f3_1, f3_2],
            'back_3': [b3_1, b3_2]
        })
    
    df = pd.DataFrame(data)
    df = df.sort_values(by='date', ascending=False).reset_index(drop=True)
    return df

df = load_data()

# ==========================================
# 3. ANALYSIS & CHECK LOGIC
# ==========================================
def analyze_number_logic(number, df):
    score = 50 
    insights = []
    num_str = str(number)
    
    # Check Frequency
    if len(num_str) == 2:
        count = df[df['digit_2'] == num_str].shape[0]
    else:
        count = df[df['prize_1'].str.endswith(num_str)].shape[0]
        
    if count > 3:
        score += 20
        insights.append(f"🔥 มาแรง: ออกแล้ว {count} ครั้ง")
    elif count > 0:
        score += 10
        insights.append(f"✅ เคยมีประวัติ: ออก {count} ครั้ง")
    else:
        score -= 10
        insights.append(f"❄️ หายาก: ไม่ค่อยเห็นเลขนี้")

    if num_str[0] == num_str[-1]:
        score += 5
        insights.append(f"✨ เลขเบิ้ล: สวยน่าลุ้น")
    
    return min(99, score), insights

def check_lotto_prize(lottery_num, latest_row):
    results = []
    is_win = False
    
    # ตรวจรางวัลที่ 1
    if lottery_num == latest_row['prize_1']:
        results.append(f"🎉 ถูกรางวัลที่ 1! ({latest_row['prize_1']})")
        is_win = True
        
    # ตรวจเลขท้าย 2 ตัว
    if lottery_num[-2:] == latest_row['digit_2']:
        results.append(f"💰 ถูกเลขท้าย 2 ตัว! ({latest_row['digit_2']})")
        is_win = True
        
    # ตรวจเลขหน้า 3 ตัว (ต้องมีครบ 6 หลักถึงตรวจได้)
    if len(lottery_num) == 6:
        front_3_check = lottery_num[:3]
        if front_3_check in latest_row['front_3']:
            results.append(f"💵 ถูกเลขหน้า 3 ตัว! ({front_3_check})")
            is_win = True
            
    # ตรวจเลขท้าย 3 ตัว (ต้องมีครบ 6 หลัก หรือ กรอกมาแค่ 3 ตัว)
    last_3_check = lottery_num[-3:]
    if last_3_check in latest_row['back_3']:
        results.append(f"💵 ถูกเลขท้าย 3 ตัว! ({last_3_check})")
        is_win = True
        
    return is_win, results

# ==========================================
# 4. USER INTERFACE
# ==========================================

st.title("🐯 Lotto AI Analyst (ระบบช่วยแม่ขาย)")
st.caption(f"อัปเดตล่าสุด: {datetime.now().strftime('%d/%m/%Y')} | พัฒนาโดย: ลูกหนิง")

# Tab Menu
tab1, tab2, tab3, tab4 = st.tabs(["🏠 แผงควบคุม", "🔍 วิเคราะห์", "✅ ตรวจหวย", "📜 สถิติ"])

# --- TAB 1: DASHBOARD ---
with tab1:
    latest = df.iloc[0]
    st.info(f"📅 **ผลงวดล่าสุด ({latest['day']}/{latest['month']}/{latest['year']})**")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("🏆 รางวัลที่ 1", latest['prize_1'])
        st.metric("เลขท้าย 2 ตัว", latest['digit_2'])
    with c2:
        st.write("เลขหน้า 3 ตัว:")
        st.code(f"{latest['front_3'][0]} | {latest['front_3'][1]}")
        st.write("เลขท้าย 3 ตัว:")
        st.code(f"{latest['back_3'][0]} | {latest['back_3'][1]}")

# --- TAB 2: ANALYZER ---
with tab2:
    st.markdown("### 🔮 ถาม AI: เลขนี้สวยไหม?")
    user_num = st.text_input("พิมพ์เลขที่ลูกค้าอยากซื้อ", max_chars=3)
    if user_num and user_num.isdigit():
        score, insights = analyze_number_logic(user_num, df)
        col_res1, col_res2 = st.columns([1, 2])
        with col_res1:
            st.radial_chart = st.progress(score)
            st.metric("คะแนนความสวย", f"{score}/100")
        with col_res2:
            for text in insights:
                st.write(text)

# --- TAB 3: CHECK LOTTERY (NEW!) ---
with tab3:
    st.markdown("### ✅ ตรวจสลากฯ (งวดล่าสุด)")
    lotto_input = st.text_input("กรอกเลขลอตเตอรี่ 6 หลัก", max_chars=6)
    
    if st.button("ตรวจรางวัลเดี๋ยวนี้"):
        if len(lotto_input) < 3:
            st.error("กรุณากรอกเลขอย่างน้อย 3 ตัวครับ")
        else:
            is_win, prize_list = check_lotto_prize(lotto_input, df.iloc[0])
            
            st.divider()
            if is_win:
                st.balloons() # เอฟเฟกต์ลูกโป่ง!
                st.success("🎉 ยินดีด้วยครับ! คุณถูกรางวัล")
                for p in prize_list:
                    st.markdown(f"### {p}")
            else:
                st.error("เสียใจด้วยครับ ไม่ถูกรางวัล")
                st.write(f"งวดนี้ออก: รางวัลที่ 1 [{df.iloc[0]['prize_1']}] | เลขท้าย [{df.iloc[0]['digit_2']}]")
                st.caption("ไม่เป็นไรนะ งวดหน้าเอาใหม่!")

# --- TAB 4: HISTORY ---
with tab4:
    st.dataframe(df[['date', 'prize_1', 'digit_2']])
