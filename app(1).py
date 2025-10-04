import streamlit as st

st.set_page_config(page_title="🏋️ Smart Nutrition Calculator", layout="wide")

st.title("🥦 Smart Nutrition Calculator for Gym & Sports")
st.markdown("### Track your meals, calories, and protein goals — made for athletes & fitness lovers 💪")

# --- Food database ---
foods = {
    "Chicken Breast": {
        "types": {
            "Grilled": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
            "Boiled": {"calories": 150, "protein": 28, "fat": 3.0, "carbs": 0},
            "Fried": {"calories": 220, "protein": 26, "fat": 11, "carbs": 2},
        },
        "recipes": [
            {
                "title": "🍗 Grilled Chicken with Veggies",
                "desc": "Lean grilled chicken served with sautéed vegetables.",
                "steps": [
                    "1️⃣ Marinate chicken in olive oil, lemon, pepper, and salt for 30 mins.",
                    "2️⃣ Grill each side for 6–8 minutes until golden.",
                    "3️⃣ Serve with roasted veggies and brown rice."
                ],
            },
            {
                "title": "🍛 Chicken Curry",
                "desc": "High-protein curry with rich flavor.",
                "steps": [
                    "1️⃣ Sauté onions and garlic.",
                    "2️⃣ Add tomato puree and spices.",
                    "3️⃣ Add chicken and simmer until tender."
                ],
            },
            {"title": "▶️ Watch: Grilled Chicken Video", "link": "https://www.youtube.com/watch?v=HC8wWZ7bU1Q"},
        ],
    },

    "Egg": {
        "sizes": {
            "Small": {"calories": 54, "protein": 4.7, "fat": 3.6, "carbs": 0.3},
            "Medium": {"calories": 68, "protein": 6.3, "fat": 4.8, "carbs": 0.4},
            "Large": {"calories": 78, "protein": 6.8, "fat": 5.3, "carbs": 0.6},
        },
        "types": {"Boiled": 1.0, "Scrambled": 1.1, "Fried": 1.25, "Omelette": 1.2},
        "recipes": [
            {
                "title": "🥚 Boiled Eggs",
                "desc": "Simple, perfect protein snack.",
                "steps": [
                    "1️⃣ Boil eggs for 8–10 minutes.",
                    "2️⃣ Cool and peel. Sprinkle with salt or pepper."
                ],
            },
            {
                "title": "🍳 Protein Omelette",
                "desc": "Omelette packed with veggies and cheese.",
                "steps": [
                    "1️⃣ Whisk eggs with salt and chili flakes.",
                    "2️⃣ Add chopped veggies.",
                    "3️⃣ Cook until golden on both sides."
                ],
            },
            {"title": "▶️ Watch: Muscle Omelette Recipe", "link": "https://www.youtube.com/watch?v=zR0RdkM-AxI"},
        ],
    },

    "Beef": {
        "types": {
            "Grilled": {"calories": 250, "protein": 26, "fat": 15, "carbs": 0},
            "Boiled": {"calories": 210, "protein": 25, "fat": 10, "carbs": 0},
            "Steak": {"calories": 271, "protein": 28, "fat": 17, "carbs": 0},
        },
        "recipes": [
            {
                "title": "🥩 Grilled Beef Steak",
                "desc": "Perfect for bulking — protein-dense and juicy.",
                "steps": [
                    "1️⃣ Season with salt, pepper, and garlic powder.",
                    "2️⃣ Grill 4–5 mins each side for medium rare.",
                    "3️⃣ Rest before slicing."
                ],
            },
            {
                "title": "🍲 Beef Stew",
                "desc": "Slow-cooked, nutrient-rich meal.",
                "steps": [
                    "1️⃣ Sear beef chunks until brown.",
                    "2️⃣ Add broth, carrots, and potatoes.",
                    "3️⃣ Simmer for 2 hours until tender."
                ],
            },
            {"title": "▶️ Watch: Perfect Steak Video", "link": "https://www.youtube.com/watch?v=WEr4Y5ncvxM"},
        ],
    },

    "Fish (Salmon)": {
        "types": {
            "Grilled": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
            "Baked": {"calories": 180, "protein": 20, "fat": 9, "carbs": 0},
            "Fried": {"calories": 240, "protein": 21, "fat": 17, "carbs": 0},
        },
        "recipes": [
            {
                "title": "🐟 Grilled Salmon",
                "desc": "Rich in Omega-3 — great for recovery.",
                "steps": [
                    "1️⃣ Marinate with lemon, garlic, and olive oil.",
                    "2️⃣ Grill for 5 mins each side.",
                    "3️⃣ Serve with greens."
                ],
            },
            {
                "title": "🍛 Salmon Rice Bowl",
                "desc": "Protein-rich bowl with rice and greens.",
                "steps": [
                    "1️⃣ Flake cooked salmon.",
                    "2️⃣ Add rice, avocado, and cucumber.",
                    "3️⃣ Top with soy sauce."
                ],
            },
            {"title": "▶️ Watch: Salmon Recipe", "link": "https://www.youtube.com/watch?v=a4Tj9a6i_8E"},
        ],
    },

    "Oats": {
        "types": {
            "Plain": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
            "Cooked with Milk": {"calories": 150, "protein": 6, "fat": 3, "carbs": 25},
            "Overnight Oats": {"calories": 200, "protein": 8, "fat": 5, "carbs": 30},
        },
        "recipes": [
            {
                "title": "🥣 Overnight Oats",
                "desc": "Great pre-workout meal.",
                "steps": [
                    "1️⃣ Mix oats, milk, chia seeds, and honey.",
                    "2️⃣ Refrigerate overnight.",
                    "3️⃣ Add fruits before serving."
                ],
            },
            {
                "title": "🍌 Banana Oat Smoothie",
                "desc": "Quick carb + protein fuel.",
                "steps": [
                    "1️⃣ Blend oats, banana, milk, and peanut butter.",
                    "2️⃣ Serve chilled."
                ],
            },
            {"title": "▶️ Watch: High-Protein Oats", "link": "https://www.youtube.com/watch?v=gfuL0sXGrq4"},
        ],
    },

    "Paneer": {
        "types": {
            "Raw": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
            "Grilled": {"calories": 280, "protein": 20, "fat": 22, "carbs": 2.5},
            "Curry": {"calories": 310, "protein": 17, "fat": 25, "carbs": 5},
        },
        "recipes": [
            {
                "title": "🧀 Grilled Paneer Tikka",
                "desc": "Vegetarian high-protein option.",
                "steps": [
                    "1️⃣ Marinate paneer in yogurt and spices.",
                    "2️⃣ Grill on skewers for 5–7 mins.",
                    "3️⃣ Serve with mint chutney."
                ],
            },
            {"title": "▶️ Watch: Paneer Tikka", "link": "https://www.youtube.com/watch?v=V3M0YQnTnE0"},
        ],
    },
}

# --- Sidebar ---
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))

# Special case for eggs
if food_name == "Egg":
    egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
    egg_style = st.sidebar.selectbox("Cooking type:", list(foods["Egg"]["types"].keys()))
    egg_count = st.sidebar.number_input("Number of eggs:", min_value=1, max_value=100, value=1)
else:
    cook_type = st.sidebar.selectbox("Select cooking type:", list(foods[food_name]["types"].keys()))
    grams = st.sidebar.number_input("Enter weight (grams):", min_value=0, max_value=1000, value=100, step=10)

submit = st.sidebar.button("✅ Submit")

# --- Main Output ---
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

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # Recipes
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

# --- Notes ---
st.markdown("---")
st.markdown("### 🧠 Tip: Athletes need balanced macros — don’t skip your proteins & hydration!")
with st.expander("📖 Add your own note"):
    note = st.text_area("Write your custom recipes or progress notes:")
    if st.button("💾 Save Note"):
        st.success("Note saved locally!")

st.caption("Built with ❤️ using Streamlit")
