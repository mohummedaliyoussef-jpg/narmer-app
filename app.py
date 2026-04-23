import streamlit as st

st.set_page_config(page_title="Narmer Test", page_icon="🔱")
st.title("🔱 NARMER SOVEREIGN MATRIX - Test Deployment")

with st.sidebar:
    pwd = st.text_input("رمز الوصول", type="password")
    if pwd != "NARMER-2026":
        st.stop()
    st.success("✅ اتصال ناجح")

st.header("تم النشر بنجاح!")
st.write("هذا إثبات أن منصة Streamlit Cloud تعمل مع مستودعك.")
st.info("الخطوة التالية هي نشر النسخة الكاملة مع Falcon AI و OSCAL.")
