import streamlit as st
from datetime import datetime
import pytz

# ----------------------------
# SMART NUTRITION TRACKER V6.0
# ----------------------------
st.set_page_config(page_title="💪 Smart Nutrition Tracker v6.0 – Pro Athlete Edition", layout="wide")

st.title("💪 Smart Nutrition Tracker – Pro Athlete Edition")
st.markdown("### Fuel smarter. Train harder. Track like a pro 🥗")

# --- Indian Time ---
india = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(india).strftime("%I:%M %p")

# --- Fitness Goal ---
goal = st.sidebar.radio("🎯 Select your fitness goal:", ["Cutting", "Maintenance", "Bulking"])

# --- Food Database ---
foods = {
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Egg (Boiled)": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Lentils (Cooked)": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Whey Protein": {"calories": 120, "protein": 24, "fat": 1, "carbs": 3},
    "Greek Yogurt": {"calories": 59, "protein": 10, "fat": 0.4, "carbs": 3.6},
    "Peanut Butter": {"calories": 588, "protein": 25, "fat": 50, "carbs": 20},
    "Chickpeas": {"calories": 164, "protein": 9, "fat": 2.6, "carbs": 27},
    "Prawns": {"calories": 99, "protein": 24, "fat": 0.3, "carbs": 0.2},
    "Protein Bar": {"calories": 250, "protein": 20, "fat": 8, "carbs": 30},
    "Sweet Potato": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
}

# --- Sidebar Inputs ---
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select food item:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (grams):", min_value=0, max_value=1000, value=100, step=10)
uploaded_file = st.sidebar.file_uploader("📸 Upload your meal image (optional):", type=["jpg", "png"])

# --- Mock AI Detection ---
if uploaded_file:
    st.sidebar.image(uploaded_file, caption="Uploaded Meal", use_container_width=True)
    st.sidebar.info("🤖 AI Detection (Mock): Looks like a high-protein meal!")

# --- Initialize Meal History ---
if "history" not in st.session_state:
    st.session_state["history"] = []

# --- Submit Button ---
if st.sidebar.button("✅ Submit"):
    info = foods[food_name]
    base_calories = info["calories"] * grams / 100
    protein = info["protein"] * grams / 100
    fat = info["fat"] * grams / 100
    carbs = info["carbs"] * grams / 100

    # Apply Goal-Based Adjustments
    if goal == "Cutting":
        calories = base_calories * 0.8
    elif goal == "Bulking":
        calories = base_calories * 1.15
    else:
        calories = base_calories

    st.success(f"**{grams}g of {food_name} logged successfully!**")
    st.write(f"🕐 **Time (IST):** {current_time}")
    st.write(f"🎯 Goal: {goal}")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔥 Calories", f"{calories:.1f} kcal")
    col2.metric("💪 Protein", f"{protein:.1f} g")
    col3.metric("🥑 Fat", f"{fat:.1f} g")
    col4.metric("🍞 Carbs", f"{carbs:.1f} g")

    # Add to history
    st.session_state["history"].append(
        {"Food": food_name, "Grams": grams, "Calories": calories, "Protein": protein, "Time": current_time, "Goal": goal}
    )

    # View Recipes & Videos
    if st.button("🍳 View Recipes & Videos"):
        recipes = {
            "Chicken Breast": [
                ("Grilled Chicken", "https://www.youtube.com/watch?v=4vRzDpJ-L9A"),
                ("Chicken Curry", "https://www.youtube.com/watch?v=Wy4U5J0lYtY"),
                ("Chicken Tikka", "https://www.youtube.com/watch?v=KNEb5Z4lRz4"),
                ("Chicken Wrap", ""),
                ("Baked Chicken", ""),
                ("Lemon Garlic Chicken", ""),
                ("Spicy Chicken Fry", ""),
                ("Chicken Salad", ""),
                ("Steamed Chicken", ""),
                ("Chicken Quinoa Bowl", ""),
            ],
            "Egg (Boiled)": [
                ("Egg Curry", "https://www.youtube.com/watch?v=s1bknh9XspE"),
                ("Scrambled Eggs", "https://www.youtube.com/watch?v=J7p8P3gdWJY"),
                ("Omelette", ""),
                ("Egg Sandwich", ""),
                ("Egg Salad", ""),
                ("Egg Fried Rice", ""),
                ("Egg Bhurji", ""),
                ("Egg Wrap", ""),
                ("Poached Egg", ""),
                ("Deviled Eggs", ""),
            ],
            "Paneer": [
                ("Paneer Tikka", "https://www.youtube.com/watch?v=6xUwN0GJXIU"),
                ("Paneer Bhurji", "https://www.youtube.com/watch?v=f0L0DptYz7A"),
                ("Paneer Wrap", ""),
                ("Paneer Curry", ""),
                ("Grilled Paneer Salad", ""),
                ("Paneer Stir Fry", ""),
                ("Chilli Paneer", ""),
                ("Paneer Sandwich", ""),
                ("Paneer Kebab", ""),
                ("Paneer Rice Bowl", ""),
            ],
            "Oats": [
                ("Oats Pancakes", "https://www.youtube.com/watch?v=xZVh2Uu6W5Y"),
                ("Oats Smoothie", ""),
                ("Overnight Oats", ""),
                ("Oats Upma", ""),
                ("Oats Cookies", ""),
                ("Oats Idli", ""),
                ("Oats Muffins", ""),
                ("Oats Dosa", ""),
                ("Oats Protein Bar", ""),
                ("Oats Bowl", ""),
            ],
            "Whey Protein": [
                ("Chocolate Whey Shake", "https://www.youtube.com/watch?v=dvQDaWj1gkM"),
                ("Peanut Butter Shake", ""),
                ("Banana Smoothie", ""),
                ("Oats Protein Shake", ""),
                ("Coffee Shake", ""),
                ("Vanilla Shake", ""),
                ("Berry Shake", ""),
                ("Mass Gainer Shake", ""),
                ("Green Protein Smoothie", ""),
                ("Ice Cream Shake", ""),
            ],
            # Simplified 10-text recipes for other foods
            "Fish (Grilled)": [("Fish Curry", ""), ("Baked Fish", ""), ("Fish Salad", ""), ("Lemon Fish", ""), ("Fish Wrap", ""), ("Fish Soup", ""), ("Spicy Fry", ""), ("Herb Fish", ""), ("Fish Bowl", ""), ("Fish Tacos", "")],
            "Tofu": [("Tofu Curry", ""), ("Grilled Tofu", ""), ("Tofu Salad", ""), ("Tofu Wrap", ""), ("Tofu Stir Fry", ""), ("Tofu Fried Rice", ""), ("Tofu Scramble", ""), ("Tofu Soup", ""), ("Crispy Tofu", ""), ("Tofu Bowl", "")],
            "Lentils (Cooked)": [("Dal Fry", ""), ("Lentil Soup", ""), ("Lentil Curry", ""), ("Lentil Wrap", ""), ("Masoor Dal", ""), ("Moong Dal", ""), ("Lentil Rice", ""), ("Spicy Dal", ""), ("Lentil Bowl", ""), ("Dal Tadka", "")],
            "Greek Yogurt": [("Yogurt Parfait", ""), ("Honey Yogurt", ""), ("Yogurt Smoothie", ""), ("Greek Yogurt Dip", ""), ("Frozen Yogurt", ""), ("Yogurt Chia Bowl", ""), ("Yogurt Oats", ""), ("Protein Yogurt Mix", ""), ("Yogurt Bowl", ""), ("Cucumber Dip", "")],
            "Peanut Butter": [("PB Banana Toast", ""), ("PB Smoothie", ""), ("PB Cookies", ""), ("PB Pancakes", ""), ("PB Yogurt Mix", ""), ("PB Brownie", ""), ("PB Energy Bar", ""), ("PB Sandwich", ""), ("PB Oat Bowl", ""), ("PB Protein Balls", "")],
            "Chickpeas": [("Chickpea Curry", ""), ("Hummus", ""), ("Chickpea Salad", ""), ("Roasted Chickpeas", ""), ("Chickpea Wrap", ""), ("Chickpea Soup", ""), ("Chickpea Rice", ""), ("Chickpea Bowl", ""), ("Chickpea Tacos", ""), ("Spicy Chickpeas", "")],
            "Prawns": [("Prawn Curry", ""), ("Grilled Prawns", ""), ("Prawn Salad", ""), ("Prawn Wrap", ""), ("Prawn Fried Rice", ""), ("Prawn Soup", ""), ("Spicy Prawns", ""), ("Lemon Garlic Prawns", ""), ("Prawn Pasta", ""), ("Prawn Bowl", "")],
            "Protein Bar": [("Chocolate Bar", ""), ("Oats Bar", ""), ("Peanut Butter Bar", ""), ("Coconut Bar", ""), ("Nutty Bar", ""), ("Banana Bar", ""), ("Almond Bar", ""), ("Protein Brownie", ""), ("No-Bake Bar", ""), ("Crispy Bar", "")],
            "Sweet Potato": [("Baked Sweet Potato", ""), ("Sweet Potato Fries", ""), ("Sweet Potato Curry", ""), ("Sweet Potato Soup", ""), ("Sweet Potato Pancake", ""), ("Sweet Potato Bowl", ""), ("Sweet Potato Smoothie", ""), ("Sweet Potato Salad", ""), ("Sweet Potato Toast", ""), ("Sweet Potato Chips", "")]
        }

        for recipe_name, video_link in recipes.get(food_name, []):
            with st.expander(f"🍴 {recipe_name}"):
                st.write(f"**How to cook {recipe_name}:**")
                st.write("1️⃣ Prepare ingredients.\n2️⃣ Cook on medium heat.\n3️⃣ Adjust seasoning.\n4️⃣ Serve hot and enjoy!\n")
                if video_link:
                    st.video(video_link)

# --- Meal History Section ---
if st.session_state["history"]:
    st.markdown("---")
    st.subheader("📅 Today's Meal History")
    st.table(st.session_state["history"])

st.markdown("---")
st.caption("Built with ❤️ by You & GPT — Smart Nutrition Tracker v6.0 Pro Athlete Edition")
