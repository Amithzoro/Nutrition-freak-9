import streamlit as st
from datetime import datetime
from PIL import Image
import pytz
import random

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.5", layout="wide")

st.title("🥦 Smart Nutrition & Fitness Tracker")
st.markdown("### Track your meals, watch real recipes, and stay consistent 💪")

# ---------------------- FOOD DATABASE ----------------------
foods = {
    # Veg
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4, "carbs": 2},
    "Broccoli": {"calories": 34, "protein": 3, "fat": 0.4, "carbs": 7},
    "Sweet Potato": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
    "Lentils (Dal)": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
    "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    "Almonds": {"calories": 579, "protein": 21, "fat": 50, "carbs": 22},
    "Milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "Greek Yogurt": {"calories": 59, "protein": 10, "fat": 0.4, "carbs": 3.6},

    # Non-Veg
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Chicken Thigh": {"calories": 209, "protein": 26, "fat": 10.9, "carbs": 0},
    "Fish (Salmon)": {"calories": 208, "protein": 20, "fat": 13, "carbs": 0},
    "Fish (Tilapia)": {"calories": 96, "protein": 20, "fat": 2, "carbs": 0},
    "Tuna": {"calories": 132, "protein": 28, "fat": 1, "carbs": 0},
    "Egg": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Prawns": {"calories": 99, "protein": 24, "fat": 0.3, "carbs": 0.2},
    "Whey Protein": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
    "Peanut Butter": {"calories": 588, "protein": 25, "fat": 50, "carbs": 20},
}

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("🍽 Meal Input")
food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)
fitness_goal = st.sidebar.selectbox("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

# ---------------------- IMAGE UPLOAD ----------------------
uploaded_file = st.sidebar.file_uploader("📸 Upload a food image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # AI image detection simulation
    if random.choice([True, False]):
        st.warning("🤖 Detected: This might be an AI-generated image.")
    else:
        st.success("✅ Real image detected.")

# ---------------------- TIME TRACKING ----------------------
tz_india = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(tz_india)
meal_time = current_time.strftime("%I:%M %p")
st.sidebar.write(f"🕒 Current Time (IST): {meal_time}")

# ---------------------- CALCULATION ----------------------
if grams > 0:
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    st.success(f"**You selected {grams}g of {food_name}**")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

# ---------------------- RECIPES ----------------------
st.markdown("## 🍳 Cooking Recipes & Videos")

# Recipe Database
if food_name == "Chicken Breast":
    with st.expander("🍗 Grilled Chicken - Step by Step"):
        st.write("""
        **How to Cook:**
        1. Marinate chicken with olive oil, garlic, lemon, and pepper.
        2. Let it rest for 30 minutes.
        3. Grill for 6–7 minutes each side.
        4. Serve with sautéed vegetables.
        """)
        st.video("https://www.youtube.com/watch?v=2qH9ZSj5FIM")
        st.video("https://www.youtube.com/watch?v=F5DxMBQUOcI")
        st.video("https://www.youtube.com/watch?v=5d9zRCpHLNg")

if food_name == "Paneer":
    with st.expander("🧀 Paneer Tikka - Step by Step"):
        st.write("""
        **How to Cook:**
        1. Marinate paneer cubes with curd, turmeric, red chili, garam masala.
        2. Skewer with veggies.
        3. Grill or bake for 15 minutes.
        4. Serve with mint chutney.
        """)
        st.video("https://www.youtube.com/watch?v=pgnFBet5pbo")
        st.video("https://www.youtube.com/watch?v=TnsQdRxi84Q")
        st.video("https://www.youtube.com/watch?v=ZaUNzwr_KF0")

if food_name == "Egg":
    with st.expander("🥚 Boiled Egg & Curry Ideas"):
        st.write("""
        **How to Cook:**
        1. Boil eggs for 8 minutes and peel.
        2. For curry: sauté onions, tomatoes, and masala.
        3. Add eggs, simmer for 5 minutes.
        """)
        st.video("https://www.youtube.com/watch?v=FVtgn8PpS-M")
        st.video("https://www.youtube.com/watch?v=pCq7L9s3DjQ")

if food_name == "Oats":
    with st.expander("🥣 Oats Recipes"):
        st.write("""
        **How to Cook:**
        1. Boil oats with milk or water for 5 minutes.
        2. Add banana slices, peanut butter, or whey for protein.
        3. Top with nuts or honey.
        """)
        st.video("https://www.youtube.com/watch?v=YI1WqYKvZzY")
        st.video("https://www.youtube.com/watch?v=shz3m2uh7v8")

if food_name == "Fish (Salmon)":
    with st.expander("🐟 Grilled Salmon"):
        st.write("""
        **How to Cook:**
        1. Marinate with olive oil, garlic, and herbs.
        2. Grill for 5–6 minutes each side.
        3. Serve with lemon and greens.
        """)
        st.video("https://www.youtube.com/watch?v=cq7SuDK7C9Y")
        st.video("https://www.youtube.com/watch?v=4A4Dg5X4NFs")

if food_name == "Whey Protein":
    with st.expander("🥤 Protein Shakes"):
        st.write("""
        **Recipes:**
        1. **Banana Whey Shake** — Blend banana + whey + milk + peanut butter.  
        2. **Oats Whey Smoothie** — Add soaked oats for extra carbs.  
        3. **Chocolate Whey Smoothie** — Add cocoa and ice for taste.
        """)
        st.video("https://www.youtube.com/watch?v=1l1HxqZLwMo")
        st.video("https://www.youtube.com/watch?v=tGybS_TB6S0")

# ---------------------- NOTES ----------------------
st.markdown("---")
st.markdown("### 🧾 Add Your Own Notes")
note = st.text_area("Write your meal notes or custom ideas:")
if st.button("💾 Save Note"):
    st.success("✅ Note saved! (Locally simulated for now)")

st.caption("Built with ❤️ using Streamlit — by your bro 💪")
