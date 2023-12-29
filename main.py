import streamlit as st
import llm

st.title("Text Translator")
language=st.text_input("Enter the Language of Translation")
text=st.text_input("Enter Text to be Translated")

if language and text:
    final=llm.translate(language,text)
    response=final['Translated_text'].strip()
    st.write(response)
    similarity=llm.similarity(response)
    st.write("Accuracy :",similarity)
    #st.write()
