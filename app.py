import streamlit as st
import pandas as pd
import plotly.express as px
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# ==========================================
# 1. المـــحرك (THE ENGINE - Logic)
# ==========================================
def run_narmer_engine(dimensions_data):
    """
    هذا هو المحرك الذي كان يفترض أن يكون في API منفصل.
    قمنا بدمجه هنا ليعمل مباشرة.
    """
    weights = {
        "السيادة المالية": 1.5, "المناعة السيبرانية": 1.4,
        "سيادة الذكاء الاصطناعي": 1.3, "القوة العسكرية": 1.2,
        "استقلالية الطاقة": 1.2, "الأمن الغذائي": 1.1
    }
    
    total_weighted_score = 0
    total_weights = 0
    
    for dim, value in dimensions_data.items():
        weight = weights.get(dim, 1.0) # الوزن الافتراضي 1.0 إذا لم يحدد
        total_weighted_score += (value * weight)
        total_weights += weight
        
    v_score = round(total_weighted_score / total_weights, 2)
    return v_score

# ==========================================
# 2. الواجــــهة (THE UI - Streamlit)
# ==========================================
st.set_page_config(page_title="Narmer Sovereign Matrix", layout="wide")

# تصميم الثيم الملكي
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    h1, h2, h3 { color: #c9a050 !important; }
    .stSlider > div > div > div > div { background: #c9a050; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ Narmer Sovereign Immunity Matrix")
st.write("---")

# الحقول الاستراتيجية
dimensions = [
    "السيادة المالية", "المناعة السيبرانية", "القوة العسكرية", 
    "استقلالية الطاقة", "الأمن الغذائي", "الاستقرار الاجتماعي", 
    "الحوكمة والامتثال", "الابتكار"
]

with st.sidebar:
    st.header("🔑 تحكم النظام")
    token = st.text_input("Access Token", type="password")
    st.info("قم بتحريك المؤشرات لتمثيل حالة الدولة السيادية")

if token == "123": # يمكنك تغيير الرقم السري هنا
    cols = st.columns(2)
    input_values = {}
    
    for i, dim in enumerate(dimensions):
        col_idx = i % 2
        input_values[dim] = cols[col_idx].slider(f"{dim}", 0, 100, 70)

    if st.button("🚀 تشغيل محرك الاستنتاج (Execute)"):
        # استدعاء المحرك المدمج
        final_score = run_narmer_engine(input_values)
        
        st.write("---")
        c1, c2 = st.columns([1, 2])
        
        with c1:
            st.metric("مؤشر الحصانة (V-Score)", f"{final_score}%")
            if final_score > 75:
                st.success("حالة السيادة: حصانة مرتفعة")
            else:
                st.warning("حالة السيادة: تعريض استراتيجي")

        with c2:
            # رسم بياني توضيحي
            df = pd.DataFrame(dict(r=list(input_values.values()), theta=list(input_values.keys())))
            fig = px.line_polar(df, r='r', theta='theta', line_close=True)
            fig.update_traces(fill='toself', line_color='#c9a050')
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', polar=dict(bgcolor='#1a1c24'))
            st.plotly_chart(fig)
else:
    st.warning("الرجاء إدخال التوكن الصحيح لفتح لوحة التحكم الاستراتيجية.")
