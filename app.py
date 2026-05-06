import streamlit as st
import pandas as pd
import plotly.express as px
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# --- 1. إعدادات الصفحة والهوية البصرية ---
st.set_page_config(
    page_title="Narmer Sovereign Matrix v50.0",
    layout="wide",
    page_icon="🏛️"
)

# تصميم الواجهة الملكية (Dark Mode & Gold Accents)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    [data-testid="stMetricValue"] { color: #c9a050 !important; font-size: 45px; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3em;
        background: linear-gradient(135deg, #8b0000 0%, #b22222 100%);
        color: white; border: none; font-weight: bold;
    }
    h1, h2, h3 { color: #c9a050 !important; font-family: 'Times New Roman', serif; }
    .sidebar .sidebar-content { background-color: #1a1c24; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك الاستنتاج السيادي (The Engine) ---
def calculate_v_score(dims):
    # الأوزان الاستراتيجية (Enterprise Weights)
    weights = {
        "السيادة المالية": 1.5, "المناعة السيبرانية": 1.5,
        "سيادة الذكاء الاصطناعي": 1.4, "القوة العسكرية": 1.3,
        "استقلالية الطاقة": 1.2, "الأمن الغذائي": 1.2
    }
    total_weighted = sum(dims.get(k, 0) * weights.get(k, 1.0) for k in dims)
    total_w = sum(weights.get(k, 1.0) for k in dims)
    return round(total_weighted / total_w, 2)

# --- 3. الشريط الجانبي (Access Control) ---
with st.sidebar:
    st.markdown("### 🔐 Access Control")
    token = st.text_input("Enter System Token", type="password", help="Authorized Personnel Only")
    st.write("---")
    st.info("🏛️ **Security Status:** Encrypted Connection")
    st.caption("Authorized Personnel Only")

# --- 4. الواجهة الرئيسية ---
if token == "NAR-2026": # التوكن الخاص بك
    st.title("🏛️ Narmer Sovereign Immunity Matrix")
    st.subheader("Sovereign Intelligence Control Panel v50.0")
    st.write("---")

    # --- Strategic Parameters (Grid Layout) ---
    st.markdown("### 🎚️ Strategic Parameters")
    
    dimensions = [
        "الحوكمة والامتثال", "البنية التحتية الرقمية", "السيادة المالية",
        "الابتكار", "الاستدامة البيئية", "القوة الناعمة",
        "القوة العسكرية", "سلاسل الإمداد", "استقلالية الطاقة",
        "الدبلوماسية", "السيادة الفضائية", "الأمن الصحي",
        "المناعة السيبرانية", "رأس المال البشري", "الأمن الغذائي",
        "الاستقرار الاجتماعي", "سيادة الذكاء الاصطناعي"
    ]

    input_data = {}
    cols = st.columns(3) # توزيع الأبعاد على 3 أعمدة للتنظيم
    
    for i, dim in enumerate(dimensions):
        with cols[i % 3]:
            input_data[dim] = st.slider(dim, 0, 100, 75, key=dim)

    st.write("---")

    # --- Immunity Assessment (The Results) ---
    if st.button("🛡️ EXECUTE IMMUNITY ASSESSMENT"):
        v_score = calculate_v_score(input_data)
        
        col_res, col_chart = st.columns([1, 2])
        
        with col_res:
            st.markdown("### 🛡️ Assessment Results")
            st.metric("V-Score Index", f"{v_score}%")
            
            if v_score >= 70:
                st.success("Status: High Resilience")
                status_text = "High Resilience"
            elif v_score >= 50:
                st.warning("Status: Moderate Exposure")
                status_text = "Moderate Exposure"
            else:
                st.error("Status: Critical Vulnerability")
                status_text = "Critical Vulnerability"
            
            st.info("Analysis based on Narmer Chronological Investigation Logic.")

        with col_chart:
            # الرسم الراداري
            df = pd.DataFrame(dict(r=list(input_data.values()), theta=list(input_data.keys())))
            fig = px.line_polar(df, r='r', theta='theta', line_close=True)
            fig.update_traces(fill='toself', line_color='#c9a050', fillcolor='rgba(201, 160, 80, 0.2)')
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                polar=dict(bgcolor='#1a1c24', radialaxis=dict(visible=True, range=[0, 100])),
                font_color="#e0e0e0"
            )
            st.plotly_chart(fig, use_container_width=True)

        # --- Executive Archive (PDF Generation) ---
        st.write("---")
        st.markdown("### 🏛️ Executive Archive")
        
        # إنشاء ملف PDF في الذاكرة
        buf = io.BytesIO()
        p = canvas.Canvas(buf, pagesize=A4)
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, 800, "NARMER SOVEREIGN IMMUNITY MATRIX - OFFICIAL REPORT")
        p.setFont("Helvetica", 12)
        p.drawString(50, 770, f"V-Score: {v_score}% | Status: {status_text}")
        p.drawString(50, 750, f"Analyst: Mohamed Ali Youssef")
        p.drawString(50, 730, "Classification: Top Secret")
        p.line(50, 720, 550, 720)
        p.save()
        
        st.download_button(
            label="📥 DOWNLOAD SEALED DOCUMENT",
            data=buf.getvalue(),
            file_name=f"Narmer_v50_Report_{v_score}.pdf",
            mime="application/pdf"
        )
        st.caption("Document Sealed. Signature: M.A.Y")

elif token != "":
    st.error("❌ Invalid System Token. Access Denied.")
else:
    st.warning("🔒 System Locked. Enter Token in Sidebar to Initialize.")
