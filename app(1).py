import streamlit as st
import json
from datetime import datetime
import pytz

st.set_page_config(page_title="Smart Nutrition Tracker", layout="wide")

# ---------------------------- Storage Helpers ----------------------------
def load_history():
    if "history" not in st.session_state:
        st.session_state.history = {"meals": [], "water": 0}
    return st.session_state.history

def save_meal(food, grams, protein, calories, goal):
    hist = load_history()
    hist["meals"].append({
        "food": food,
        "grams": grams,
        "protein": protein,
        "calories": calories,
        "goal": goal,
        "time": datetime.now().strftime("%I:%M %p")
    })

def export_data():
    return json.dumps(load_history())

def import_data(data):
    st.session_state.history = json.loads(data)

# ---------------------------- Food Database ----------------------------
foods = {
    "Chicken Breast": {"cal": 165, "pro": 31},
    "Egg": {"cal": 78, "pro": 6},
    "Paneer": {"cal": 265, "pro": 18},
    "Oats": {"cal": 389, "pro": 17},
    "Fish": {"cal": 206, "pro": 22},
    "Protein Shake": {"cal": 120, "pro": 24},
}

goals_reply = {
    "Cutting": "Eat high protein and low carbs after 6 PM. Avoid sugar & fried food.",
    "Bulking": "Increase calories + 1 heavy meal before bed. Aim 1.6–2g protein per kg body weight.",
    "Lean Muscle": "Balanced macros. Cardio 20 mins + strength 1 hr. Maintain calorie deficit."
}

# ---------------------------- Login ----------------------------
if "logged" not in st.session_state:
    st.title("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user and pwd:
            st.session_state.logged = True
            st.session_state.username = user
            st.rerun()
        else:
            st.error("Enter username and password")
    st.stop()

# ---------------------------- Main App ----------------------------
st.sidebar.title(f"👋 Welcome {st.session_state.username}")
page = st.sidebar.radio("Navigate", ["🏠 Dashboard", "🍽 Log Meal", "💬 AI Nutrition Chat", "💧 Water Tracker", "📁 Backup & Restore"])

# ---------------------------- Dashboard ----------------------------
if page == "🏠 Dashboard":
    hist = load_history()
    total_cal = sum(m["calories"] for m in hist["meals"])
    total_pro = sum(m["protein"] for m in hist["meals"])

    st.header("📊 Today Summary")
    c1, c2 = st.columns(2)
    c1.metric("🔥 Total Calories", f"{total_cal:.1f}")
    c2.metric("💪 Total Protein", f"{total_pro:.1f} g")
    st.write("---")

    st.subheader("🍽 Meal History")
    for m in hist["meals"][::-1]:
        st.write(f"🕒 {m['time']} — {m['food']} {m['grams']}g — **{m['calories']} cal / {m['protein']}g protein** — ({m['goal']})")

# ---------------------------- Log Meal ----------------------------
if page == "🍽 Log Meal":
    st.header("🍱 Add a Meal")
    food = st.selectbox("Food", list(foods.keys()))
    grams = st.number_input("Grams", 1, 2000, 100)
    eggs = 0
    if food == "Egg":
        eggs = st.number_input("Number of eggs", 1, 12, 2)

    goal = st.radio("Goal", ["Cutting", "Bulking", "Lean Muscle"])

    if st.button("Save Meal"):
        cal = foods[food]["cal"] * grams / 100
        pro = foods[food]["pro"] * grams / 100
        if food == "Egg":
            cal = foods[food]["cal"] * eggs
            pro = foods[food]["pro"] * eggs

        save_meal(food, grams if food != "Egg" else eggs, pro, cal, goal)
        st.success(f"Saved! {cal:.1f} cal / {pro:.1f}g protein")

# ---------------------------- AI Chat ----------------------------
if page == "💬 AI Nutrition Chat":
    st.header("🤖 Nutrition Chat Assistant")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_msg = st.text_input("Ask me anything about your food or diet:")

    if st.button("Send") and user_msg:
        st.session_state.chat.append(("user", user_msg))
        
        reply = "I didn't understand completely, but keep eating high protein meals!"
        hist = load_history()
        total_cal = sum(m["calories"] for m in hist["meals"])
        total_pro = sum(m["protein"] for m in hist["meals"])

        if "calorie" in user_msg.lower():
            reply = f"You currently consumed {total_cal:.1f} calories today."

        if "protein" in user_msg.lower():
            reply = f"You have taken {total_pro:.1f} grams of protein today."

        if "lost fat" in user_msg.lower() or "cutting" in user_msg.lower():
            reply = goals_reply["Cutting"]

        if "bulking" in user_msg.lower():
            reply = goals_reply["Bulking"]

        if "lean" in user_msg.lower():
            reply = goals_reply["Lean Muscle"]

        st.session_state.chat.append(("bot", reply))

    for sender, msg in st.session_state.chat[::-1]:
        st.write(f"**{'🧑 You' if sender=='user' else '🤖 Bot'}:** {msg}")

# ---------------------------- Water Tracker ----------------------------
if page == "💧 Water Tracker":
    hist = load_history()
    st.header("💦 Water Intake")

    st.metric("💧 Water drunk today", f"{hist['water']} ml")
    add = st.number_input("Add water (ml)", 0, 2000, 250)

    if st.button("Add"):
        hist["water"] += add
        st.success(f"Added {add} ml")

# ---------------------------- Backup & Restore ----------------------------
if page == "📁 Backup & Restore":
    st.header("📦 Save or Restore")

    if st.button("Download Backup"):
        st.download_button("Download", export_data(), "nutrition_backup.json")

    uploaded = st.file_uploader("Upload backup JSON")
    if uploaded:
        data = uploaded.read().decode()
        import_data(data)
        st.success("Backup restored successfully!")
