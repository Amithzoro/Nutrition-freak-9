import streamlit as st

st.set_page_config(page_title="🥗 Smart Nutrition Calculator", layout="wide")

st.title("🥦 Smart Nutrition Calculator")
st.markdown("### Track your meals like a pro — simple, accurate, and fast!")

# --- Food database with cooking types & recipes ---
foods = {
    "Rice": {
        "types": {
            "Boiled": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
            "Fried": {"calories": 180, "protein": 3.5, "fat": 4.0, "carbs": 30},
            "Steamed": {"calories": 120, "protein": 2.5, "fat": 0.2, "carbs": 26},
        },
        "recipes": [
            "🍛 Veg Fried Rice (Text): Rice, mixed veggies, soy sauce, olive oil.",
            "🍋 Lemon Rice (Text): Rice, lemon juice, turmeric, curry leaves.",
            "🍚 Steamed Rice with Dal (Text): Rice with yellow lentils and ghee.",
            "🥦 Rice Bowl (Text): Rice, broccoli, tofu, soy dressing.",
            "▶️ Watch: [Fried Rice Recipe](https://www.youtube.com/watch?v=4hG_NvF7pXY)",
            "▶️ Watch: [Lemon Rice Recipe](https://www.youtube.com/watch?v=l3ZB8LzQd2M)",
        ]
    },
    "Chicken Breast": {
        "types": {
            "Grilled": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
            "Boiled": {"calories": 150, "protein": 28, "fat": 3.0, "carbs": 0},
            "Fried": {"calories": 220, "protein": 26, "fat": 11, "carbs": 2},
        },
        "recipes": [
            "🍗 Grilled Chicken (Text): Marinated with olive oil, lemon, and herbs.",
            "🍛 Chicken Curry (Text): Chicken, tomato gravy, and spices.",
            "🥗 Chicken Salad (Text): Grilled chicken, lettuce, cucumber, olive dressing.",
            "🌮 Chicken Wrap (Text): Chicken breast, veggies, and flatbread.",
            "▶️ Watch: [Grilled Chicken Recipe](https://www.youtube.com/watch?v=4CjP5v1E5Ew)",
            "▶️ Watch: [Chicken Curry Recipe](https://www.youtube.com/watch?v=HC8wWZ7bU1Q)",
        ]
    },
    "Egg": {
        "sizes": {
            "Small": {"calories": 54, "protein": 4.7, "fat": 3.6, "carbs": 0.3},
            "Medium": {"calories": 68, "protein": 6.3, "fat": 4.8, "carbs": 0.4},
            "Large": {"calories": 78, "protein": 6.8, "fat": 5.3, "carbs": 0.6},
        },
        "types": {
            "Boiled": 1.0,
            "Scrambled": 1.1,
            "Fried": 1.25,
            "Omelette": 1.2
        },
        "recipes": [
            "🥚 Egg Sandwich (Text): Boiled eggs, lettuce, tomato, bread.",
            "🍳 Scrambled Eggs (Text): Beaten eggs cooked in butter.",
            "🌶 Masala Egg (Text): Boiled eggs sautéed with onions, tomatoes, and chili.",
            "🥗 Egg Salad (Text): Eggs, Greek yogurt, mustard, pepper.",
            "🍞 Egg Toast (Text): Egg mixture on toasted bread.",
            "▶️ Watch: [Egg Sandwich Recipe](https://www.youtube.com/watch?v=zR0RdkM-AxI)",
            "▶️ Watch: [Masala Egg Recipe](https://www.youtube.com/watch?v=ts53VQyRhDU)",
        ]
    },
    "Paneer": {
        "types": {
            "Raw": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
            "Grilled": {"calories": 280, "protein": 20, "fat": 22, "carbs": 3},
            "Fried": {"calories": 320, "protein": 21, "fat": 26, "carbs": 4},
        },
        "recipes": [
            "🧀 Paneer Bhurji (Text): Crumbled paneer with onion, tomato & spices.",
            "🍢 Paneer Tikka (Text): Marinated paneer grilled with capsicum.",
            "🥘 Paneer Curry (Text): Paneer cubes in tomato gravy.",
            "🥗 Paneer Salad (Text): Paneer with cucumber and herbs.",
            "▶️ Watch: [Paneer Bhurji Recipe](https://www.youtube.com/watch?v=g0o6tR3Yv9Y)",
            "▶️ Watch: [Paneer Tikka Recipe](https://www.youtube.com/watch?v=fxX4O5UO4jY)",
        ]
    },
    "Oats": {
        "types": {
            "Raw": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
            "Cooked": {"calories": 70, "protein": 2.4, "fat": 1.4, "carbs": 12},
        },
        "recipes": [
            "🥣 Oatmeal Bowl (Text): Oats, milk, banana, chia seeds.",
            "🍪 Oat Cookies (Text): Oats, peanut butter, honey.",
            "🥛 Oat Smoothie (Text): Oats, milk, apple, and cinnamon.",
            "🥥 Coconut Oats (Text): Oats cooked with coconut milk and raisins.",
            "▶️ Watch: [Oatmeal Recipe](https://www.youtube.com/watch?v=Q4x-9XoeV2Y)",
        ]
    },
}

# --- Sidebar ---
st.sidebar.header("🍽 Choose Your Food & Quantity")

food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))

# --- Conditional options ---
if food_name == "Egg":
    egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
    egg_style = st.sidebar.selectbox("Cooking type:", list(foods["Egg"]["types"].keys()))
    egg_count = st.sidebar.number_input("Number of eggs:", min_value=1, max_value=100, value=1)
else:
    cook_type = st.sidebar.selectbox("Select cooking type:", list(foods[food_name]["types"].keys()))
    grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)

# --- Submit Button ---
submit = st.sidebar.button("✅ Submit")

if submit:
    st.markdown("---")

    if food_name == "Egg":
        base = foods["Egg"]["sizes"][egg_size]
        multiplier = foods["Egg"]["types"][egg_style]
        calories = base["calories"] * egg_count * multiplier
        protein = base["protein"] * egg_count
        fat = base["fat"] * egg_count * multiplier
        carbs = base["carbs"] * egg_count
        st.success(f"**You selected {egg_count} {egg_size.lower()} {egg_style.lower()} egg(s)**")

    else:
        info = foods[food_name]["types"][cook_type]
        calories = info["calories"] * grams / 100
        protein = info["protein"] * grams / 100
        fat = info["fat"] * grams / 100
        carbs = info["carbs"] * grams / 100
        st.success(f"**You selected {grams}g of {cook_type.lower()} {food_name.lower()}**")

    # --- Nutrition summary ---
    st.write("Here’s your detailed breakdown:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # --- Recipes ---
    st.markdown("---")
    st.markdown("### 🍽 Recipe Suggestions")
    for recipe in foods[food_name].get("recipes", []):
        st.markdown(f"- {recipe}")

else:
    st.info("👈 Choose your food, cooking type, and quantity — then click **Submit**!")

# --- Notes section ---
st.markdown("---")
st.markdown("### 🧠 Tip: Consistency is key! Track your meals daily for best results.")
with st.expander("📖 Add your own note"):
    note = st.text_area("Write down your meal notes or custom recipes:")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a real app, this could be stored locally or in the cloud.)")

st.caption("Built with ❤️ using Streamlit")
