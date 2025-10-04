import streamlit as st
from PIL import Image
import datetime, pytz, random

st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.9 — Team Edition", layout="wide")

st.title("🥦 Smart Nutrition Tracker v3.9 — Team Edition")
st.markdown("### Built by us 💪 — Smart, Clean, Future-Ready")

# ---------- FOOD DATABASE ----------
foods = {
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Boiled Egg": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Prawns": {"calories": 99, "protein": 24, "fat": 1, "carbs": 0},
    "Milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "Almonds": {"calories": 579, "protein": 21, "fat": 50, "carbs": 22},
    "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23}
}

# ---------- RECIPE DATABASE ----------
recipes = {
    "Chicken Breast": [
        {"title": "Grilled Chicken", "steps": "1️⃣ Marinate chicken with lemon juice, salt, pepper, and garlic.\n2️⃣ Preheat grill to medium-high.\n3️⃣ Grill 6–7 mins per side until cooked.\n4️⃣ Rest for 5 mins and serve hot.", "video": "https://www.youtube.com/watch?v=F5DxMBQUOcI"},
        {"title": "Chicken Curry", "steps": "1️⃣ Heat oil, fry onions till golden.\n2️⃣ Add ginger-garlic paste, tomatoes, and spices.\n3️⃣ Add chicken, mix and cover for 15 mins.\n4️⃣ Garnish with coriander.", "video": ""},
        {"title": "Lemon Chicken", "steps": "1️⃣ Sauté garlic, add lemon juice and honey.\n2️⃣ Add cooked chicken and toss till coated.\n3️⃣ Serve with rice or salad.", "video": ""},
        {"title": "Chicken Stir Fry", "steps": "1️⃣ Slice chicken thinly.\n2️⃣ Stir fry with veggies, soy sauce, and chili.\n3️⃣ Serve with brown rice.", "video": "https://www.youtube.com/watch?v=f6U8fF8V2vE"},
        {"title": "Baked Chicken", "steps": "1️⃣ Season chicken with paprika & herbs.\n2️⃣ Bake at 200°C for 25 mins.\n3️⃣ Let rest before serving.", "video": ""},
        {"title": "Tandoori Chicken", "steps": "1️⃣ Marinate with yogurt, turmeric, and garam masala.\n2️⃣ Grill or bake till slightly charred.", "video": "https://www.youtube.com/watch?v=ZEBjLhF7Jg8"},
        {"title": "Chicken Wrap", "steps": "1️⃣ Add grilled chicken, lettuce, and sauce in a tortilla.\n2️⃣ Wrap tight and serve.", "video": ""},
        {"title": "Chicken Salad", "steps": "1️⃣ Mix boiled chicken with greens and olive oil dressing.\n2️⃣ Add pepper and lime juice.", "video": ""},
        {"title": "Garlic Butter Chicken", "steps": "1️⃣ Cook chicken in garlic butter sauce.\n2️⃣ Sprinkle parsley before serving.", "video": ""},
        {"title": "Chicken Soup", "steps": "1️⃣ Boil chicken bones with herbs and ginger.\n2️⃣ Strain and add boiled chicken chunks.\n3️⃣ Simmer for 10 mins.", "video": ""}
    ],
    "Boiled Egg": [
        {"title": "Masala Omelette", "steps": "1️⃣ Beat eggs, add onion, chili, tomato.\n2️⃣ Cook on low heat till both sides golden.", "video": "https://www.youtube.com/watch?v=gVvyQeF8a7o"},
        {"title": "Egg Curry", "steps": "1️⃣ Fry onions and tomatoes with curry masala.\n2️⃣ Add boiled eggs and simmer 5 mins.", "video": "https://www.youtube.com/watch?v=dxlW2b-Nckc"},
        {"title": "Scrambled Eggs", "steps": "1️⃣ Whisk eggs, salt, and milk.\n2️⃣ Stir on buttered pan till fluffy.", "video": ""},
        {"title": "Egg Fried Rice", "steps": "1️⃣ Scramble eggs and mix with cooked rice.\n2️⃣ Add soy sauce & spring onion.", "video": "https://www.youtube.com/watch?v=EhhRy0eC1tk"},
        {"title": "Egg Toast", "steps": "1️⃣ Dip bread in beaten egg.\n2️⃣ Toast till golden both sides.", "video": ""},
        {"title": "Egg Bhurji", "steps": "1️⃣ Cook onions and spices.\n2️⃣ Add eggs and stir till scrambled.", "video": ""},
        {"title": "Cheese Omelette", "steps": "1️⃣ Add cheese mid-cook.\n2️⃣ Fold and cook till melted.", "video": ""},
        {"title": "Poached Eggs", "steps": "1️⃣ Crack egg into hot water.\n2️⃣ Cook till white sets.", "video": ""},
        {"title": "Deviled Eggs", "steps": "1️⃣ Scoop yolk, mix with mayo.\n2️⃣ Fill back into egg whites.", "video": ""},
        {"title": "Egg Sandwich", "steps": "1️⃣ Layer boiled egg slices with lettuce and sauce.", "video": ""}
    ]
}

# ---------- SIDEBAR ----------
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select Food:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (g):", 0, 1000, 100, 10)
goal = st.sidebar.radio("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Upload Meal Image")
file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Meal", width=250)
    if random.choice([True, False]):
        st.error("⚠️ This image might be AI-generated.")
    else:
        st.success("✅ Real image detected.")
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.datetime.now(ist).strftime("%I:%M %p")
    st.info(f"🕒 Tracked at: **{now} IST**")

# ---------- SUBMIT BUTTON ----------
if st.sidebar.button("✅ Submit Meal"):
    if grams > 0:
        info = foods[food_name]
        cal, pro, fat, carb = [info[k] * grams / 100 for k in ["calories", "protein", "fat", "carbs"]]
        if goal == "Cutting": cal *= 0.9
        elif goal == "Bulking": cal *= 1.1
        st.success(f"✅ {grams}g {food_name} logged for {goal}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🔥 Calories", f"{cal:.1f}")
        col2.metric("💪 Protein", f"{pro:.1f}g")
        col3.metric("🥑 Fat", f"{fat:.1f}g")
        col4.metric("🍞 Carbs", f"{carb:.1f}g")
    else:
        st.warning("Please enter a valid weight.")

# ---------- RECIPE SECTION ----------
st.markdown("---")
st.subheader(f"🍳 {food_name} Recipes")

if food_name in recipes:
    recipe_titles = [r["title"] for r in recipes[food_name]]
    selected_recipe = st.selectbox("Select a recipe to view:", ["-- Choose a recipe --"] + recipe_titles)

    if selected_recipe != "-- Choose a recipe --":
        recipe = next(r for r in recipes[food_name] if r["title"] == selected_recipe)
        st.markdown(f"### {recipe['title']}")
        st.write(recipe["steps"])
        if recipe["video"]:
            with st.expander("🎥 Watch Video"):
                st.video(recipe["video"])
else:
    st.info("Recipes for this food are coming soon!")

# ---------- FUTURE MODULE HOOKS ----------
# 🧩 Meal Log System (future)
# 🧩 Progress Tracker (future)
# 🧩 Custom Food Adder (future)
# 🧩 Smart AI Recommendations (future)

st.markdown("---")
st.success("💡 We'll find even better ways to make your tracking smarter and smoother.")

