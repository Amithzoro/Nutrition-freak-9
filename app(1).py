import streamlit as st
from datetime import datetime
import pytz

# ----------------------------
# App Configuration
# ----------------------------
st.set_page_config(page_title="🥦 Smart Nutrition Calculator", layout="wide")
st.title("🥗 Smart Nutrition Calculator")
st.markdown("### Track your meals like a pro — simple, accurate, and fast!")

# ----------------------------
# Food Database (Veg + Non-Veg)
# ----------------------------
foods = {
    "Chicken": {
        "types": {
            "Grilled": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
            "Fried": {"calories": 250, "protein": 28, "fat": 12, "carbs": 6},
            "Boiled": {"calories": 150, "protein": 30, "fat": 2, "carbs": 0}
        },
        "recipes": [
            "Marinate with salt, pepper, and olive oil → grill for 8–10 min per side.",
            "Boil with spices → shred for salads or wraps.",
            "Stir-fry with veggies for a protein-packed meal.",
            "Air fry for crispy low-fat chicken.",
            "Bake with lemon and herbs at 180°C for 25 mins.",
            "Pan-sear with garlic butter and thyme.",
            "Add to pasta for creamy chicken Alfredo.",
            "Grill with BBQ sauce for smoky flavor.",
            "Shred and add to soup for muscle recovery.",
            "Make high-protein chicken sandwich with oats bread."
        ],
        "videos": [
            "https://www.youtube.com/watch?v=4oJq6j1bH9Q",
            "https://www.youtube.com/watch?v=PPfJ1r5n8Ro",
            "https://www.youtube.com/watch?v=JzjGqJH7Ogo"
        ]
    },
    "Egg": {
        "types": {
            "Boiled": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
            "Scrambled": {"calories": 90, "protein": 6.3, "fat": 7, "carbs": 1},
            "Omelette": {"calories": 100, "protein": 7, "fat": 8, "carbs": 1.2}
        },
        "recipes": [
            "Boil eggs for 7 minutes → peel → season with salt and pepper.",
            "Scramble eggs with milk and veggies for extra nutrients.",
            "Make omelette with spinach and cheese.",
            "Fry with minimal oil for high-protein snack.",
            "Add boiled eggs to salad.",
            "Cook egg bhurji with onion and tomato.",
            "Prepare egg sandwich with multigrain bread.",
            "Make deviled eggs with Greek yogurt filling.",
            "Add to ramen for post-gym protein.",
            "Mix boiled eggs with oats for morning breakfast."
        ],
        "videos": [
            "https://www.youtube.com/watch?v=JbnXykUYqYw",
            "https://www.youtube.com/watch?v=DNfLvJ4zAY8",
            "https://www.youtube.com/watch?v=F5-YqLJbqRE"
        ]
    },
    "Oats": {
        "types": {
            "Porridge": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
            "Overnight": {"calories": 350, "protein": 14, "fat": 6, "carbs": 60}
        },
        "recipes": [
            "Boil oats with milk and honey for 5 mins.",
            "Add banana, nuts, and peanut butter for energy.",
            "Soak overnight oats with chia seeds.",
            "Blend oats with whey protein for shake.",
            "Bake into oats muffins.",
            "Make oats upma with veggies.",
            "Mix with curd for savory breakfast.",
            "Oats + egg = high-protein pancakes.",
            "Add cocoa powder for chocolate oats.",
            "Layer with yogurt and fruits for parfait."
        ],
        "videos": [
            "https://www.youtube.com/watch?v=QnWcHR2v3io",
            "https://www.youtube.com/watch?v=rVn1XyTnK2E"
        ]
    },
    # Add more foods here later...
}

# ----------------------------
# Sidebar UI
# ----------------------------
st.sidebar.header("🍽 Choose Your Meal")

food_name = st.sidebar.selectbox("Select Food Item:", list(foods.keys()), index=None, placeholder="Select a food")

if food_name:
    food_data = foods[food_name]
    food_type = st.sidebar.selectbox(
        "Select Cooking Type:",
        list(food_data["types"].keys()),
        index=None,
        placeholder="Select type (e.g., Boiled, Fried)"
    )

    if food_type:
        grams = st.sidebar.number_input("Enter Weight (in grams):", min_value=0, max_value=1000, value=100, step=10)

        goal = st.sidebar.radio("🎯 Select Your Goal:", ["Cutting", "Maintenance", "Bulking"])
        image = st.sidebar.file_uploader("📸 Upload Food Image (optional):", type=["jpg", "jpeg", "png"])
        submit = st.sidebar.button("✅ Submit")

        if submit:
            info = food_data["types"][food_type]
            calories = info["calories"] * grams / 100
            protein = info["protein"] * grams / 100
            fat = info["fat"] * grams / 100
            carbs = info["carbs"] * grams / 100

            st.success(f"### 🍱 You selected {grams}g of {food_name} ({food_type})")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🔥 Calories", f"{calories:.1f} kcal")
            col2.metric("💪 Protein", f"{protein:.1f} g")
            col3.metric("🥑 Fat", f"{fat:.1f} g")
            col4.metric("🍞 Carbs", f"{carbs:.1f} g")

            # Show local Indian time
            india_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M %p")
            st.info(f"🕒 Meal logged at: **{india_time} (IST)**")

            # Recipes
            with st.expander("👨‍🍳 Show Recipes & Cooking Steps"):
                st.markdown("### 🥣 Step-by-step Recipes:")
                for i, recipe in enumerate(food_data["recipes"], start=1):
                    st.write(f"{i}. {recipe}")

                st.markdown("### 🎥 Cooking Videos (Optional):")
                for vid in food_data["videos"]:
                    st.video(vid)

else:
    st.sidebar.info("👈 Select a food item to begin!")

st.caption("Built with ❤️ using Streamlit | v6.4 Ultimate Edition")
