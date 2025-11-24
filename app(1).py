import streamlit as st
from datetime import datetime
import pytz

# ---------- APP CONFIG ----------
st.set_page_config(page_title="💪 Smart Nutrition Tracker", layout="wide")
st.title("🏋️‍♂️ Smart Nutrition Tracker – Ultimate Gym Edition")

# ---------- TIME (IST 12hr) ----------
ist = pytz.timezone("Asia/Kolkata")
st.sidebar.write("🕒 Current Time (IST): **{}**".format(datetime.now(ist).strftime("%I:%M %p")))

# ---------- SESSION STATE ----------
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "foods" not in st.session_state:
    st.session_state.foods = {
        "Chicken Breast": {"cal": 165, "pro": 31, "fat": 3.6, "carb": 0},
        "Paneer": {"cal": 265, "pro": 18, "fat": 21, "carb": 2.4},
        "Egg": {"cal": 78, "pro": 6, "fat": 5, "carb": 0.6},
        "Oats": {"cal": 389, "pro": 17, "fat": 7, "carb": 66},
        "Fish": {"cal": 206, "pro": 22, "fat": 12, "carb": 0},
        "Protein Shake": {"cal": 120, "pro": 24, "fat": 1, "carb": 3},
    }
if "last_meal" not in st.session_state:
    st.session_state.last_meal = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

foods = st.session_state.foods

# ---------- SIDEBAR: SELECT EXISTING FOOD OR ADD NEW ----------
st.sidebar.header("🍛 Select Your Meal")
choice = st.sidebar.radio("Choose Option", ["Select Food", "➕ Add New Food"])

if choice == "➕ Add New Food":
    st.sidebar.subheader("Add Food Nutrition per 100g")
    new_name = st.sidebar.text_input("Food Name")
    cal = st.sidebar.number_input("Calories", 0.0, 2000.0, 0.0, 1.0)
    pro = st.sidebar.number_input("Protein", 0.0, 200.0, 0.0, 0.1)
    fat = st.sidebar.number_input("Fat", 0.0, 200.0, 0.0, 0.1)
    carb = st.sidebar.number_input("Carbs", 0.0, 200.0, 0.0, 0.1)

    if st.sidebar.button("💾 Save Food"):
        if new_name != "" and cal > 0:
            st.session_state.foods[new_name] = {"cal": cal, "pro": pro, "fat": fat, "carb": carb}
            st.sidebar.success(f"{new_name} added successfully!")
        else:
            st.sidebar.error("Enter valid food and calories.")

else:
    food = st.sidebar.selectbox("Food", list(foods.keys()))

    if food == "Egg":
        egg_count = st.sidebar.number_input("Number of Eggs", 0, 20, 1, 1)
        grams = None
    else:
        grams = st.sidebar.number_input("Grams", 0, 1000, 100, 10)
        egg_count = None

    goal = st.sidebar.radio("Goal", ["Cutting", "Maintenance", "Bulking"])
    if st.sidebar.button("✅ Submit"):
        st.session_state.submitted = True

# ---------- RESULTS ----------
if st.session_state.submitted and choice == "Select Food":
    data = foods[food]

    if food == "Egg":
        total_cal = data["cal"] * egg_count
        total_pro = data["pro"] * egg_count
        total_fat = data["fat"] * egg_count
        total_carb = data["carb"] * egg_count
        st.session_state.last_meal = (food, f"{egg_count} Eggs", total_cal, total_pro)
        st.success(f"{egg_count} Eggs — **{goal} Mode**")
    else:
        total_cal = data["cal"] * grams / 100
        total_pro = data["pro"] * grams / 100
        total_fat = data["fat"] * grams / 100
        total_carb = data["carb"] * grams / 100
        st.session_state.last_meal = (food, f"{grams} g", total_cal, total_pro)
        st.success(f"{grams} g of {food} — **{goal} Mode**")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 Calories", f"{total_cal:.1f}")
    c2.metric("💪 Protein", f"{total_pro:.1f} g")
    c3.metric("🥑 Fat", f"{total_fat:.1f} g")
    c4.metric("🍞 Carbs", f"{total_carb:.1f} g")

st.markdown("---")

# ---------- CHATBOT ----------
st.subheader("🤖 AI Nutrition Chatbot")

def chatbot_reply(msg):
    msg = msg.lower()

    # last meal data
    last = st.session_state.last_meal

    if "last" in msg and last:
        food, qty, cal, pro = last
        return f"Your last meal was **{qty} of {food}** providing **{cal:.1f} calories** and **{pro:.1f} g protein**."

    if "protein" in msg:
        return "To build muscle, try to target 1.8 – 2.2 g protein per kg body weight per day."

    if "calorie" in msg:
        return "For cutting choose calorie deficit. For bulking choose 300–400 kcal surplus."

    if "what to eat" in msg or "suggest" in msg:
        return "Good choices now: Chicken Breast, Eggs, Fish, Paneer, Oats & Protein Shake."

    if "hello" in msg or "hi" in msg:
        return "Hello chief! 💪 Tell me what you ate or ask anything about nutrition."

    return "Got it! 💡 Tell me your meal or nutrition question — I'm here to guide you."

# message input
user_msg = st.text_input("💬 Ask anything about food & nutrition:")

if st.button("Send"):
    if user_msg.strip() != "":
        st.session_state.chat_history.append(("user", user_msg))
        bot = chatbot_reply(user_msg)
        st.session_state.chat_history.append(("bot", bot))

# chatbox display
for sender, text in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"🧍 **You:** {text}")
    else:
        st.markdown(f"🤖 **Bot:** {text}")

st.caption("Built with ❤️ | Team Project Bro")
