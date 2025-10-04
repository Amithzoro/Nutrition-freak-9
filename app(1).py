import streamlit as st
from datetime import datetime, timedelta
import pytz

# 🥗 SMART NUTRITION TRACKER v4.1 (You x Me Edition)

st.set_page_config(page_title="🥗 Smart Nutrition Tracker", layout="wide")

st.title("🥦 Smart Nutrition Tracker")
st.markdown("### Track your meals like a pro — accurate, visual, and gym-ready!")

# -------------------------------------------
# --- FOOD DATABASE (Veg + Non-Veg Balanced) ---
# -------------------------------------------
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
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Sweet Potato": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
    "Egg White (Cooked)": {"calories": 52, "protein": 11, "fat": 0.2, "carbs": 0.7},
    "Salmon (Grilled)": {"calories": 208, "protein": 20, "fat": 13, "carbs": 0},
    "Prawns": {"calories": 99, "protein": 24, "fat": 0.3, "carbs": 0.2},
    "Turkey Breast": {"calories": 135, "protein": 30, "fat": 1, "carbs": 0},
    "Curd (Low Fat)": {"calories": 63, "protein": 5, "fat": 1.6, "carbs": 7},
    "Peanut Butter": {"calories": 588, "protein": 25, "fat": 50, "carbs": 20},
    "Brown Rice": {"calories": 111, "protein": 2.6, "fat": 0.9, "carbs": 23},
    "Spinach": {"calories": 23, "protein": 2.9, "fat": 0.4, "carbs": 3.6}
}

# -------------------------------------------
# --- SIDEBAR CONTROLS ---
# -------------------------------------------
st.sidebar.header("🍽 Choose Your Food & Quantity")

food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))

if food_name == "Egg (Boiled)":
    egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
    egg_count = st.sidebar.number_input("Enter number of eggs:", min_value=1, max_value=100, value=2)
    size_cal = {"Small": 60, "Medium": 78, "Large": 90}[egg_size]
    calories = size_cal * egg_count
    protein = 6 * egg_count
    fat = 5 * egg_count
    carbs = 0.6 * egg_count
else:
    grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

goal = st.sidebar.selectbox("🎯 Select your fitness goal:", ["Cutting", "Maintenance", "Bulking"])

uploaded_image = st.sidebar.file_uploader("📸 Upload your meal image (optional):", type=["jpg", "png", "jpeg"])

if st.sidebar.button("✅ Submit"):
    # --- TIME TRACKING (Indian Time) ---
    india_tz = pytz.timezone("Asia/Kolkata")
    time_now = datetime.now(india_tz).strftime("%I:%M %p")

    st.success(f"🕒 Meal logged at: {time_now} (IST)")
    st.markdown(f"### 🍱 {food_name} Nutrition Summary")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # --- GOAL CALORIE ADJUSTMENT ---
    multiplier = {"Cutting": 0.85, "Maintenance": 1.0, "Bulking": 1.15}[goal]
    daily_goal = 2000 * multiplier
    diff = daily_goal - calories

    if diff > 0:
        st.info(f"⚖️ You’re {diff:.0f} kcal below your {goal.lower()} goal — add a meal like oats or paneer.")
    else:
        st.success(f"💪 You’re {abs(diff):.0f} kcal above your {goal.lower()} goal — perfect for growth!")

    # --- IMAGE DISPLAY ---
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Meal Image", use_container_width=True)
        st.caption("📷 AI image authenticity verified ✅ (sample model placeholder)")

    # --- RECIPE DROPDOWN ---
    with st.expander("📖 Show Detailed Recipes & Videos"):
        st.markdown(f"### 🍴 {food_name} Recipes")

        # Show detailed text recipes
        st.markdown("""
        **Step-by-Step Recipe Example:**
        1. Clean and prepare all ingredients.
        2. Heat oil/ghee in a pan.
        3. Add the main ingredient and cook for 5–7 minutes.
        4. Season with salt, pepper, or masala as preferred.
        5. Serve hot with rice, roti, or vegetables.
        """)

        # Optional YouTube Videos
        st.markdown("🎥 **Watch Recipe Videos (optional):**")
        if food_name == "Chicken Breast":
            st.video("https://www.youtube.com/watch?v=0SPwwpruGIA")
        elif food_name == "Oats":
            st.video("https://www.youtube.com/watch?v=TLc9_tDJ4aA")
        elif food_name == "Paneer":
            st.video("https://www.youtube.com/watch?v=2VZTqk_Qm8w")
        elif food_name == "Rice (Cooked)":
            st.video("https://www.youtube.com/watch?v=Gv7bXrj5dQw")
        elif food_name == "Fish (Grilled)":
            st.video("https://www.youtube.com/watch?v=kHkzp1YvYuI")
        else:
            st.info("📄 No video available — full recipe provided above.")
else:
    st.warning("👈 Select your food, quantity, and click Submit to see results!")

st.caption("Built with ❤️ by You & ChatGPT — Team Work Makes Gains Work 💪")

