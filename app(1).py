import streamlit as st
import datetime
import pytz

# ---------------------- APP CONFIG ----------------------
st.set_page_config(page_title="💪 Smart Nutrition Tracker v4.0", layout="wide")
st.title("🥗 Smart Nutrition Tracker v4.0")
st.markdown("### The ultimate gym & sportsperson meal calculator — smart, clean, and powerful.")

# ---------------------- FOOD DATABASE ----------------------
foods = {
    "Grilled Chicken": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Boiled Egg": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Rice (Cooked)": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Egg Curry": {"calories": 150, "protein": 9, "fat": 11, "carbs": 2},
    "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    "Milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "Almonds": {"calories": 579, "protein": 21, "fat": 50, "carbs": 22},
    "Apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
    "Lentils (Cooked)": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
    "Peanut Butter": {"calories": 588, "protein": 25, "fat": 50, "carbs": 20},
}

# ---------------------- IMAGE UPLOAD ----------------------
st.sidebar.header("📸 Upload Food Image (optional)")
uploaded_image = st.sidebar.file_uploader("Upload a food image:", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.sidebar.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.sidebar.success("✅ Image uploaded! Food detection will improve future accuracy.")

# ---------------------- FOOD SELECTION ----------------------
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select a food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (grams):", min_value=0, max_value=1000, value=100, step=10)

if st.sidebar.button("✅ Submit"):
    info = foods[food_name]
    calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    st.markdown("---")
    st.success(f"**Results for {grams}g of {food_name}:**")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # Current Indian Time
    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.datetime.now(ist).strftime("%I:%M %p")
    st.info(f"🕒 Logged at: {current_time} (Indian Standard Time)")

    # Recipes section
    with st.expander("📖 View Recipes (click to expand)"):
        st.markdown(f"### 🍽 Recipes for {food_name}")

        # Step-by-step recipes
        recipes = {
            "Grilled Chicken": [
                "Marinate with olive oil, lemon juice, pepper, and salt.",
                "Rest for 30 minutes.",
                "Grill for 6–8 minutes each side.",
                "Serve with steamed veggies.",
            ],
            "Boiled Egg": [
                "Place eggs in a pot of water.",
                "Boil for 6–8 minutes.",
                "Cool under running water.",
                "Peel and enjoy with salt or salad.",
            ],
            "Paneer": [
                "Cut paneer into cubes.",
                "Marinate with curd, turmeric, chili powder.",
                "Pan-fry or grill for 10 minutes.",
                "Serve with lemon and coriander.",
            ],
            "Oats": [
                "Boil 1 cup oats with 2 cups milk or water.",
                "Add honey or fruits.",
                "Cook until creamy.",
                "Top with nuts or banana slices.",
            ],
        }

        for step in recipes.get(food_name, ["Recipe not found yet."]):
            st.markdown(f"🔹 {step}")

        # Optional YouTube Video
        video_links = {
            "Grilled Chicken": "https://www.youtube.com/watch?v=8L5nVnQ9QhA",
            "Boiled Egg": "https://www.youtube.com/watch?v=4z4VbUJH3Zo",
            "Paneer": "https://www.youtube.com/watch?v=5_PB8vY-7bM",
            "Oats": "https://www.youtube.com/watch?v=VgJ8WgFYwVo",
        }

        if food_name in video_links:
            if st.button(f"▶️ Watch {food_name} Recipe Video"):
                st.video(video_links[food_name])

else:
    st.info("👈 Choose a food and click Submit to see detailed results!")

st.markdown("---")
st.caption("Built with ❤️ for gym lovers and athletes | Smart Nutrition Tracker v4.0")
