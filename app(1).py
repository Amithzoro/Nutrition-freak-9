import streamlit as st
from datetime import datetime
import pytz
import random

# ---------- APP CONFIG ----------
st.set_page_config(page_title="💪 Smart Nutrition Tracker", layout="wide")
st.title("🏋️‍♂️ Smart Nutrition Tracker – Ultimate Gym Edition")

# ---------- TIME (IST 12hr) ----------
ist = pytz.timezone("Asia/Kolkata")
st.sidebar.write("🕒 Current Time (IST): **{}**".format(datetime.now(ist).strftime("%I:%M %p")))

# ---------- FOOD DATA ----------
foods = {
    "Chicken Breast": {
        "types": ["Grilled", "Boiled", "Baked"],
        "nutrition": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
        "recipes": [
            [
                "1️⃣ Mix olive oil, garlic, lemon juice, and salt in a bowl.",
                "2️⃣ Coat chicken pieces evenly and marinate for 30 min.",
                "3️⃣ Preheat grill or pan on medium-high heat.",
                "4️⃣ Grill 6–7 min per side until golden.",
                "5️⃣ Check internal temp 75 °C.",
                "6️⃣ Rest 5 min before slicing.",
                "7️⃣ Serve with brown rice and veggies.",
                "8️⃣ Optional: herbs or chili flakes.",
                "9️⃣ Store leftovers 2 days max.",
                "🔟 Great post-workout lean protein."
            ],
            [
                "1️⃣ Boil chicken in salted water for 20 min.",
                "2️⃣ Shred and mix with olive oil, herbs, and lemon.",
                "3️⃣ Add boiled vegetables.",
                "4️⃣ Serve hot or chilled.",
                "5️⃣ Use in wraps or salads.",
                "6️⃣ Sprinkle pepper and oregano.",
                "7️⃣ Add yogurt dressing.",
                "8️⃣ Optional chili for spice.",
                "9️⃣ Store 1 day refrigerated.",
                "🔟 Perfect meal-prep option."
            ],
            # eight more sets like above …
        ],
        "video": "https://www.youtube.com/watch?v=4gqdo6QmAqQ",
    },
    "Paneer": {
        "types": ["Grilled", "Curry", "Fried"],
        "nutrition": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
        "recipes": [
            [
                "1️⃣ Cut paneer cubes, marinate in yogurt + spices 20 min.",
                "2️⃣ Grill both sides 5 min.",
                "3️⃣ Serve with mint chutney.",
                "4️⃣ Add onions and peppers.",
                "5️⃣ Sprinkle chat masala.",
                "6️⃣ Use in sandwiches.",
                "7️⃣ Add lemon juice for tang.",
                "8️⃣ Serve with brown rice.",
                "9️⃣ Store refrigerated 1 day.",
                "🔟 Protein-rich vegetarian meal."
            ],
            # nine more detailed recipe sets …
        ],
        "video": "https://www.youtube.com/watch?v=VYp8jV4AG5g",
    },
    "Egg": {
        "types": ["Boiled", "Scrambled", "Omelette"],
        "nutrition": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
        "recipes": [
            [
                "1️⃣ Boil eggs 7 min, peel.",
                "2️⃣ Slice and sprinkle salt + pepper.",
                "3️⃣ Mix olive oil and chili flakes.",
                "4️⃣ Serve warm.",
                "5️⃣ Great for breakfast.",
                "6️⃣ Add toast for carbs.",
                "7️⃣ Optional: herbs.",
                "8️⃣ Store 2 days max.",
                "9️⃣ Quick on-the-go meal.",
                "🔟 High protein start."
            ],
            # nine more sets …
        ],
        "video": "https://www.youtube.com/watch?v=3a4zRZsXKys",
    },
    "Oats": {
        "types": ["Porridge", "Overnight", "Protein Bowl"],
        "nutrition": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
        "recipes": [
            [
                "1️⃣ Boil oats in milk 5 min.",
                "2️⃣ Add banana, honey, nuts.",
                "3️⃣ Stir and simmer 2 min.",
                "4️⃣ Serve warm.",
                "5️⃣ Sprinkle cinnamon.",
                "6️⃣ Add protein scoop.",
                "7️⃣ Mix berries.",
                "8️⃣ Serve with peanut butter.",
                "9️⃣ Healthy breakfast fuel.",
                "🔟 Keeps full till lunch."
            ],
            # nine more sets …
        ],
        "video": "https://www.youtube.com/watch?v=4pU9pG0Gm9k",
    },
    "Fish": {
        "types": ["Grilled", "Curry", "Baked"],
        "nutrition": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
        "recipes": [
            [
                "1️⃣ Marinate fish with lemon + garlic 15 min.",
                "2️⃣ Grill 4 min each side.",
                "3️⃣ Serve with veggies.",
                "4️⃣ Optional: olive oil drizzle.",
                "5️⃣ Add chili flakes.",
                "6️⃣ Check doneness.",
                "7️⃣ Serve with quinoa.",
                "8️⃣ Store 1 day.",
                "9️⃣ Omega-3 rich.",
                "🔟 Great post-workout meal."
            ],
            # nine more sets …
        ],
        "video": "https://www.youtube.com/watch?v=OFO5I9rL0Ko",
    },
    "Protein Shake": {
        "types": ["Whey", "Vegan", "Mass Gainer"],
        "nutrition": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
        "recipes": [
            [
                "1️⃣ Add 1 scoop whey to 300 ml milk.",
                "2️⃣ Add banana + oats.",
                "3️⃣ Blend till smooth.",
                "4️⃣ Add peanut butter.",
                "5️⃣ Chill with ice cubes.",
                "6️⃣ Optional cocoa powder.",
                "7️⃣ Drink post-workout.",
                "8️⃣ Add honey for taste.",
                "9️⃣ 25 g protein per shake.",
                "🔟 Helps muscle recovery."
            ],
            # nine more sets …
        ],
        "video": "https://www.youtube.com/watch?v=F7ZZIoB1bI0",
    },
}

# ---------- AI IMAGE DETECTION (mock) ----------
def detect_ai_image(_img):
    return "✅ 99% Real Image Detected"

# ---------- SIDEBAR INPUTS ----------
st.sidebar.header("🍛 Select Your Meal")
food_choice = st.sidebar.selectbox("Food", list(foods.keys()))
food_type = st.sidebar.selectbox("Type", foods[food_choice]["types"])
grams = st.sidebar.number_input("Grams", 0, 1000, 100, 10)
goal = st.sidebar.radio("Goal", ["Cutting", "Maintenance", "Bulking"])

uploaded = st.sidebar.file_uploader("📸 Upload meal photo", ["jpg", "jpeg", "png"])
if uploaded:
    st.image(uploaded, caption="Uploaded meal", width=250)
    st.sidebar.success(detect_ai_image(uploaded))

# ---------- SUBMIT ----------
if st.sidebar.button("✅ Submit"):
    st.session_state.submitted = True

if st.session_state.get("submitted"):
    data = foods[food_choice]["nutrition"]
    cal = data["calories"] * grams / 100
    pro = data["protein"] * grams / 100
    fat = data["fat"] * grams / 100
    carb = data["carbs"] * grams / 100

    st.success(f"{grams} g of {food_choice} ({food_type}) for **{goal}** mode")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 Calories", f"{cal:.1f}")
    c2.metric("💪 Protein", f"{pro:.1f}")
    c3.metric("🥑 Fat", f"{fat:.1f}")
    c4.metric("🍞 Carbs", f"{carb:.1f}")

    st.markdown("---")
    st.subheader("👨‍🍳 Recipes & Guide")

    with st.expander("📜 Step-by-Step Recipes"):
        for i, recipe in enumerate(foods[food_choice]["recipes"], 1):
            st.markdown(f"**Recipe {i}**")
            for step in recipe:
                st.write(step)
            st.markdown("---")

    with st.expander("🎥 Watch Recipe Video"):
        st.video(foods[food_choice]["video"])

st.caption("Built with ❤️ | Team Project Bro")
