import streamlit as st
from datetime import datetime
import pytz

# -----------------------------
# Nutrition Database
# per 100g unless specified
# -----------------------------
FOODS = {
    "Chicken Breast": {"protein": 31, "carbs": 0, "fat": 3.6, "calories": 165},
    "Egg (per 1 egg)": {"protein": 6, "carbs": 0.6, "fat": 5.3, "calories": 75},
    "Rice (Cooked)": {"protein": 2.7, "carbs": 28, "fat": 0.3, "calories": 130},
    "Roti": {"protein": 3, "carbs": 15, "fat": 3, "calories": 120},
    "Paneer": {"protein": 18, "carbs": 1.2, "fat": 20, "calories": 265},
    "Oats": {"protein": 17, "carbs": 66, "fat": 7, "calories": 389},
    "Banana": {"protein": 1.3, "carbs": 27, "fat": 0.3, "calories": 105}
}

# Timezone for IST
IST = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(IST).strftime("%I:%M %p")

# Session storage for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# 🏋️ UI Design
# -----------------------------
st.set_page_config(page_title="Smart Nutrition Tracker", layout="wide")

with st.sidebar:
    st.markdown("🕒 **Current Time (IST):** " + current_time)
    st.title("🍽 Select Your Meal")

    food = st.selectbox("Food", list(FOODS.keys()))

    if "Egg" in food:
        qty = st.number_input("Number of Eggs", min_value=1, value=2)
        grams = None
    else:
        grams = st.number_input("Grams", min_value=10, step=10, value=100)
        qty = None

    goal = st.radio("Goal", ["Cutting", "Maintenance", "Bulking"])

    uploaded_photo = st.file_uploader("📸 Upload meal photo", type=["png", "jpg", "jpeg"])

    if st.button("✔ Submit"):
        st.success("Meal Added Successfully! Scroll right to view analysis")

# -----------------------------
# Main Title Page
# -----------------------------
st.markdown("<h1 style='text-align: center;'>💪 Smart Nutrition Tracker – Ultimate Gym Edition</h1>", unsafe_allow_html=True)
st.subheader("Built with ❤️ by Team Project Bro")

# -----------------------------
# Nutrition Calculation
# -----------------------------
if grams or qty:
    st.markdown("### 🧮 Meal Overview")

    data = FOODS[food]

    if qty:
        multiplier = qty  # eggs are per piece
    else:
        multiplier = grams / 100  # others per 100g

    protein = round(data["protein"] * multiplier, 1)
    carbs = round(data["carbs"] * multiplier, 1)
    fat = round(data["fat"] * multiplier, 1)
    calories = round(data["calories"] * multiplier, 1)

    st.write(f"🍗 **{food}**")
    if qty:
        st.write(f"🥚 Quantity: {qty} eggs")
    else:
        st.write(f"⚖️ Weight: {grams}g")

    st.metric("Protein", f"{protein} g")
    st.metric("Carbs", f"{carbs} g")
    st.metric("Fat", f"{fat} g")
    st.metric("Calories", f"{calories} kcal")

# -----------------------------
# 🤖 Nutrition Chatbot
# -----------------------------
st.markdown("---")
st.markdown("### 🤖 Nutrition Chat Assistant")

user_msg = st.text_input("Ask me anything about your food or diet:")

if user_msg:
    st.session_state.chat_history.append(("You", user_msg))

    bot_reply = f"Based on your goal **{goal}**: \n\n"

    if "protein" in user_msg.lower():
        bot_reply += "💡 Aim 1.8–2.2g protein per kg body weight daily.\n"
    if "egg" in user_msg.lower():
        bot_reply += "🥚 1 egg ≈ 6g protein, 75 calories.\n"
    if "chicken" in user_msg.lower():
        bot_reply += "🍗 100g chicken ≈ 31g protein.\n"

    if goal == "Cutting":
        bot_reply += "🔥 For cutting: Increase protein & reduce carbs after 6 PM."
    elif goal == "Bulking":
        bot_reply += "🍚 For bulking: Add rice/pasta & milk for calorie boost."
    else:
        bot_reply += "⚖️ Balanced macro intake is key for maintenance."

    st.session_state.chat_history.append(("Bot", bot_reply))

# Show chat messages
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑 **{role}:** {msg}")
    else:
        st.markdown(f"🤖 **{role}:** {msg}")
