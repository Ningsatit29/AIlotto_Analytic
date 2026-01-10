import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime
import time

# ==========================================
# 1. SETUP: NEWS PORTAL THEME
# ==========================================
st.set_page_config(page_title="คัมภีร์วิถีรวย (Lotto Guru)", layout="wide", page_icon="📰")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700&display=swap');

    /* Theme: Green Thairath Style & Clean White */
    .stApp { background-color: #F4F6F9 !important; font-family: 'Prompt', sans-serif; color: #333; }
    
    header {visibility: hidden;}
    .block-container { padding-top: 1rem !important; max-width: 1200px !important;}

    /* HEADER */
    .site-header {
        background: linear-gradient(90deg, #009688 0%, #004D40 100%);
        color: white;
        padding: 20px;
        border-radius: 0 0 15px 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .site-title { font-size: 36px; font-weight: 800; margin: 0; }
    .site-subtitle { font-size: 18px; opacity: 0.9; }

    /* NEWS CARD (เหมือนเว็บข่าว) */
    .news-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s;
        height: 100%;
        border: 1px solid #eee;
    }
    .news-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        border-color: #009688;
    }
    .news-img-box {
        height: 180px;
        background-color: #eee;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .news-img { width: 100%; height: 100%; object-fit: cover; }
    .news-content { padding: 15px; }
    .news-source { 
        font-size: 12px; 
        font-weight: bold; 
        color: #009688; 
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .news-title {
        font-size: 18px;
        font-weight: 700;
        line-height: 1.4;
        margin-bottom: 10px;
        color: #222;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .news-date { font-size: 12px; color: #888; }
    .read-more {
        display: block;
        margin-top: 10px;
        text-align: right;
        font-size: 14px;
        color: #009688;
        text-decoration: none;
        font-weight: bold;
    }

    /* GURU SECTION SIDEBAR */
    .guru-card {
        background: #fff;
        border-top: 5px solid #D32F2F;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .guru-badge {
        background: #D32F2F;
        color: white;
        padding: 5px 10px;
        font-size: 12px;
        border-radius: 4px;
        font-weight: bold;
    }
    .guru-num { font-size: 48px; font-weight: 900; color: #D32F2F; text-align: center; }

    /* LATEST RESULT BAR */
    .result-bar {
        background: #212121;
        color: #FFD700;
        padding: 15px;
        border-radius: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. FUNCTION: FETCH REAL NEWS (RSS)
# ==========================================
@st.cache_data(ttl=3600) # เก็บข้อมูลไว้ 1 ชม. ไม่โหลดบ่อย
def fetch_lotto_news():
    # RSS Feed จริงของไทยรัฐและ Sanook (หมวดหวย/ข่าวทั่วไป)
    rss_urls = [
        "https://www.thairath.co.th/rss/news/local", # ไทยรัฐทั่วไทย (มักมีข่าวหวย)
        "https://rss.sanook.com/rss/latest", # สนุก ล่าสุด
    ]
    
    news_items = []
    
    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:4]: # เอาแค่ 4 ข่าวต่อเว็บ
                # พยายามหาคำว่า "หวย", "เลขเด็ด", "สลาก" ในหัวข้อ
                if any(x in entry.title for x in ['หวย', 'เลข', 'สลาก', 'รางวัล', 'แก้บน', 'คำชะโนด']):
                    
                    # หาภาพประกอบ (RSS บางทีซ่อนภาพไว้ลึก)
                    img_url = "https://via.placeholder.com/400x200?text=Lotto+News"
                    if 'media_content' in entry:
                        img_url = entry.media_content[0]['url']
                    elif 'links' in entry:
                        for link in entry.links:
                            if link.type == 'image/jpeg':
                                img_url = link.href
                                break
                    
                    news_items.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': entry.published if 'published' in entry else str(datetime.now().date()),
                        'source': 'THAIRATH' if 'thairath' in url else 'SANOOK',
                        'image': img_url
                    })
        except:
            pass
            
    # ถ้าหาข่าวไม่ได้เลย (หรือไม่มีเน็ต) ให้ใช้ Mock Data สวยๆ แทน
    if not news_items:
        news_items = [
            {
                'title': "โค้งสุดท้าย! เลขเด็ด 'คำชะโนด' มาแรง คอหวยแห่ส่องขันน้ำมนต์",
                'link': '#',
                'published': 'วันนี้ 10:30',
                'source': 'THAIRATH',
                'image': 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
            },
            {
                'title': "หนุ่มดวงเฮง ถูกรางวัลที่ 1 เผยที่มาเลขความฝัน เห็นปู่พญานาค",
                'link': '#',
                'published': 'เมื่อวาน 18:45',
                'source': 'SANOOK',
                'image': 'https://images.unsplash.com/photo-1518688248740-759786498362?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
            },
            {
                'title': "สถิติหวยออกวันศุกร์ ย้อนหลัง 10 ปี พบเลขเบิ้ลออกบ่อยมาก",
                'link': '#',
                'published': 'วันนี้ 08:15',
                'source': 'MATICHON',
                'image': 'https://images.unsplash.com/photo-1614026480209-cd9934144671?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
            },
             {
                'title': "ฮือฮา! งูเหลือมยักษ์เลื้อยเข้าบ้านเลขที่ 936 เจ้าของเชื่อมาให้โชค",
                'link': '#',
                'published': 'วันนี้ 12:00',
                'source': 'KHAOSOD',
                'image': 'https://images.unsplash.com/photo-1531384441138-2736e62e0919?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
            }
        ]
        
    return news_items

# ==========================================
# 3. LAYOUT & CONTENT
# ==========================================

# --- HEADER ---
st.markdown("""
<div class="site-header">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <h1 class="site-title">📰 คัมภีร์วิถีรวย (Lotto Guru)</h1>
            <div class="site-subtitle">ศูนย์รวมข่าวหวย สถิติ และแนวทางเลขเด็ดที่แม่นที่สุด</div>
        </div>
        <div style="text-align:right;">
            <div style="font-size:14px; opacity:0.8;">งวดประจำวันที่</div>
            <div style="font-size:24px; font-weight:bold;">30 ธันวาคม 2568</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- MAIN GRID ---
col_main, col_sidebar = st.columns([2.5, 1], gap="large")

with col_main:
    # 1. Latest Result Banner
    st.markdown("""
    <div class="result-bar">
        <div>
            <span style="background:#D32F2F; color:white; padding:5px 10px; border-radius:5px; font-weight:bold; margin-right:10px;">ล่าสุด</span>
            ผลรางวัลที่ 1 งวด 16 ธ.ค. : 
        </div>
        <div style="font-size:32px; font-weight:900; letter-spacing:2px;">458145</div>
        <div style="font-size:14px; color:#ccc;">(เลขท้าย 2 ตัว: 37)</div>
    </div>
    """, unsafe_allow_html=True)

    # 2. News Feed Grid
    st.markdown("### 🔥 ข่าวเลขเด็ด ล่าสุด (Breaking News)")
    
    news_data = fetch_lotto_news()
    
    # จัดเรียงข่าวเป็น Grid (แถวละ 3 ข่าว)
    rows = [news_data[i:i + 3] for i in range(0, len(news_data), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for i, news in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                <div class="news-card">
                    <div class="news-img-box">
                        <img src="{news['image']}" class="news-img">
                    </div>
                    <div class="news-content">
                        <div class="news-source">{news['source']} • {news['published']}</div>
                        <div class="news-title">{news['title']}</div>
                        <a href="{news['link']}" target="_blank" class="read-more">อ่านต่อ ></a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
    st.markdown("<br><button style='width:100%; padding:10px; border:none; background:#eee; cursor:pointer;'>โหลดข่าวเพิ่มเติม...</button>", unsafe_allow_html=True)

# --- SIDEBAR (GURU & STATS) ---
with col_sidebar:
    # Guru Profile
    st.markdown("""
    <div class="guru-card">
        <div style="display:flex; align-items:center; margin-bottom:15px;">
            <div style="width:60px; height:60px; background:#ddd; border-radius:50%; overflow:hidden; margin-right:15px;">
                <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Ning" width="100%">
            </div>
            <div>
                <div style="font-weight:bold; font-size:18px;">อ.หนิง พาปัง</div>
                <div style="font-size:12px; color:gray;">นักวิเคราะห์ตัวเลขมือหนึ่ง</div>
            </div>
        </div>
        <div style="margin-bottom:15px;">
            <span class="guru-badge">ฟันธงงวดนี้</span>
            <div style="font-size:14px; color:#555; margin-top:5px;">"งวดส่งท้ายปี วันเกิดผมเอง 29 มาแน่ครับแม่!"</div>
        </div>
        <div class="guru-num">29</div>
        <div style="text-align:center; color:#888; font-size:12px;">ความมั่นใจ 99%</div>
        <hr>
        <div style="margin-bottom:5px;">
            <span class="guru-badge" style="background:#1976D2;">เลขชุด 3 ตัว</span>
        </div>
        <div class="guru-num" style="color:#1976D2; font-size:36px;">936</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Check
    st.markdown("""
    <div class="guru-card" style="border-top-color: #388E3C;">
        <h4>🔎 ตรวจหวยด่วน</h4>
        <p style="font-size:14px; color:#666;">กรอกเลข 6 หลัก เพื่อตรวจรางวัลย้อนหลัง</p>
    </div>
    """, unsafe_allow_html=True)
    
    check_num = st.text_input("เลขสลาก", label_visibility="collapsed")
    if st.button("ตรวจรางวัล", type="primary", use_container_width=True):
        if check_num == "458145":
            st.success("🎉 ยินดีด้วย! ถูกรางวัลที่ 1")
        else:
            st.error("เสียใจด้วยครับ ยังไม่ถูกรางวัล")

    # Stats List
    st.markdown("#### 📊 สถิติเลขท้าย 2 ตัว (ปี 68)")
    st.dataframe(
        pd.DataFrame({
            'งวดวันที่': ['16 ธ.ค.', '1 ธ.ค.', '16 พ.ย.', '1 พ.ย.'],
            'เลขที่ออก': ['37', '89', '44', '09']
        }),
        hide_index=True,
        use_container_width=True
    )
