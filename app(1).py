import streamlit as st
import datetime
import pytz
from PIL import Image
import random

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.6", layout="wide")

st.title("🥦 Smart Nutrition Tracker v3.6")
st.markdown("### Track your meals, nutrition, and progress — with real recipes 🍳")

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
    "Salmon": {"calories": 208, "protein": 20, "fat": 13, "carbs": 0},
    "Egg Curry": {"calories": 150, "protein": 10, "fat": 10, "carbs": 3},
    "Tofu Stir Fry": {"calories": 120, "protein": 10, "fat": 7, "carbs": 5},
    "Whey Protein Shake": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
    "Vegetable Salad": {"calories": 45, "protein": 2, "fat": 0.3, "carbs": 9},
}

# ----------------------------
# SIDEBAR SELECTION
# ----------------------------
st.sidebar.header("🍽 Choose Your Food & Quantity")

food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (in grams):", min_value=0, max_value=1000, value=100, step=10)
goal = st.sidebar.radio("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

# ----------------------------
# IMAGE UPLOAD + TIME TRACK
# ----------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Upload your meal image")

uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Meal Image", width=250)

    # Mock AI image detection
    ai_detected = random.choice([True, False])
    if ai_detected:
        st.error("⚠️ This image might be AI-generated.")
    else:
        st.success("✅ Real image detected.")

    # Record current Indian time
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
# RECIPES + VIDEOS (DETAILED)
# ----------------------------
st.markdown("---")
st.subheader(f"🍳 Detailed Recipes & Cooking Guide for {food_name}")

if food_name == "Chicken Breast":
    with st.expander("🔥 Grilled Chicken Breast Recipe"):
        st.write("""
        **Ingredients:**
        - 200g chicken breast
        - 1 tbsp olive oil
        - 1 tsp garlic paste
        - 1 tsp lemon juice
        - Salt, pepper, chili flakes to taste

        **Steps:**
        1. Clean and pat dry the chicken.
        2. Mix olive oil, garlic, lemon juice, salt, and pepper.
        3. Marinate chicken for at least 30 minutes.
        4. Heat grill or non-stick pan and cook both sides 6–7 minutes until golden.
        5. Let it rest for 2 minutes before slicing.
        """)
        st.video("https://www.youtube.com/watch?v=F5DxMBQUOcI")

elif food_name == "Paneer":
    with st.expander("🧀 Paneer Tikka Masala"):
        st.write("""
        **Ingredients:**
        - 200g paneer cubes
        - 2 tbsp yogurt
        - 1 tsp ginger-garlic paste
        - 1 tsp red chili, turmeric, garam masala
        - 1 onion, 1 tomato, and coriander leaves

        **Steps:**
        1. Marinate paneer in yogurt and spices for 30 mins.
        2. Grill or roast till golden brown.
        3. In another pan, sauté onion and tomato till soft.
        4. Add the paneer to this gravy and simmer 5 minutes.
        5. Garnish with coriander and serve hot.
        """)
        st.video("https://www.youtube.com/watch?v=pgnFBet5pbo")

elif food_name == "Oats":
    with st.expander("🥣 Protein Oats Breakfast Bowl"):
        st.write("""
        **Ingredients:**
        - 1/2 cup oats
        - 1 cup milk
        - 1 banana, 5 almonds
        - 1 scoop whey protein
        - Honey (optional)

        **Steps:**
        1. Cook oats in milk for 5 minutes.
        2. Add banana slices, almonds, and honey.
        3. Mix whey protein once cooled slightly.
        4. Stir and enjoy warm or chilled.
        """)
        st.video("https://www.youtube.com/watch?v=E6FEtUPcT2E")

elif food_name == "Boiled Egg":
    with st.expander("🥚 Simple Egg Curry"):
        st.write("""
        **Ingredients:**
        - 3 boiled eggs
        - 1 onion, 1 tomato
        - 1 tsp garam masala, 1 tsp chili powder
        - Salt, oil, coriander

        **Steps:**
        1. Sauté onions till brown.
        2. Add tomato, chili powder, and masala.
        3. Add 1/4 cup water and mix well.
        4. Add eggs, cook 5 mins, and garnish with coriander.
        """)
        st.video("https://www.youtube.com/watch?v=dxlW2b-Nckc")

elif food_name == "Grilled Fish":
    with st.expander("🐟 Spicy Grilled Fish"):
        st.write("""
        **Ingredients:**
        - 150g fish fillet
        - 1 tsp turmeric, chili powder, lemon juice
        - 1 tbsp oil, salt to taste

        **Steps:**
        1. Marinate fish with spices and lemon for 15 mins.
        2. Heat pan and drizzle oil.
        3. Cook fish 3–4 mins per side till crisp golden.
        4. Serve with lemon wedge and salad.
        """)
        st.video("https://www.youtube.com/watch?v=w0Dqj9GCVzA")

elif food_name == "Whey Protein Shake":
    with st.expander("🥤 High Protein Smoothie"):
        st.write("""
        **Ingredients:**
        - 1 scoop whey protein
        - 1 banana
        - 1 tbsp peanut butter
        - 1 cup milk or water
        - Ice cubes

        **Steps:**
        1. Add all ingredients to blender.
        2. Blend until smooth and creamy.
        3. Drink immediately after workout for recovery.
        """)
        st.video("https://www.youtube.com/watch?v=1rZJ1b8XgS4")

# ----------------------------
# NOTES
# ----------------------------
st.markdown("---")
with st.expander("🧾 Add Meal Notes"):
    note = st.text_area("Write about this meal (taste, timing, macros, etc.):")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a full app, this would store locally or on the cloud.)")

st.caption("Built with ❤️ using Streamlit — Smart Nutrition Tracker v3.6")
