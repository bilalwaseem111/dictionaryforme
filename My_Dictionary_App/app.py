import streamlit as st
import os
from dictionary import get_word_meaning

# Load CSS correctly
def load_css():
    css_file = "style.css"
    if os.path.exists(css_file):  # Check if file exists
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(" Using styles.")



# Streamlit App
def main():
    st.set_page_config(page_title="My Dictionary App", page_icon="📖", layout="centered")

    load_css()

    st.markdown("<h1 class='title'>📖 My Global Dictionary</h1>", unsafe_allow_html=True)

    word = st.text_input("🔍 Enter a word:")

    if st.button("Search Meaning 🚀"):
        if word.strip():
            meanings = get_word_meaning(word.strip())

            st.markdown('<div class="result-box">', unsafe_allow_html=True)

            for meaning in meanings:
                st.markdown(f"✅ {meaning}")

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a valid word.")

if __name__ == "__main__":
    main()
