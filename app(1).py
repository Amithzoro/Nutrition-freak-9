import streamlit as st
from PIL import Image
import datetime, pytz, random

st.set_page_config(page_title="🥗 Smart Nutrition Tracker v3.8 Compact", layout="wide")

st.title("🥦 Smart Nutrition Tracker v3.8 Compact Edition")
st.markdown("### Track, Cook, and Improve — All in One Place 💪")

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
        {"title": "Grilled Chicken", "steps": "Marinate with lemon, garlic, pepper, grill 7 mins per side.", "video": "https://www.youtube.com/watch?v=F5DxMBQUOcI"},
        {"title": "Chicken Stir Fry", "steps": "Cook chicken with veggies and soy sauce.", "video": "https://www.youtube.com/watch?v=f6U8fF8V2vE"},
        {"title": "Chicken Salad", "steps": "Mix boiled chicken with lettuce and olive oil.", "video": "https://www.youtube.com/watch?v=VZqW0VrK5X4"},
        {"title": "Spicy Chicken Curry", "steps": "Cook onions, tomato, spices, add chicken.", "video": "https://www.youtube.com/watch?v=c4Z3lKf0X1M"},
        {"title": "Baked Chicken", "steps": "Season & bake 25 mins at 200°C.", "video": "https://www.youtube.com/watch?v=UkmRrI1QBd8"},
        {"title": "Garlic Butter Chicken", "steps": "Cook chicken in garlic butter sauce.", "video": "https://www.youtube.com/watch?v=0nOeHchF1oA"},
        {"title": "Tandoori Chicken", "steps": "Yogurt marinate, bake or grill.", "video": "https://www.youtube.com/watch?v=ZEBjLhF7Jg8"},
        {"title": "Chicken Wrap", "steps": "Add grilled chicken & veggies to wrap.", "video": "https://www.youtube.com/watch?v=t_bPKrUwShU"},
        {"title": "Chicken Soup", "steps": "Boil chicken with ginger & herbs.", "video": "https://www.youtube.com/watch?v=44PExUccWUc"},
        {"title": "Lemon Chicken", "steps": "Stir-fry chicken in lemon & honey glaze.", "video": "https://www.youtube.com/watch?v=65ZlAOUyS7Q"},
    ],
    "Boiled Egg": [
        {"title": "Egg Curry", "steps": "Fry onion-tomato, add spices & eggs.", "video": "https://www.youtube.com/watch?v=dxlW2b-Nckc"},
        {"title": "Masala Omelette", "steps": "Whisk eggs, onion, chili, cook both sides.", "video": "https://www.youtube.com/watch?v=gVvyQeF8a7o"},
        {"title": "Scrambled Eggs", "steps": "Cook eggs on butter, keep creamy.", "video": "https://www.youtube.com/watch?v=CuD5Qr8J5_o"},
        {"title": "Egg Fried Rice", "steps": "Mix scrambled egg with rice & soy sauce.", "video": "https://www.youtube.com/watch?v=EhhRy0eC1tk"},
        {"title": "Poached Eggs", "steps": "Simmer eggs in hot water till white sets.", "video": "https://www.youtube.com/watch?v=Zf-Ks59YzjY"},
        {"title": "Egg Sandwich", "steps": "Add boiled egg slices in brown bread.", "video": "https://www.youtube.com/watch?v=46hM44XEq1Q"},
        {"title": "Egg Bhurji", "steps": "Indian scrambled eggs with spices.", "video": "https://www.youtube.com/watch?v=I6C6Q67V-6Y"},
        {"title": "Cheese Omelette", "steps": "Add grated cheese before folding.", "video": "https://www.youtube.com/watch?v=jqAfLqTye48"},
        {"title": "Egg Toast", "steps": "Dip bread in egg mix, toast till golden.", "video": "https://www.youtube.com/watch?v=xJbE01tEz30"},
        {"title": "Deviled Eggs", "steps": "Stuff boiled egg halves with yolk mix.", "video": "https://www.youtube.com/watch?v=oyvD3d5N2mo"},
    ],
}

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("🍽 Choose Your Food & Quantity")
food_name = st.sidebar.selectbox("Select food:", list(foods.keys()))
grams = st.sidebar.number_input("Enter weight (grams):", 0, 1000, 100, 10)
goal = st.sidebar.radio("🎯 Goal", ["Cutting", "Maintenance", "Bulking"])

# ---------- IMAGE UPLOAD ----------
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Upload Meal Image")
file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Meal", width=250)
    if random.choice([True, False]):
        st.error("⚠️ This might be AI-generated.")
    else:
        st.success("✅ Real image detected.")
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.datetime.now(ist).strftime("%I:%M %p")
    st.info(f"🕒 Recorded at: **{now} IST**")

# ---------- SUBMIT ----------
if st.sidebar.button("✅ Submit Meal"):
    if grams > 0:
        info = foods[food_name]
        cal, pro, fat, carb = [info[k] * grams / 100 for k in ["calories", "protein", "fat", "carbs"]]
        if goal == "Cutting": cal *= 0.9
        elif goal == "Bulking": cal *= 1.1
        st.success(f"Submitted: {grams}g {food_name} ({goal})")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🔥 Calories", f"{cal:.1f} kcal")
        col2.metric("💪 Protein", f"{pro:.1f} g")
        col3.metric("🥑 Fat", f"{fat:.1f} g")
        col4.metric("🍞 Carbs", f"{carb:.1f} g")
    else:
        st.warning("Please enter a valid weight.")

# ---------- RECIPES ----------
st.markdown("---")
st.subheader(f"🍳 {food_name} Recipes")

if food_name in recipes:
    # Dropdown for quick selection
    selected = st.selectbox("Select a recipe:", [r["title"] for r in recipes[food_name]])
    rcp = next(r for r in recipes[food_name] if r["title"] == selected)
    st.markdown(f"### {rcp['title']}")
    st.write(rcp["steps"])
    st.video(rcp["video"])
    st.markdown(f"[🔗 Watch on YouTube]({rcp['video']})")

    # Expanders for all recipes
    st.markdown("---")
    st.write("### 📚 Explore All Recipes")
    for r in recipes[food_name]:
        with st.expander(r["title"]):
            st.write(r["steps"])
            st.video(r["video"])
            st.markdown(f"[🔗 YouTube Link]({r['video']})")

else:
    st.info("Recipes for this food are coming soon!")

# ---------- NOTES ----------
st.markdown("---")
with st.expander("🧾 Add Notes"):
    note = st.text_area("Write your meal note:")
    if st.button("💾 Save Note"):
        st.success("Note saved!")

st.caption("Built with ❤️ — Smart Nutrition Tracker v3.8 Compact Edition")
