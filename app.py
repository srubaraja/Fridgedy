import streamlit as st
import random

# Simple Malaysian recipe app
st.set_page_config(page_title="Fridgedy", page_icon="🍳")

st.title("🍳 Fridgedy - AI Recipe Generator")
st.write("Find Malaysian recipes using ingredients you have! 🇲🇾")

# Malaysian recipes database
MALAYSIAN_RECIPES = {
    "chicken": ["🍗 Chicken Curry", "🍗 Ayam Percik", "🍗 Chicken Satay"],
    "rice": ["🍚 Nasi Goreng", "🍚 Nasi Lemak", "🍚 Chicken Rice"],
    "vegetables": ["🥬 Vegetable Stir Fry", "🥬 Mixed Veg Curry", "🥬 Gado-Gado"],
    "fish": ["🐟 Fish Head Curry", "🐟 Ikan Bakar", "🐟 Steamed Fish"],
    "eggs": ["🥚 Egg Fried Rice", "🥚 Telur Dadar", "🥚 Curry Eggs"],
    "beef": ["🥩 Beef Rendang", "🥩 Satay", "🥩 Beef Stir Fry"],
    "prawns": ["🦐 Prawn Curry", "🦐 Sambal Udang", "🦐 Prawn Noodles"],
    "tofu": ["🧈 Tofu Curry", "🧈 Mapo Tofu", "🧈 Fried Tofu"],
    "noodles": ["🍜 Mee Goreng", "🍜 Curry Laksa", "🍜 Hokkien Mee"]
}

# User input
st.subheader("What's in your fridge? 🧊")
ingredients = st.text_input("Type ingredients separated by commas:", placeholder="chicken, rice, vegetables")

if ingredients:
    st.success(f"🎯 Finding Malaysian recipes for: {ingredients}")
    
    # Clean ingredients
    user_ingredients = [ing.strip().lower() for ing in ingredients.split(",")]
    
    found_recipes = []
    
    # Find matching recipes
    for ing in user_ingredients:
        if ing in MALAYSIAN_RECIPES:
            found_recipes.extend(MALAYSIAN_RECIPES[ing])
    
    # Show results
    if found_recipes:
        st.subheader("🍲 Recommended Malaysian Recipes:")
        for recipe in set(found_recipes):  # Remove duplicates
            st.write(f"• {recipe}")
    else:
        st.warning("No specific recipes found. Try: chicken, rice, vegetables, fish, eggs, beef, prawns, tofu, or noodles")
    
    # Special combo suggestions
    st.subheader("🌟 Perfect Combos:")
    if "chicken" in user_ingredients and "rice" in user_ingredients:
        st.write("• **Nasi Lemak** - Coconut rice with chicken")
        st.write("• **Chicken Rice** - Hainanese style")
    
    if "fish" in user_ingredients:
        st.write("• **Ikan Bakar** - Grilled fish with sambal")
    
    if "noodles" in user_ingredients:
        st.write("• **Mee Goreng** - Malaysian fried noodles")

# Future feature placeholder
st.markdown("---")
st.subheader("📸 Coming Soon!")
st.info("AI Photo Analysis: Soon you'll be able to upload fridge photos and AI will automatically identify ingredients! 🚀")

# Footer
st.markdown("---")
st.write("Made with ❤️ for Malaysian families | Powered by Streamlit")
