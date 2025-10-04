import streamlit as st

st.set_page_config(page_title="🥗 Smart Nutrition Calculator", layout="wide")

st.title("🥦 Smart Nutrition Calculator")
st.markdown("### Track your meals like a pro — simple, accurate, and fast!")

# --- Food database ---
foods = {
    "Rice (Cooked)": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Egg (Boiled)": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    "Milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Almonds": {"calories": 579, "protein": 21, "fat": 50, "carbs": 22},
}

st.sidebar.header("🍽 Choose Your Food & Quantity")

food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)

if grams > 0:
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    st.success(f"**You selected {grams}g of {food_name}**")
    st.write("Here’s your detailed breakdown:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")
else:
    st.info("👈 Start by choosing a food and entering its weight.")

st.markdown("---")
st.markdown("### 🧠 Tip: Consistency is key! Track your meals daily for best results.")

with st.expander("📖 Add your own note"):
    note = st.text_area("Write down your meal notes or custom recipes:")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a real app, this could be stored locally or in the cloud.)")

st.caption("Built with ❤️ using Streamlit")
