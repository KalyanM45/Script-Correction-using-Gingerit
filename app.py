import streamlit as st
from gingerit.gingerit import GingerIt
st.title("Script Correction")
text  = st.text_input("Enter Your Script")

if st.button("Refine"):
    if text:
        corrected_text = GingerIt().parse(text)
        st.success(corrected_text['result'])
    else:
        st.warning("No Script Written")

