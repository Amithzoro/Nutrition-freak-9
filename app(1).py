import streamlit as st

st.set_page_config(page_title="🥗 Smart Nutrition Calculator", layout="wide")

st.title("🥦 Smart Nutrition Calculator")
st.markdown("### Track your meals like a pro — simple, accurate, and fast!")

# --- Food database with cooking types, recipes & instructions ---
foods = {
    "Rice": {
        "types": {
            "Boiled": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
            "Fried": {"calories": 180, "protein": 3.5, "fat": 4.0, "carbs": 30},
            "Steamed": {"calories": 120, "protein": 2.5, "fat": 0.2, "carbs": 26},
        },
        "recipes": [
            {
                "title": "🍛 Veg Fried Rice",
                "desc": "Rice, mixed veggies, soy sauce, olive oil.",
                "steps": [
                    "1️⃣ Heat oil in a wok.",
                    "2️⃣ Add chopped veggies and stir-fry for 3–4 mins.",
                    "3️⃣ Add cooked rice and soy sauce.",
                    "4️⃣ Stir well and serve hot."
                ],
            },
            {
                "title": "🍋 Lemon Rice",
                "desc": "Rice, lemon juice, turmeric, curry leaves.",
                "steps": [
                    "1️⃣ Heat oil, add mustard seeds and curry leaves.",
                    "2️⃣ Add turmeric and cooked rice.",
                    "3️⃣ Mix lemon juice and salt, stir well.",
                    "4️⃣ Serve with chutney or yogurt."
                ],
            },
            {
                "title": "▶️ Watch: Fried Rice Video",
                "link": "https://www.youtube.com/watch?v=4hG_NvF7pXY",
            },
        ],
    },

    "Chicken Breast": {
        "types": {
            "Grilled": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
            "Boiled": {"calories": 150, "protein": 28, "fat": 3.0, "carbs": 0},
            "Fried": {"calories": 220, "protein": 26, "fat": 11, "carbs": 2},
        },
        "recipes": [
            {
                "title": "🍗 Grilled Chicken",
                "desc": "Marinated with olive oil, lemon, and herbs.",
                "steps": [
                    "1️⃣ Marinate chicken with olive oil, salt, pepper, and lemon juice for 30 mins.",
                    "2️⃣ Preheat grill and cook for 6–8 mins on each side.",
                    "3️⃣ Let it rest and serve with veggies or salad."
                ],
            },
            {
                "title": "🍛 Chicken Curry",
                "desc": "Chicken, tomato gravy, and spices.",
                "steps": [
                    "1️⃣ Sauté onions, garlic, and ginger until golden.",
                    "2️⃣ Add tomatoes and spices, cook till thick.",
                    "3️⃣ Add chicken pieces and simmer until cooked.",
                    "4️⃣ Garnish with coriander and serve hot."
                ],
            },
            {
                "title": "▶️ Watch: Chicken Curry Video",
                "link": "https://www.youtube.com/watch?v=HC8wWZ7bU1Q",
            },
        ],
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
            {
                "title": "🥚 Boiled Egg",
                "desc": "Simple boiled egg.",
                "steps": [
                    "1️⃣ Place eggs in boiling water for 7–10 minutes.",
                    "2️⃣ Cool in ice water and peel before serving."
                ],
            },
            {
                "title": "🍳 Scrambled Eggs",
                "desc": "Fluffy and delicious scrambled eggs.",
                "steps": [
                    "1️⃣ Beat eggs with salt and a splash of milk.",
                    "2️⃣ Pour into heated pan with butter.",
                    "3️⃣ Stir gently until fluffy."
                ],
            },
            {
                "title": "▶️ Watch: Egg Sandwich Video",
                "link": "https://www.youtube.com/watch?v=zR0RdkM-AxI",
            },
        ],
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

    # --- Recipe Section with clickable instructions ---
    st.markdown("---")
    st.markdown("### 🍽 Recipe Suggestions")

    for recipe in foods[food_name].get("recipes", []):
        if "link" in recipe:
            st.markdown(f"- [{recipe['title']}]({recipe['link']})")
        else:
            with st.expander(recipe["title"] + f" — {recipe['desc']}"):
                for step in recipe["steps"]:
                    st.write(step)

else:
    st.info("👈 Choose your food, cooking type, and quantity — then click **Submit**!")

# --- Notes Section ---
st.markdown("---")
st.markdown("### 🧠 Tip: Consistency is key! Track your meals daily for best results.")
with st.expander("📖 Add your own note"):
    note = st.text_area("Write down your meal notes or custom recipes:")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a real app, this could be stored locally or in the cloud.)")

st.caption("Built with ❤️ using Streamlit")

