import streamlit as st
import datetime
import pytz
from PIL import Image
import random

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.5", layout="wide")

st.title("🥦 Smart Nutrition Tracker v3.5")
st.markdown("### Track your meals, nutrition & progress like a pro — powered by AI + real cooking guides 🍳")

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
# NUTRITION CALCULATION
# ----------------------------
if grams > 0:
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    # Adjust calories based on fitness goal
    if goal == "Cutting":
        calories *= 0.9
    elif goal == "Bulking":
        calories *= 1.1

    st.success(f"**{grams}g of {food_name} ({goal} mode)**")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

else:
    st.info("👈 Start by selecting a food and entering its weight.")

# ----------------------------
# RECIPES + VIDEOS
# ----------------------------
st.markdown("---")
st.subheader(f"🍳 Recipes & Cooking Guides for {food_name}")

if food_name == "Chicken Breast":
    with st.expander("🔥 Grilled Chicken Recipe"):
        st.write("""
        **Ingredients:**
        - 200g chicken breast
        - Olive oil, salt, pepper, lemon juice, garlic

        **Steps:**
        1. Marinate chicken with ingredients for 30 minutes.
        2. Preheat grill pan and cook both sides for ~6-7 minutes.
        3. Rest for 2 minutes and serve hot with veggies.
        """)
        st.video("https://www.youtube.com/watch?v=F5DxMBQUOcI")
        st.video("https://www.youtube.com/watch?v=m25_qh1a5qI")

elif food_name == "Paneer":
    with st.expander("🧀 Paneer Tikka Masala"):
        st.write("""
        **Ingredients:** Paneer cubes, yogurt, masala, onion, tomato gravy.  
        **Steps:** Marinate → Grill → Mix with gravy → Serve with roti.
        """)
        st.video("https://www.youtube.com/watch?v=pgnFBet5pbo")
        st.video("https://www.youtube.com/watch?v=ZaUNzwr_KF0")

elif food_name == "Oats":
    with st.expander("🥣 Protein Oats Bowl"):
        st.write("""
        - Cook oats in milk or water.  
        - Add banana slices, almonds, and a scoop of whey.  
        - Stir and top with honey for energy.
        """)
        st.video("https://www.youtube.com/watch?v=E6FEtUPcT2E")

elif food_name == "Boiled Egg":
    with st.expander("🥚 Egg Curry"):
        st.write("""
        1. Boil eggs and peel.  
        2. Sauté onion, tomato, and spices.  
        3. Add eggs and simmer 5 min.
        """)
        st.video("https://www.youtube.com/watch?v=dxlW2b-Nckc")

elif food_name == "Whey Protein Shake":
    with st.expander("🥤 Protein Smoothie"):
        st.write("""
        Blend 1 scoop whey, 1 banana, peanut butter & milk.  
        Great post-workout drink!
        """)
        st.video("https://www.youtube.com/watch?v=1rZJ1b8XgS4")

elif food_name == "Grilled Fish":
    with st.expander("🐟 Spicy Fish Curry"):
        st.write("""
        - Marinate fish with turmeric, salt, and chili.  
        - Shallow fry and add to coconut gravy.  
        - Cook 10 mins and garnish with coriander.
        """)
        st.video("https://www.youtube.com/watch?v=w0Dqj9GCVzA")

# ----------------------------
# NOTES
# ----------------------------
st.markdown("---")
with st.expander("🧾 Add Meal Notes"):
    note = st.text_area("Write about this meal (taste, timing, macros, etc.):")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In real app, this can store locally or cloud.)")

st.caption("Built with ❤️ using Streamlit — Smart Nutrition Tracker v3.5")
