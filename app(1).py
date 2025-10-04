import streamlit as st
from PIL import Image, ImageStat
import random
from datetime import datetime
import pytz

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="🥗 Smart Nutrition & Meal Tracker", layout="wide")
st.title("🥦 Smart Nutrition & Meal Tracker")
st.markdown("### Eat Smart, Train Hard, and Track Everything in One Place 💪")

# ------------------ FOOD DATABASE ------------------
foods = {
    "Rice (Cooked)": {
        "calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28,
        "recipes": [
            {
                "title": "Lemon Rice",
                "text": "Cook rice, cool it slightly. Heat oil, add mustard, curry leaves, turmeric, and lemon juice. Mix with rice.",
                "video": "https://www.youtube.com/watch?v=IM8E8hE3KqE"
            },
            {
                "title": "Veg Fried Rice",
                "text": "Cook rice, stir-fry with vegetables, soy sauce, pepper, and a little oil.",
                "video": "https://www.youtube.com/watch?v=4cJczZ3xJ9Y"
            },
            {
                "title": "Brown Rice Bowl",
                "text": "Boil brown rice, add grilled paneer or chicken, and top with salad and curd.",
                "video": "https://www.youtube.com/watch?v=Z8vP3KJ2L6g"
            },
        ]
    },
    "Chicken Breast": {
        "calories": 165, "protein": 31, "fat": 3.6, "carbs": 0,
        "recipes": [
            {
                "title": "Grilled Chicken",
                "text": "Marinate chicken in olive oil, lemon, garlic, and pepper. Grill for 8-10 min each side.",
                "video": "https://www.youtube.com/watch?v=4CkJp9D7q4M"
            },
            {
                "title": "Chicken Curry",
                "text": "Cook onions, tomatoes, and spices. Add chicken and simmer till tender.",
                "video": "https://www.youtube.com/watch?v=QGZsFr1U6kE"
            },
            {
                "title": "Chicken Wrap",
                "text": "Grill chicken, roll in roti with veggies and curd dressing.",
                "video": "https://www.youtube.com/watch?v=cDq8V7C4KSk"
            },
        ]
    },
    "Egg": {
        "calories": 78, "protein": 6, "fat": 5, "carbs": 0.6,
        "recipes": [
            {
                "title": "Masala Omelette",
                "text": "Beat eggs, add onion, chili, salt. Cook in butter until golden.",
                "video": "https://www.youtube.com/watch?v=HjFx4gVXbJY"
            },
            {
                "title": "Boiled Egg Salad",
                "text": "Boil eggs, slice, and mix with cucumber, tomato, and lemon.",
                "video": "https://www.youtube.com/watch?v=F3Uu4K_GwFw"
            },
            {
                "title": "Egg Sandwich",
                "text": "Toast bread, add boiled eggs, lettuce, and mayo.",
                "video": "https://www.youtube.com/watch?v=kVtSgHNmHjA"
            },
        ]
    },
    "Paneer": {
        "calories": 265, "protein": 18, "fat": 21, "carbs": 2.4,
        "recipes": [
            {
                "title": "Paneer Tikka",
                "text": "Marinate paneer cubes in yogurt and spices, grill or bake until golden.",
                "video": "https://www.youtube.com/watch?v=qkzvcz3dZz8"
            },
            {
                "title": "Paneer Bhurji",
                "text": "Crumble paneer, sauté with onion, tomato, chili, and turmeric.",
                "video": "https://www.youtube.com/watch?v=7kW_0y0Yd6k"
            },
            {
                "title": "Paneer Rice Bowl",
                "text": "Mix cooked rice with paneer cubes, herbs, and lemon.",
                "video": "https://www.youtube.com/watch?v=F96JSe6_gmY"
            },
        ]
    },
    "Fish (Grilled)": {
        "calories": 206, "protein": 22, "fat": 12, "carbs": 0,
        "recipes": [
            {
                "title": "Tandoori Fish",
                "text": "Marinate fish in yogurt and spices, grill till flaky.",
                "video": "https://www.youtube.com/watch?v=Y5DPRmVvHR8"
            },
            {
                "title": "Fish Curry",
                "text": "Cook fish in coconut milk, curry leaves, and spices.",
                "video": "https://www.youtube.com/watch?v=2pHTc2Hro24"
            },
            {
                "title": "Baked Fish with Veggies",
                "text": "Bake marinated fish with bell peppers, garlic, and olive oil.",
                "video": "https://www.youtube.com/watch?v=FDhTvdYAIbE"
            },
        ]
    }
}

# ------------------ IMAGE AI DETECTION (SIMULATION) ------------------
def detect_ai_image(img):
    stat = ImageStat.Stat(img)
    variance = sum(stat.var)
    # Lower variance often means smoother, artificial image
    if variance < 500:
        return True
    return False

# ------------------ TIME UTILITY ------------------
def get_ist_time():
    tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(tz)
    return now.strftime("%I:%M %p")

# ------------------ SIDEBAR ------------------
st.sidebar.header("🍽 Meal Entry")
mode = st.sidebar.radio("Select Input Mode", ["📸 Upload Image", "📝 Manual Entry"])
goal = st.sidebar.selectbox("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

if "meals" not in st.session_state:
    st.session_state.meals = []

# ------------------ IMAGE UPLOAD ------------------
if mode == "📸 Upload Image":
    uploaded_file = st.sidebar.file_uploader("Upload your meal image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)

        if detect_ai_image(img):
            st.warning("⚠️ This image seems AI-generated. Please upload a real food photo.")
        else:
            detected_food = random.choice(list(foods.keys()))
            st.success(f"🍛 Detected: {detected_food}")
            grams = st.slider("Estimate serving size (grams):", 50, 500, 150, step=10)
            info = foods[detected_food]
            calories = info["calories"] * grams / 100
            protein = info["protein"] * grams / 100
            fat = info["fat"] * grams / 100
            carbs = info["carbs"] * grams / 100

            st.metric("🔥 Calories", f"{calories:.1f} kcal")
            st.metric("💪 Protein", f"{protein:.1f} g")
            st.metric("🥑 Fat", f"{fat:.1f} g")
            st.metric("🍞 Carbs", f"{carbs:.1f} g")

            time_now = get_ist_time()
            st.session_state.meals.append(
                {"Food": detected_food, "Grams": grams, "Calories": calories,
                 "Protein": protein, "Fat": fat, "Carbs": carbs, "Time": time_now}
            )

# ------------------ MANUAL ENTRY ------------------
if mode == "📝 Manual Entry":
    food_name = st.sidebar.selectbox("Select a food item", list(foods.keys()))
    grams = st.sidebar.number_input("Enter weight (in grams)", min_value=0, max_value=1000, value=100, step=10)
    if grams > 0:
        info = foods[food_name]
        calories = info["calories"] * grams / 100
        protein = info["protein"] * grams / 100
        fat = info["fat"] * grams / 100
        carbs = info["carbs"] * grams / 100
        time_now = get_ist_time()
        st.session_state.meals.append(
            {"Food": food_name, "Grams": grams, "Calories": calories,
             "Protein": protein, "Fat": fat, "Carbs": carbs, "Time": time_now}
        )
        st.success(f"Added {grams}g of {food_name} at {time_now}.")

# ------------------ DISPLAY MEAL LOG ------------------
if st.session_state.meals:
    st.markdown("## 📊 Today's Meal Log (IST)")
    st.dataframe(st.session_state.meals)

    total_cal = sum(m["Calories"] for m in st.session_state.meals)
    total_pro = sum(m["Protein"] for m in st.session_state.meals)
    total_fat = sum(m["Fat"] for m in st.session_state.meals)
    total_carb = sum(m["Carbs"] for m in st.session_state.meals)

    st.markdown(f"### 🧾 **Total for Today:** {total_cal:.1f} kcal | {total_pro:.1f}g Protein | {total_fat:.1f}g Fat | {total_carb:.1f}g Carbs")

# ------------------ RECIPES SECTION ------------------
st.markdown("---")
st.markdown("## 🧑‍🍳 Recipes & How to Cook")
selected = st.selectbox("Select a food to view recipes", list(foods.keys()))

for r in foods[selected]["recipes"]:
    with st.expander(f"🍽 {r['title']}"):
        st.write(r["text"])
        st.video(r["video"])

# ------------------ NOTES ------------------
st.markdown("---")
with st.expander("🗒️ Add a personal note"):
    note = st.text_area("Write down your meal reflection or comment:")
    if st.button("💾 Save Note"):
        st.success("Note saved! (In a real version, this would store in a database.)")

st.caption("Built with ❤️ using Streamlit — Smart Nutrition Tracker v2.0")
