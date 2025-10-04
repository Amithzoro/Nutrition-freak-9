import streamlit as st
from datetime import datetime
import pytz
import random

# --------------------------
# 🧭 APP CONFIG
# --------------------------
st.set_page_config(page_title="💪 Smart Nutrition Tracker", layout="wide")
st.title("🏋️‍♂️ Smart Nutrition Tracker – Ultimate Gym Edition")
st.markdown("Track your meals, macros, and recipes like a pro! 💪")

# --------------------------
# 🕒 INDIAN TIME TRACKER
# --------------------------
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).strftime("%I:%M %p")
st.sidebar.write(f"🕒 Current Time (IST): **{current_time}**")

# --------------------------
# 🥩 FOOD DATABASE
# --------------------------
foods = {
    "Chicken Breast": {
        "types": ["Grilled", "Boiled", "Fried", "Baked"],
        "nutrition": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
        "recipes": [
            "Marinate chicken with olive oil, salt, pepper, and lemon juice for 30 mins.",
            "Grill both sides for 6-8 minutes until golden brown.",
            "Serve hot with veggies or rice.",
            "Boil chicken in salt water and shred for salads.",
            "Bake at 180°C for 25 minutes with herbs.",
            "Make chicken rolls with lettuce wraps.",
            "Prepare spicy tandoori chicken using yogurt and masala.",
            "Cook in air fryer for 10 mins for fat-free version.",
            "Add to pasta with tomato sauce.",
            "Use leftover chicken in egg scramble."
        ],
        "video": "https://www.youtube.com/watch?v=4gqdo6QmAqQ"
    },
    "Paneer": {
        "types": ["Grilled", "Curry", "Fried"],
        "nutrition": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
        "recipes": [
            "Cut paneer cubes and marinate in yogurt, turmeric, and chili powder.",
            "Grill both sides for 5 mins until golden.",
            "Add grilled paneer to salads or wraps.",
            "Cook paneer with onion-tomato gravy for curry.",
            "Add paneer to mixed veggies for a protein boost.",
            "Make paneer tikka on skewers.",
            "Use paneer in oats bowl for extra protein.",
            "Fry lightly and sprinkle chat masala.",
            "Mix paneer with spinach for Palak Paneer.",
            "Serve with brown rice for a balanced meal."
        ],
        "video": "https://www.youtube.com/watch?v=VYp8jV4AG5g"
    },
    "Egg": {
        "types": ["Boiled", "Scrambled", "Omelette"],
        "nutrition": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
        "recipes": [
            "Boil eggs for 6–8 mins and peel.",
            "Mash boiled eggs with salt, pepper, and chili flakes.",
            "Whisk eggs and make omelette with spinach and onion.",
            "Scramble eggs with tomato and herbs.",
            "Use boiled eggs in sandwiches.",
            "Prepare egg curry with coconut gravy.",
            "Add chopped eggs in salads.",
            "Make egg wrap with tortilla.",
            "Cook egg muffins in oven.",
            "Make deviled eggs for snacks."
        ],
        "video": "https://www.youtube.com/watch?v=3a4zRZsXKys"
    },
    "Oats": {
        "types": ["Porridge", "Overnight", "Protein Bowl"],
        "nutrition": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
        "recipes": [
            "Boil oats in milk for 5 mins.",
            "Add banana, honey, and nuts.",
            "Soak oats overnight with yogurt and chia seeds.",
            "Mix oats with whey and peanut butter for a protein bowl.",
            "Add apple slices and cinnamon for flavor.",
            "Blend oats with banana for pancake batter.",
            "Cook oats with water and salt for savory oats.",
            "Add almond milk for a vegan version.",
            "Top with berries for antioxidants.",
            "Mix oats with paneer for high protein meal."
        ],
        "video": "https://www.youtube.com/watch?v=4pU9pG0Gm9k"
    },
    "Fish": {
        "types": ["Grilled", "Curry", "Baked"],
        "nutrition": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
        "recipes": [
            "Marinate fish with lemon, garlic, and olive oil.",
            "Grill for 4 mins each side.",
            "Serve with rice and veggies.",
            "Make curry using coconut milk and spices.",
            "Bake with herbs for 20 mins at 180°C.",
            "Add to sandwiches or tacos.",
            "Pan fry with minimal oil.",
            "Prepare spicy masala fish.",
            "Serve with quinoa.",
            "Make fish soup for recovery meal."
        ],
        "video": "https://www.youtube.com/watch?v=OFO5I9rL0Ko"
    },
    "Protein Shake": {
        "types": ["Whey", "Vegan", "Mass Gainer"],
        "nutrition": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
        "recipes": [
            "Mix 1 scoop protein with water or milk.",
            "Add banana and oats for extra calories.",
            "Blend with peanut butter for bulking.",
            "Add spinach for a green shake.",
            "Use almond milk for dairy-free option.",
            "Mix cocoa powder for flavor.",
            "Add ice cubes for a chilled version.",
            "Use in smoothie bowls.",
            "Blend with coffee for pre-workout.",
            "Add honey for sweetness."
        ],
        "video": "https://www.youtube.com/watch?v=F7ZZIoB1bI0"
    }
}

# --------------------------
# 💡 AI IMAGE DETECTION MOCK
# --------------------------
def detect_ai_image(uploaded_image):
    return random.choice(["✅ 99% Real Image Detected", "⚠️ AI-Generated Image Suspected"])

# --------------------------
# 🍽 SIDEBAR: FOOD SELECTION
# --------------------------
st.sidebar.header("🍛 Select Your Meal")
food_choice = st.sidebar.selectbox("Choose Food Item", list(foods.keys()))
food_type = st.sidebar.selectbox("Choose Cooking Type", foods[food_choice]["types"])
grams = st.sidebar.number_input("Enter weight (in grams)", min_value=0, max_value=1000, value=100, step=10)
goal = st.sidebar.radio("Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

# --------------------------
# 📷 IMAGE UPLOAD + AI DETECTION
# --------------------------
uploaded_image = st.sidebar.file_uploader("📸 Upload your meal photo", type=["jpg", "png", "jpeg"])
if uploaded_image:
    st.image(uploaded_image, caption="Your uploaded meal", width=250)
    st.sidebar.success(detect_ai_image(uploaded_image))

# --------------------------
# ✅ SUBMIT BUTTON
# --------------------------
if st.sidebar.button("✅ Submit"):
    st.session_state.submitted = True

if "submitted" in st.session_state and st.session_state.submitted:
    st.success(f"You selected {grams}g of {food_choice} ({food_type}) for **{goal}** mode.")
    
    # Calculate Nutrition
    data = foods[food_choice]["nutrition"]
    calories = data["calories"] * grams / 100
    protein = data["protein"] * grams / 100
    fat = data["fat"] * grams / 100
    carbs = data["carbs"] * grams / 100

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # Recipes Section
    st.markdown("---")
    st.subheader("👨‍🍳 Recipes & Cooking Guide")

    with st.expander("📜 Step-by-Step Recipe Instructions"):
        for step in foods[food_choice]["recipes"]:
            st.markdown(f"- {step}")

    with st.expander("🎥 Watch Recipe Video (Optional)"):
        st.video(foods[food_choice]["video"])

st.caption("Built by Team Bro ❤️ | Powered by Streamlit")
