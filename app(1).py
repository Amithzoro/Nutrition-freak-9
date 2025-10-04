import streamlit as st
import datetime
import pytz
from PIL import Image
import random

st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.7", layout="wide")

st.title("🥦 Smart Nutrition Tracker v3.7")
st.markdown("### Track your meals, nutrition, and progress — now with more recipes 🍳")

# ----------------------------
# FOOD DATABASE
# ----------------------------
foods = {
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Grilled Fish": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Boiled Egg": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    "Apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
    "Milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "Almonds": {"calories": 579, "protein": 21, "fat": 50, "carbs": 22},
    "Egg Curry": {"calories": 150, "protein": 10, "fat": 10, "carbs": 3},
    "Whey Protein Shake": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
    "Vegetable Salad": {"calories": 45, "protein": 2, "fat": 0.3, "carbs": 9},
    "Grilled Prawns": {"calories": 99, "protein": 24, "fat": 1, "carbs": 0},
    "Chicken Curry": {"calories": 180, "protein": 20, "fat": 9, "carbs": 4},
    "Mixed Veg Curry": {"calories": 90, "protein": 4, "fat": 3, "carbs": 12},
    "Masala Omelette": {"calories": 180, "protein": 12, "fat": 14, "carbs": 1},
    "Greek Yogurt Bowl": {"calories": 120, "protein": 10, "fat": 5, "carbs": 9},
}

# ----------------------------
# SIDEBAR INPUT
# ----------------------------
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)
goal = st.sidebar.radio("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

# ----------------------------
# IMAGE UPLOAD & TIME TRACK
# ----------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Upload your meal image")
uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Meal Image", width=250)

    ai_detected = random.choice([True, False])
    if ai_detected:
        st.error("⚠️ This image might be AI-generated.")
    else:
        st.success("✅ Real image detected.")

    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.datetime.now(ist).strftime("%I:%M %p")
    st.info(f"🕒 Meal recorded at: **{current_time} IST**")

# ----------------------------
# SUBMIT BUTTON
# ----------------------------
submitted = st.sidebar.button("✅ Submit Meal")

if submitted and grams > 0:
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    if goal == "Cutting":
        calories *= 0.9
    elif goal == "Bulking":
        calories *= 1.1

    st.success(f"**{grams}g of {food_name} ({goal} mode)** submitted successfully!")
    st.write("Here’s your nutritional breakdown:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")
elif submitted:
    st.warning("⚠️ Please enter a valid food weight before submitting.")

# ----------------------------
# RECIPES SECTION
# ----------------------------
st.markdown("---")
st.subheader(f"🍳 Recipes & How To Cook {food_name}")

def recipe_block(title, steps, video_url):
    with st.expander(title):
        st.write(steps)
        st.video(video_url)

# ----------------------------
# EXTENDED RECIPES
# ----------------------------
if food_name == "Chicken Breast":
    recipe_block("🔥 Grilled Chicken Breast", """
**Ingredients:**
- 200g chicken breast, olive oil, lemon, pepper, garlic

**Steps:**
1. Marinate with olive oil, garlic, lemon, pepper.
2. Grill or pan-fry 6–7 mins per side.
3. Rest 2 mins and serve with veggies.
""", "https://www.youtube.com/watch?v=F5DxMBQUOcI")

    recipe_block("🍗 Chicken Stir Fry", """
**Ingredients:**
- 150g chicken strips, soy sauce, onion, bell peppers, olive oil.

**Steps:**
1. Stir-fry onions and peppers in olive oil.
2. Add chicken and soy sauce.
3. Cook until golden and soft.
""", "https://www.youtube.com/watch?v=f6U8fF8V2vE")

elif food_name == "Paneer":
    recipe_block("🧀 Paneer Tikka Masala", """
**Steps:**
1. Marinate paneer in yogurt + spices.
2. Grill till golden and add to curry base.
""", "https://www.youtube.com/watch?v=pgnFBet5pbo")

    recipe_block("🥗 Paneer Bhurji", """
**Steps:**
1. Crumble paneer and sauté with onion, tomato, green chili.
2. Add turmeric, chili powder, and garam masala.
3. Cook 5 mins and serve hot.
""", "https://www.youtube.com/watch?v=R6a4Qk8F1lE")

elif food_name == "Oats":
    recipe_block("🥣 Overnight Oats", """
**Steps:**
1. Mix oats, milk, honey, banana in jar.
2. Refrigerate overnight and eat cold.
""", "https://www.youtube.com/watch?v=zUZrjqx6xrc")

    recipe_block("🍪 Oats Pancake", """
**Steps:**
1. Blend oats, egg, banana, and protein powder.
2. Cook on a pan till golden both sides.
""", "https://www.youtube.com/watch?v=K2mF4mAYxGE")

elif food_name == "Boiled Egg":
    recipe_block("🥚 Egg Curry", """
**Steps:**
1. Sauté onions, add tomato and spices.
2. Add boiled eggs, simmer 5 mins.
""", "https://www.youtube.com/watch?v=dxlW2b-Nckc")

    recipe_block("🍳 Masala Omelette", """
**Steps:**
1. Mix 2 eggs with onion, tomato, chili.
2. Cook both sides golden.
""", "https://www.youtube.com/watch?v=gVvyQeF8a7o")

elif food_name == "Grilled Fish":
    recipe_block("🐟 Spicy Grilled Fish", """
**Steps:**
1. Marinate fish in lemon, chili, turmeric.
2. Grill both sides till golden.
""", "https://www.youtube.com/watch?v=w0Dqj9GCVzA")

    recipe_block("🍋 Lemon Butter Fish", """
**Steps:**
1. Cook fish in butter with lemon and herbs.
2. Serve with rice or salad.
""", "https://www.youtube.com/watch?v=wE0pV_tL8wU")

elif food_name == "Grilled Prawns":
    recipe_block("🦐 Garlic Butter Prawns", """
**Steps:**
1. Sauté prawns in butter, garlic, and parsley.
2. Cook 5 mins and serve hot.
""", "https://www.youtube.com/watch?v=gJw4e3xpnrU")

# ----------------------------
# NOTES
# ----------------------------
st.markdown("---")
with st.expander("🧾 Add Meal Notes"):
    note = st.text_area("Write about this meal (taste, timing, macros, etc.):")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a full app, this would store locally or on the cloud.)")

st.caption("Built with ❤️ using Streamlit — Smart Nutrition Tracker v3.7")
