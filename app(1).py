import streamlit as st

st.set_page_config(page_title="🥗 Smart Nutrition Calculator", layout="wide")

st.title("🥦 Smart Nutrition Calculator")
st.markdown("### Track your meals like a pro — simple, accurate, and fast!")

# --- Food database with recipes (text + YouTube links) ---
foods = {
    "Rice (Cooked)": {
        "calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28,
        "recipes": [
            "🍛 Veg Fried Rice (Text): Cooked rice, mixed veggies, soy sauce, olive oil.",
            "▶️ Watch: [Veg Fried Rice Recipe](https://www.youtube.com/watch?v=4hG_NvF7pXY)"
        ]
    },
    "Chicken Breast": {
        "calories": 165, "protein": 31, "fat": 3.6, "carbs": 0,
        "recipes": [
            "🍗 Grilled Chicken (Text): Marinated chicken with olive oil and herbs.",
            "▶️ Watch: [Grilled Chicken Recipe](https://www.youtube.com/watch?v=4CjP5v1E5Ew)"
        ]
    },
    "Egg (Boiled)": {
        "sizes": {
            "Small": {"calories": 54, "protein": 4.7, "fat": 3.6, "carbs": 0.3},
            "Medium": {"calories": 68, "protein": 6.3, "fat": 4.8, "carbs": 0.4},
            "Large": {"calories": 78, "protein": 6.8, "fat": 5.3, "carbs": 0.6},
        },
        "recipes": [
            "🥚 Egg Sandwich (Text): Boiled eggs, lettuce, tomato, bread.",
            "▶️ Watch: [Boiled Egg Sandwich Recipe](https://www.youtube.com/watch?v=zR0RdkM-AxI)"
        ]
    },
    "Paneer": {
        "calories": 265, "protein": 18, "fat": 21, "carbs": 2.4,
        "recipes": [
            "🧀 Paneer Bhurji (Text): Crumbled paneer with onions, tomatoes & spices.",
            "▶️ Watch: [Paneer Bhurji Recipe](https://www.youtube.com/watch?v=g0o6tR3Yv9Y)"
        ]
    },
    "Banana": {
        "calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23,
        "recipes": [
            "🍌 Banana Smoothie (Text): Banana, milk, oats, honey.",
            "▶️ Watch: [Banana Smoothie Recipe](https://www.youtube.com/watch?v=Qq_QWsdAsyA)"
        ]
    },
    "Milk": {
        "calories": 42, "protein": 3.4, "fat": 1, "carbs": 5,
        "recipes": [
            "🥛 Chocolate Milk (Text): Milk, cocoa powder, and honey.",
            "▶️ Watch: [Chocolate Milk Recipe](https://www.youtube.com/watch?v=4Xn8H6f1cLQ)"
        ]
    },
    "Oats": {
        "calories": 389, "protein": 17, "fat": 7, "carbs": 66,
        "recipes": [
            "🥣 Oatmeal Bowl (Text): Oats, milk, banana, chia seeds.",
            "▶️ Watch: [Oatmeal Bowl Recipe](https://www.youtube.com/watch?v=Q4x-9XoeV2Y)"
        ]
    },
    "Apple": {
        "calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14,
        "recipes": [
            "🍏 Apple Smoothie (Text): Apple, yogurt, honey, cinnamon.",
            "▶️ Watch: [Apple Smoothie Recipe](https://www.youtube.com/watch?v=r1TtL7aZPGo)"
        ]
    },
    "Fish (Grilled)": {
        "calories": 206, "protein": 22, "fat": 12, "carbs": 0,
        "recipes": [
            "🐟 Lemon Garlic Fish (Text): Grilled fish with lemon and herbs.",
            "▶️ Watch: [Grilled Fish Recipe](https://www.youtube.com/watch?v=VQrfG2l_UwE)"
        ]
    },
    "Almonds": {
        "calories": 579, "protein": 21, "fat": 50, "carbs": 22,
        "recipes": [
            "🥜 Almond Smoothie (Text): Almonds, milk, oats, banana.",
            "▶️ Watch: [Almond Smoothie Recipe](https://www.youtube.com/watch?v=7fP6xCC4C8k)"
        ]
    },
}

# --- Sidebar ---
st.sidebar.header("🍽 Choose Your Food & Quantity")

food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))

# --- Input fields based on food type ---
if food_name == "Egg (Boiled)":
    egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
    egg_count = st.sidebar.number_input("Enter number of eggs:", min_value=1, max_value=100, value=1)
else:
    grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)

# --- Submit Button ---
submit = st.sidebar.button("✅ Submit")

if submit:
    st.markdown("---")
    if food_name == "Egg (Boiled)":
        egg_info = foods["Egg (Boiled)"]["sizes"][egg_size]
        calories = egg_info["calories"] * egg_count
        protein = egg_info["protein"] * egg_count
        fat = egg_info["fat"] * egg_count
        carbs = egg_info["carbs"] * egg_count
        st.success(f"**You selected {egg_count} {egg_size.lower()} egg(s)**")
    else:
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

    # --- Recipes Section ---
    st.markdown("---")
    st.markdown("### 🍽 Recipe Suggestions")
    for recipe in foods[food_name].get("recipes", []):
        st.markdown(f"- {recipe}")

else:
    st.info("👈 Choose your food, enter quantity, and click **Submit** to see nutrition info!")

# --- Notes Section ---
st.markdown("---")
st.markdown("### 🧠 Tip: Consistency is key! Track your meals daily for best results.")
with st.expander("📖 Add your own note"):
    note = st.text_area("Write down your meal notes or custom recipes:")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a real app, this could be stored locally or in the cloud.)")

st.caption("Built with ❤️ using Streamlit")
