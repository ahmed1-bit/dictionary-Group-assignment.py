# Simple English to Yoruba Dictionarie 
import streamlit as st

st.title("Yoruba Dictionary")

yoruba_dict = {
    "hello": "báwo",
    "good morning": "ẹ káàárọ̀",
    "good afternoon": "ẹ káàsán",
    "good evening": "ẹ káalẹ́",
    "thank you": "ẹ ṣé",
    "yes": "béèni",
    "no": "rárá",
    "food": "oúnjẹ",
    "water": "omi",
    "house": "ilé",
    "school": "ilé-èkó",
    "love": "ìfẹ́",
    "friend": "ọ̀rẹ́",
    "money": "owó",
    "father": "bàbá",
    "mother": "ìyá",
    "child": "ọmọ",
    "come": "wá",
    "go": "lọ",
    "sleep": "sùn"
}

word = st.text_input("Enter your word:").lower().strip()

if st.button("Translate"):
    if word:
        if word in yoruba_dict:
            st.success(f"Yoruba translation: **{yoruba_dict[word]}**")
        else:
            st.error("Word not found 😕")
