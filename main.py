import streamlit as st
import llm

st.title("Text Translator")
language=st.text_input("Enter the Language of Translation")
text=st.text_input("Enter Text to be Translated")

if language:
    final=llm.translate(language,text)
    st.write(final['Translated_text'].strip())
    