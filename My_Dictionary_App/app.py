import streamlit as st
import os  # Import os to check file existence
from dictionary import get_word_meaning

# Load CSS correctly
def load_css():
    css_file = "style.css"
    if os.path.exists(css_file):  # ✅ Check if file exists
        with open(css_file, "r") as f:
            css_content = f"<style>{f.read()}</style>"
            st.markdown(css_content, unsafe_allow_html=True)
    else:
        st.warning("⚠️ CSS file not found. Using inline styles.")

        # ✅ Fallback inline styles if `style.css` is missing
        st.markdown("""
            <style>
                body {background: linear-gradient(135deg, #4379df, #2a5298); color: white;}
                .title {text-align: center; font-size: 36px; font-weight: bold;}
                .stTextInput > div > div > input {
                    border: 2px solid #4CAF50 !important;
                    border-radius: 10px !important;
                    padding: 12px !important;
                    width: 100% !important;
                    font-size: 18px !important;
                    color: black !important;
                    background-color: white !important;
                }
                .stButton button {
                    background: linear-gradient(90deg, #4CAF50, #45a049) !important;
                    color: white !important;
                    border-radius: 8px !important;
                    padding: 12px 25px !important;
                    border: none !important;
                    font-size: 18px !important;
                    transition: 0.3s ease-in-out !important;
                    cursor: pointer !important;
                }
                .stButton button:hover {
                    background: linear-gradient(90deg, #45a049, #4CAF50) !important;
                    transform: scale(1.05) !important;
                }
                .result-box {
                    background: rgba(255, 255, 255, 0.15);
                    backdrop-filter: blur(10px);
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                    margin-top: 20px;
                    font-size: 18px;
                    text-align: left;
                    color: white;
                    animation: fadeIn 0.5s ease-in-out;
                }
                @keyframes fadeIn {
                    from {opacity: 0; transform: translateY(-10px);}
                    to {opacity: 1; transform: translateY(0);}
                }
            </style>
        """, unsafe_allow_html=True)

# Streamlit App
def main():
    st.set_page_config(page_title="My Dictionary App", page_icon="📖", layout="centered")

    load_css()  # ✅ Load the CSS file safely

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
