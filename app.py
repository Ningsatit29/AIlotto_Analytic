import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# 1. CSS SETUP
st.set_page_config(page_title="ระบบวิเคราะห์หวยแม่นๆ", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;700&display=swap');
    
    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Prompt', sans-serif;
        color: #000000 !important; 
    }
    
    h1, h2, h3 { 
        color: #D81B60 !important; 
        font-weight: bold !important;
        text-align: center !important;
    }

    .lotto-container {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .box-pink {
        border: 3px solid #D81B60; 
        border-radius: 20px;
        background-color: #FFFFFF; 
        text-align: center;
        padding: 15px;
        color: #000000 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .label-badge {
        background-color: #D81B60;
        color: white !important;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }
    
    .num-big { font-size: 60px; font-weight: 900; color: #000000 !important; }
    .num-med { font-size: 36px;
