import streamlit as st
import requests

st.title("🍳 Fridgedy - AI Recipe Generator")
st.write("Upload a fridge photo or type ingredients!")

# Simple input
ingredients = st.text_input("What's in your fridge? (e.g., chicken, rice, vegetables)")

if ingredients:
    st.write(f"🥘 Recipe ideas for: {ingredients}")
    st.write("1. **Nasi Goreng** - Fried rice with your ingredients")
    st.write("2. **Curry** - Make a delicious curry")
    st.write("3. **Stir Fry** - Quick and healthy meal")

st.info("More AI features coming soon! 🚀")
