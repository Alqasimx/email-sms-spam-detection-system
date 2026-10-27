"""
Streamlit UI for the Email/SMS Spam Detection system.

Usage:
    streamlit run app.py
"""

import streamlit as st

# ---------- Page configuration ----------
st.set_page_config(
    page_title="Email / SMS Spam Detector",
    page_icon="📧",
    layout="centered",
)

# ---------- Hide Streamlit default UI (optional) ----------
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# ---------- Lazy-import model ----------
from predict import predict  # noqa: E402

# ---------- Sidebar ----------
with st.sidebar:
    st.title("ℹ️ About")

    st.markdown(
        """
        This application uses a **Machine-Learning model** to classify
        email or SMS messages as **Spam** or **Ham (not spam)**.

        **Stack:** Streamlit · scikit-learn · NLTK

        **How it works:**
        1. Text is cleaned and tokenized.
        2. TF-IDF converts text into numerical features.
        3. ML model predicts spam or ham with confidence score.
        """
    )

    # 👇 نص بسيط فقط بدون تنسيق HTML
    st.success("👨‍🎓 Developed by Cybersecurity Students – University of Science and Technology")

    st.divider()
    st.caption("Built for production-readiness 🚀")

# ---------- Main UI ----------
st.title("📧 Email / SMS Spam Detector")

# 👇 نص بسيط في الصفحة الرئيسية
st.markdown("👨‍🎓 Developed by Cybersecurity Students – University of Science and Technology")

st.markdown(
    "Enter an email or SMS message below and click **Predict** to check if it is spam."
)

input_text = st.text_area(
    "Message",
    height=180,
    placeholder="Type or paste the message here …",
)

# ---------- Prediction ----------
if st.button("🔍 Predict", use_container_width=True):

    if not input_text or not input_text.strip():
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        try:
            result = predict(input_text)
            label = result["label"]
            confidence = result["confidence"]

            if label == "spam":
                st.error("🚨 SPAM detected!")
            else:
                st.success("✅ This message looks safe (Ham).")

            st.markdown(f"**Confidence:** {confidence:.1%}")
            st.progress(confidence)

        except ValueError as exc:
            st.warning(f"⚠️ {exc}")
        except Exception as exc:
            st.error(f"❌ Unexpected error: {exc}")