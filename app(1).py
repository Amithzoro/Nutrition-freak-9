import streamlit as st
from datetime import datetime
import pytz

# ----------------------- PAGE SETUP -----------------------
st.set_page_config(page_title="💪 Smart Nutrition Tracker v6.2", layout="wide")
st.title("🥗 Smart Nutrition Tracker — Perfect Flow Edition")
st.markdown("### Track your nutrition, recipes, and goals like a pro!")

# ----------------------- FOOD DATABASE -----------------------
foods = {
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Egg (Boiled)": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Lentils": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Greek Yogurt": {"calories": 59, "protein": 10, "fat": 0.4, "carbs": 3.6},
    "Peanut Butter": {"calories": 588, "protein": 25, "fat": 50, "carbs": 20},
    "Chickpeas": {"calories": 164, "protein": 9, "fat": 2.6, "carbs": 27},
    "Prawns": {"calories": 99, "protein": 24, "fat": 0.3, "carbs": 0.2},
    "Sweet Potato": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
    "Whey Protein": {"calories": 400, "protein": 80, "fat": 7, "carbs": 8},
    "Protein Bar": {"calories": 350, "protein": 30, "fat": 10, "carbs": 40},
}

# ----------------------- RECIPES -----------------------
recipes = {
    "Chicken Breast": [
        ("Grilled Chicken", "Marinate with olive oil, salt, pepper, grill for 8 min/side.", "https://www.youtube.com/watch?v=4UHVxRjYX8E"),
        ("Chicken Curry", "Cook onions, tomato, garlic, spices, then add chicken and simmer 20 mins.", "https://www.youtube.com/watch?v=I3tBz2kT7zQ"),
        ("Chicken Stir Fry", "Saute veggies, add soy sauce, and chicken strips.", "https://www.youtube.com/watch?v=Qv6F7D8l8wk"),
        ("Chicken Wrap", "Mix grilled chicken with lettuce & yogurt dressing in a wrap.", ""),
        ("Chicken Salad", "Add grilled chicken to greens with olive oil & lemon.", ""),
        ("Baked Chicken", "Marinate and bake at 200°C for 25 mins.", ""),
        ("Boiled Chicken", "Boil chicken with salt and herbs for 20 mins.", ""),
        ("Chicken Sandwich", "Grill chicken and layer it with veggies and sauce in bread.", ""),
        ("Spicy Chicken Skewers", "Thread marinated pieces on skewers, grill for 10 mins.", ""),
        ("Tandoori Chicken", "Marinate in yogurt, chili, lime; bake or grill.", "https://www.youtube.com/watch?v=4oPOkzqYx1c")
    ],
    "Egg (Boiled)": [
        ("Boiled Eggs", "Boil eggs for 8–10 minutes, cool and peel.", "https://www.youtube.com/watch?v=8U3Y2tYQK8I"),
        ("Scrambled Eggs", "Whisk eggs, cook with butter until fluffy.", "https://www.youtube.com/watch?v=1S5aZlHgb7U"),
        ("Omelet", "Mix veggies with egg, cook on both sides.", ""),
        ("Egg Curry", "Cook onions, spices, tomato; add boiled eggs.", ""),
        ("Poached Egg", "Boil water, swirl, drop egg for 3–4 mins.", ""),
        ("Egg Bhurji", "Scramble eggs with onions, tomato & masala.", ""),
        ("Egg Toast", "Dip bread in egg mix, fry golden.", ""),
        ("Egg Fried Rice", "Mix cooked rice with scrambled eggs & veggies.", ""),
        ("Deviled Eggs", "Halve boiled eggs, mix yolks with mayo & mustard.", ""),
        ("Egg Wrap", "Roll omelet with veggies in a tortilla.", "")
    ],
    # Add recipes for other foods in the same format...
}

# ----------------------- SIDEBAR -----------------------
st.sidebar.header("🍽 Meal Tracker")

food_name = st.sidebar.selectbox("Select Food:", list(foods.keys()))

grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)

# Special handling for eggs
egg_size, egg_count = None, None
if food_name == "Egg (Boiled)":
    egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
    egg_count = st.sidebar.number_input("Number of eggs:", 1, 100, 1)

goal = st.sidebar.radio("Select Goal:", ["Cutting", "Maintenance", "Bulking"])
uploaded_image = st.sidebar.file_uploader("📸 Upload your food image (optional):", type=["jpg", "png"])

submit = st.sidebar.button("🍽 Submit")

# ----------------------- MAIN AREA -----------------------
if submit:
    info = foods[food_name]
    if food_name == "Egg (Boiled)" and egg_count:
        base_cal = info["calories"] * egg_count
        base_pro = info["protein"] * egg_count
        base_fat = info["fat"] * egg_count
        base_carb = info["carbs"] * egg_count
    else:
        base_cal = info["calories"] * grams / 100
        base_pro = info["protein"] * grams / 100
        base_fat = info["fat"] * grams / 100
        base_carb = info["carbs"] * grams / 100

    # Goal-based macro adjustment
    if goal == "Cutting":
        factor = 0.8
    elif goal == "Bulking":
        factor = 1.15
    else:
        factor = 1.0

    calories = base_cal * factor
    protein = base_pro * factor
    fat = base_fat * factor
    carbs = base_carb * factor

    # Time (India)
    india_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M %p")

    st.success(f"✅ You selected {grams}g of {food_name} at {india_time} ({goal})")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # Image AI mock detection
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        st.info("🤖 AI Detection: Detected as high-protein food (mock demo)")

    # View Recipes Button
    if st.button("🍳 View Recipes & Videos"):
        st.subheader(f"📖 {food_name} — Recipes & Videos")
        if food_name in recipes:
            for i, (rname, steps, link) in enumerate(recipes[food_name], 1):
                with st.expander(f"Recipe {i}: {rname}"):
                    st.write(f"**How to Cook:** {steps}")
                    if link:
                        st.video(link)
        else:
            st.warning("Recipes not added yet for this item!")

# ----------------------- FOOTER -----------------------
st.markdown("---")
st.caption("Built by ❤️ You & GPT | Smart Nutrition Tracker v6.2")
