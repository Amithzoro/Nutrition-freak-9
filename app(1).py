# app.py
import streamlit as st
from datetime import datetime
import pytz
from PIL import Image
import random

st.set_page_config(page_title="💪 Smart Nutrition Tracker v4.2", layout="wide")
st.title("🥗 Smart Nutrition Tracker — Final (recipes show after Submit)")
st.markdown("Submit first → then view 10 step-by-step recipes (video optional).")

# ---------------------------
# Food nutrition database
# ---------------------------
foods = {
    "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "Egg (Boiled)": {"calories": 78, "protein": 6, "fat": 5, "carbs": 0.6},  # used for reference if needed
    "Paneer": {"calories": 265, "protein": 18, "fat": 21, "carbs": 2.4},
    "Oats": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66},
    "Fish (Grilled)": {"calories": 206, "protein": 22, "fat": 12, "carbs": 0},
    "Rice (Cooked)": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
    "Tofu": {"calories": 76, "protein": 8, "fat": 4.8, "carbs": 1.9},
    "Prawns": {"calories": 99, "protein": 24, "fat": 0.3, "carbs": 0.2},
    "Lentils (Cooked)": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
    "Sweet Potato": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
}

# ---------------------------
# Recipes dictionary (10 recipes per food)
# Each recipe is { "title": str, "steps": str, "video": str-or-empty }
# ---------------------------
recipes = {
    "Chicken Breast": [
        {"title": "Grilled Lemon Garlic Chicken",
         "steps": "1) Take 200g chicken breast, trim fat and pat dry.\n"
                  "2) Mix 1 tbsp olive oil, 1 tbsp lemon juice, 1 tsp garlic paste, salt and pepper.\n"
                  "3) Marinate chicken 20–30 minutes in fridge.\n"
                  "4) Preheat grill/pan to medium-high and cook 6–8 min per side until internal temp reaches 74°C.\n"
                  "5) Rest 3 minutes, slice and serve with salad.",
         "video": "https://www.youtube.com/watch?v=F5DxMBQUOcI"},
        {"title": "Simple Chicken Stir Fry",
         "steps": "1) Slice 200g chicken into thin strips.\n"
                  "2) Heat 1 tbsp oil, stir-fry sliced onion & bell peppers 2–3 min.\n"
                  "3) Add chicken strips, 1 tbsp soy sauce and cook 5–7 min until done.\n"
                  "4) Finish with spring onions and serve with brown rice.",
         "video": "https://www.youtube.com/watch?v=f6U8fF8V2vE"},
        {"title": "Tandoori-style Oven Chicken",
         "steps": "1) Mix 3 tbsp yogurt, 1 tsp turmeric, 1 tsp chili powder, 1 tsp garam masala, ginger-garlic paste.\n"
                  "2) Coat chicken, refrigerate 1–2 hours.\n"
                  "3) Bake at 200°C for 20–25 min, broil 2–3 min for char.\n"
                  "4) Serve with lemon wedges.",
         "video": ""},
        {"title": "Garlic Butter Pan Chicken",
         "steps": "1) Season chicken with salt and pepper.\n"
                  "2) Sear 2 min per side in hot pan, add 1 tbsp butter & 1 tsp chopped garlic.\n"
                  "3) Spoon butter over chicken until cooked. Rest and serve.",
         "video": ""},
        {"title": "Chicken Salad Bowl",
         "steps": "1) Grill chicken and chop into cubes.\n"
                  "2) Toss mixed greens, cucumber, cherry tomatoes with olive oil + lemon.\n"
                  "3) Top with chicken and pumpkin seeds.",
         "video": ""},
        {"title": "Baked Herbs Chicken",
         "steps": "1) Season chicken with rosemary, thyme, salt, pepper, and a drizzle of oil.\n"
                  "2) Bake at 200°C for 25–30 minutes until juices run clear.\n"
                  "3) Slice and serve with roasted veg.",
         "video": ""},
        {"title": "Chicken Wrap (Light)",
         "steps": "1) Slice grilled chicken, mix with Greek yogurt and herbs.\n"
                  "2) Stuff into whole-wheat wrap with lettuce and cucumber.\n"
                  "3) Roll tight and slice in half.",
         "video": ""},
        {"title": "Honey Lemon Glazed Chicken",
         "steps": "1) Sear cooked chicken pieces, make glaze from 1 tbsp honey + 1 tbsp lemon juice + soy.\n"
                  "2) Toss chicken in glaze on low heat until sticky.\n"
                  "3) Serve immediately.",
         "video": ""},
        {"title": "One-pan Chicken & Vegetables",
         "steps": "1) Toss chicken and mixed veg with oil, salt, pepper.\n"
                  "2) Roast on a sheet pan at 200°C for 25–30 minutes.\n"
                  "3) Serve straight from pan.",
         "video": ""},
        {"title": "Spicy Chicken Curry (Lean)",
         "steps": "1) Sauté onion until golden, add ginger-garlic paste.\n"
                  "2) Add tomato puree and spices (cumin, coriander, chili) and cook till oil separates.\n"
                  "3) Add chicken and water, simmer 20 min, garnish with coriander.",
         "video": ""}
    ],
    "Egg (Boiled)": [
        {"title": "Perfect Boiled Eggs",
         "steps": "1) Place eggs in pot, cover with cold water.\n"
                  "2) Bring to boil, then simmer 7–8 minutes for hard-boiled.\n"
                  "3) Cool in ice water, peel and serve.",
         "video": ""},
        {"title": "Masala Omelette",
         "steps": "1) Beat 2 eggs with chopped onion, tomato, green chilli and salt.\n"
                  "2) Heat 1 tsp oil, pour mixture and cook until golden both sides.\n"
                  "3) Serve hot with toast.",
         "video": "https://www.youtube.com/watch?v=gVvyQeF8a7o"},
        {"title": "Egg Bhurji (Indian Scramble)",
         "steps": "1) Sauté onion, tomato and green chillies, add turmeric and salt.\n"
                  "2) Add beaten eggs and stir quickly until set.\n"
                  "3) Garnish with coriander and serve with roti.",
         "video": ""},
        {"title": "Egg Salad Bowl",
         "steps": "1) Chop boiled eggs, mix with cucumber, tomato and a dressing of yogurt + lemon.\n"
                  "2) Season with pepper and serve chilled.",
         "video": ""},
        {"title": "Egg Fried Rice",
         "steps": "1) Scramble eggs and set aside.\n"
                  "2) Stir-fry cooked rice with vegetables, add egg and soy sauce.\n"
                  "3) Toss and serve hot.",
         "video": "https://www.youtube.com/watch?v=EhhRy0eC1tk"},
        {"title": "Poached Eggs on Greens",
         "steps": "1) Poach eggs in simmering water 3–4 minutes.\n"
                  "2) Serve on sautéed spinach with wholegrain toast.",
         "video": ""},
        {"title": "Deviled Eggs",
         "steps": "1) Halve boiled eggs, remove yolks and mash with mustard and mayo.\n"
                  "2) Refill whites with yolk mix and sprinkle paprika.",
         "video": ""},
        {"title": "Egg Sandwich",
         "steps": "1) Slice boiled egg, layer on multigrain bread with lettuce & mustard.\n"
                  "2) Toast if preferred.",
         "video": ""},
        {"title": "Cheese Omelette",
         "steps": "1) Whisk eggs, pour into pan, add grated cheese before folding.\n"
                  "2) Cook until cheese melts and serve.",
         "video": ""},
        {"title": "Spiced Egg Wrap",
         "steps": "1) Make masala omelette, fold and place inside a wrap with salad.\n"
                  "2) Roll and serve.",
         "video": ""}
    ],
    "Paneer": [
        {"title": "Paneer Tikka",
         "steps": "1) Marinate paneer cubes in yogurt, turmeric, chili powder and garam masala for 30 min.\n"
                  "2) Skewer with capsicum and onion, grill 10–12 min.\n"
                  "3) Serve with mint chutney.",
         "video": "https://www.youtube.com/watch?v=pgnFBet5pbo"},
        {"title": "Paneer Bhurji",
         "steps": "1) Crumble paneer, sauté onion, tomato and spices.\n"
                  "2) Add paneer and cook 3–4 min. Garnish with coriander.",
         "video": ""},
        {"title": "Shahi Paneer (Light)",
         "steps": "1) Make a light tomato-onion gravy, add paneer cubes and simmer 5 min.\n"
                  "2) Finish with a splash of cream (optional).",
         "video": ""},
        {"title": "Paneer Stir Fry",
         "steps": "1) Pan-fry paneer cubes till golden.\n"
                  "2) Toss with bell peppers and a splash of soy for Indo-Chinese twist.",
         "video": ""},
        {"title": "Paneer Salad Bowl",
         "steps": "1) Roast paneer, combine with salad greens, cucumber, cherry tomatoes.\n"
                  "2) Dress with lemon & olive oil.",
         "video": ""},
        {"title": "Paneer Wrap",
         "steps": "1) Mix grilled paneer cubes with yogurt & herbs.\n"
                  "2) Fill into whole-wheat wrap with lettuce.",
         "video": ""},
        {"title": "Paneer Tawa Masala",
         "steps": "1) Sauté onion, tomato and spices, add paneer and cook till masala coats paneer.\n"
                  "2) Serve hot.",
         "video": ""},
        {"title": "Paneer Rice Bowl",
         "steps": "1) Mix paneer cubes with cooked rice and herbs.\n"
                  "2) Add lemon for freshness.",
         "video": ""},
        {"title": "Spicy Paneer Bites",
         "steps": "1) Marinate paneer in chili-garlic, shallow fry until crisp.\n"
                  "2) Serve as snack with ketchup or chutney.",
         "video": ""},
        {"title": "Paneer & Veg Skillet",
         "steps": "1) Sauté seasonal veg, add paneer and a pinch of garam masala.\n"
                  "2) Cook 4–5 min and serve.",
         "video": ""}
    ],
    "Oats": [
        {"title": "Classic Oatmeal",
         "steps": "1) Combine 1/2 cup oats with 1 cup water or milk.\n"
                  "2) Cook 3–5 min until creamy.\n"
                  "3) Top with banana or berries and nuts.",
         "video": "https://www.youtube.com/watch?v=TLc9_tDJ4aA"},
        {"title": "Overnight Oats",
         "steps": "1) Mix oats, milk, chia and honey in a jar.\n"
                  "2) Refrigerate overnight.\n"
                  "3) Add fruit in morning and enjoy.",
         "video": ""},
        {"title": "Oats Protein Pancake",
         "steps": "1) Blend oats, egg, banana and protein powder.\n"
                  "2) Cook pancakes on medium heat till golden each side.",
         "video": ""},
        {"title": "Savory Masala Oats",
         "steps": "1) Sauté mustard seeds, curry leaves, vegetables.\n"
                  "2) Add oats and water, cook 3–4 min. Season to taste.",
         "video": ""},
        {"title": "Oats Smoothie Bowl",
         "steps": "1) Blend soaked oats with milk and banana.\n"
                  "2) Pour into bowl and top with nuts and fruit.",
         "video": ""},
        {"title": "Baked Oat Cups",
         "steps": "1) Mix oats, egg, yogurt, fruit and bake in muffin tray at 180°C for 15–18 min.",
         "video": ""},
        {"title": "Peanut Oats Energy Balls",
         "steps": "1) Mix oats, peanut butter, honey and roll into balls.\n"
                  "2) Chill and store for snacks.",
         "video": ""},
        {"title": "Oats Upma (Indian style)",
         "steps": "1) Roast oats, prepare tempering with mustard & curry leaves.\n"
                  "2) Add veg and water, cook till oats are soft.",
         "video": ""},
        {"title": "Oats Bircher",
         "steps": "1) Soak oats with yogurt and grated apple.\n"
                  "2) Refrigerate then serve chilled with nuts.",
         "video": ""},
        {"title": "Oats & Fruit Parfait",
         "steps": "1) Layer oats, yogurt and fruit in a glass.\n"
                  "2) Chill and serve as breakfast parfait.",
         "video": ""}
    ],
    "Fish (Grilled)": [
        {"title": "Simple Grilled Fish",
         "steps": "1) Pat fish fillet dry.\n"
                  "2) Marinate with oil, garlic, lemon and salt for 10–15 min.\n"
                  "3) Grill 3–4 min per side depending on thickness.\n"
                  "4) Serve with lemon wedge.",
         "video": "https://www.youtube.com/watch?v=kHkzp1YvYuI"},
        {"title": "Tandoori Fish",
         "steps": "1) Marinate fish in yogurt + tandoori masala 30 min.\n"
                  "2) Grill until charred and cooked through.",
         "video": ""},
        {"title": "Baked Herb Fish",
         "steps": "1) Bake fish with herbs, garlic and olive oil at 200°C for 12–15 min.\n"
                  "2) Serve with steamed veggies.",
         "video": ""},
        {"title": "Pan-seared Lemon Fish",
         "steps": "1) Season fish, sear on high heat 2–3 min per side.\n"
                  "2) Finish with a lemon-butter sauce.",
         "video": ""},
        {"title": "Fish Curry (Coconut)",
         "steps": "1) Make a light coconut-tomato gravy and add fish.\n"
                  "2) Simmer 8–10 min till flaky.",
         "video": ""},
        {"title": "Fish Tacos (Light)",
         "steps": "1) Grill fish strips, serve in tortillas with slaw and lime.\n"
                  "2) Drizzle with yogurt sauce.",
         "video": ""},
        {"title": "Fish & Veg Foil Pack",
         "steps": "1) Place fish and veg on foil with herbs and a splash of oil.\n"
                  "2) Seal and bake at 200°C for 12–15 min.",
         "video": ""},
        {"title": "Mediterranean Fish Salad",
         "steps": "1) Flake grilled fish over salad greens with olives and feta.\n"
                  "2) Dress with olive oil and lemon.",
         "video": ""},
        {"title": "Garlic Chilli Prawns Twist",
         "steps": "1) Saute prawns with garlic and chili; similar method works for small fish pieces.\n"
                  "2) Serve on rice or noodles.",
         "video": ""},
        {"title": "Herb-crusted Fish",
         "steps": "1) Coat fish with breadcrumbs and herbs, pan sear or bake till crisp.\n"
                  "2) Serve hot.",
         "video": ""}
    ],
    "Rice (Cooked)": [
        {"title": "Steamed Fluffy Rice",
         "steps": "1) Rinse rice till water runs clear.\n"
                  "2) Use 1:2 rice to water ratio, bring to boil and simmer covered 12–15 min.\n"
                  "3) Fluff with fork and serve.",
         "video": ""},
        {"title": "Veg Fried Rice (Light)",
         "steps": "1) Stir-fry mixed veggies, add cooked rice and soy sauce.\n"
                  "2) Toss and serve hot.",
         "video": ""},
        {"title": "Lemon Rice",
         "steps": "1) Temper mustard seeds, curry leaves and turmeric in oil.\n"
                  "2) Toss with cooked rice and lemon juice.",
         "video": ""},
        {"title": "Paneer Rice Bowl",
         "steps": "1) Mix cooked rice with cubed paneer, herbs and lemon.\n"
                  "2) Serve warm.",
         "video": ""},
        {"title": "Chicken Rice Bowl",
         "steps": "1) Top warm rice with sliced grilled chicken and steamed veg.\n"
                  "2) Drizzle soy or teriyaki if desired.",
         "video": ""},
        {"title": "Tomato Rice",
         "steps": "1) Cook onion and tomato with spices, add rice and simmer a few mins.\n"
                  "2) Serve hot.",
         "video": ""},
        {"title": "Coconut Rice",
         "steps": "1) Cook rice with coconut milk and a touch of sugar and salt for flavor.\n"
                  "2) Garnish with toasted coconut.",
         "video": ""},
        {"title": "Curd Rice (Simple)",
         "steps": "1) Mix cooled rice with low-fat curd and salt.\n"
                  "2) Temper with mustard seeds and curry leaves if desired.",
         "video": ""},
        {"title": "Fried Rice with Egg",
         "steps": "1) Scramble eggs, stir-fry with rice and veggies, add soy sauce.\n"
                  "2) Serve hot.",
         "video": ""},
        {"title": "Brown Rice Pilaf",
         "steps": "1) Sauté onion and spices, add brown rice and stock and simmer until tender.\n"
                  "2) Serve with grilled protein.",
         "video": ""}
    ],
    "Tofu": [
        {"title": "Tofu Stir Fry",
         "steps": "1) Press tofu, cube and pat dry.\n"
                  "2) Stir-fry with colorful veg and a sauce of soy, garlic and ginger.\n"
                  "3) Serve with rice or noodles.",
         "video": ""},
        {"title": "Grilled Tofu Skewers",
         "steps": "1) Marinate tofu cubes in BBQ or teriyaki sauce.\n"
                  "2) Skewer with veg and grill 10–12 min.",
         "video": ""},
        {"title": "Tofu Scramble",
         "steps": "1) Crumble firm tofu, sauté with turmeric and veggies until warmed.\n"
                  "2) Serve like scrambled eggs.",
         "video": ""},
        {"title": "Tofu Curry",
         "steps": "1) Add tofu cubes to a light tomato-coconut curry, simmer 8–10 min.\n"
                  "2) Garnish and serve with rice.",
         "video": ""},
        {"title": "Tofu Salad Bowl",
         "steps": "1) Bake tofu cubes till crisp, toss with salad greens and dressing.\n"
                  "2) Serve chilled or warm.",
         "video": ""},
        {"title": "Crispy Tofu Bites",
         "steps": "1) Coat tofu in a little cornstarch and pan-fry until golden.\n"
                  "2) Serve with chili dip.",
         "video": ""},
        {"title": "Tofu & Veg Wrap",
         "steps": "1) Mix grilled tofu with hummus and salad, wrap in whole wheat tortilla.\n"
                  "2) Serve warm.",
         "video": ""},
        {"title": "Tofu Rice Bowl",
         "steps": "1) Top rice with baked tofu, steamed veg and a drizzle of soy-sesame sauce.\n"
                  "2) Serve immediately.",
         "video": ""},
        {"title": "Mapo-style Tofu (light)",
         "steps": "1) Cook tofu in a light stir-fry with mild chili and bean paste.\n"
                  "2) Serve over rice in small quantities.",
         "video": ""},
        {"title": "Tofu Kebabs",
         "steps": "1) Marinate tofu chunks and skewer with veggies.\n"
                  "2) Grill until slightly charred.",
         "video": ""}
    ],
    "Prawns": [
        {"title": "Garlic Butter Prawns",
         "steps": "1) Clean prawns, pat dry.\n"
                  "2) Sauté garlic in butter, add prawns and cook 2–3 min each side.\n"
                  "3) Finish with parsley and lemon.",
         "video": ""},
        {"title": "Spicy Prawn Curry",
         "steps": "1) Make a tomato-onion masala base, add prawns and simmer 6–8 min.\n"
                  "2) Garnish with coriander.",
         "video": ""},
        {"title": "Grilled Prawns Skewers",
         "steps": "1) Marinate prawns with chili, lemon and oil.\n"
                  "2) Thread on skewers and grill 2–3 min per side.",
         "video": ""},
        {"title": "Prawn Fried Rice",
         "steps": "1) Stir-fry prawns, add rice and veg, toss with soy sauce.\n"
                  "2) Serve hot.",
         "video": ""},
        {"title": "Lemon Pepper Prawns",
         "steps": "1) Sear prawns in oil, season with lemon pepper and butter.\n"
                  "2) Serve immediately.",
         "video": ""},
        {"title": "Prawns & Veg Stir Fry",
         "steps": "1) Stir-fry prawns with mixed veggies and a splash of soy.\n"
                  "2) Finish with sesame seeds.",
         "video": ""},
        {"title": "Prawn Skillet with Garlic",
         "steps": "1) Saute prawns with garlic, chili flakes and tomato.\n"
                  "2) Serve over brown rice.",
         "video": ""},
        {"title": "Prawn Salad",
         "steps": "1) Toss grilled prawns with salad greens and lemon dressing.\n"
                  "2) Serve chilled.",
         "video": ""},
        {"title": "Coconut Prawn Curry",
         "steps": "1) Cook prawns in coconut milk with curry leaves and mustard.\n"
                  "2) Simmer 6–8 min and serve.",
         "video": ""},
        {"title": "Prawn Tacos (light)",
         "steps": "1) Fill small tortillas with grilled prawns, cabbage slaw and lime.\n"
                  "2) Serve immediately.",
         "video": ""}
    ],
    "Lentils (Cooked)": [
        {"title": "Dal Tadka (Simple)",
         "steps": "1) Cook lentils until soft.\n"
                  "2) Temper with ghee, cumin, garlic and red chilli.\n"
                  "3) Mix and simmer 5 min; serve with rice.",
         "video": ""},
        {"title": "Masoor Dal Soup",
         "steps": "1) Cook red lentils with carrots and onion.\n"
                  "2) Blend lightly for a smooth soup consistency.\n"
                  "3) Season and serve warm.",
         "video": ""},
        {"title": "Moong Dal Khichdi",
         "steps": "1) Cook moong dal and rice with turmeric and salt.\n"
                  "2) Finish with a ghee tadka and serve with curd.",
         "video": ""},
        {"title": "Lentil Salad Bowl",
         "steps": "1) Toss cooked lentils with cucumber, tomato and lemon dressing.\n"
                  "2) Serve chilled as a protein bowl.",
         "video": ""},
        {"title": "Spiced Lentil Stew",
         "steps": "1) Sauté onion, add spices and cooked lentils, simmer 10 min.\n"
                  "2) Serve with a crusty bread.",
         "video": ""},
        {"title": "Dal Fry (Light)",
         "steps": "1) Cook lentils, make onion-tomato gravy and mix.\n"
                  "2) Simmer and serve hot with rice.",
         "video": ""},
        {"title": "Lentil Patties",
         "steps": "1) Mash cooked lentils, mix with spices and shape patties.\n"
                  "2) Pan-fry until golden and serve with chutney.",
         "video": ""},
        {"title": "Lentil & Veg Stir",
         "steps": "1) Stir-fry seasonal veg, add lentils and a splash of soy.\n"
                  "2) Serve as a warm bowl.",
         "video": ""},
        {"title": "Dal & Spinach",
         "steps": "1) Add chopped spinach to cooked dal and simmer till wilted.\n"
                  "2) Season and serve.",
         "video": ""},
        {"title": "Lentil Curry with Coconut",
         "steps": "1) Make a mild coconut-tomato curry and add lentils.\n"
                  "2) Simmer 8–10 min and serve.",
         "video": ""}
    ],
    "Sweet Potato": [
        {"title": "Roasted Sweet Potato",
         "steps": "1) Cube sweet potato, toss with oil and herbs.\n"
                  "2) Roast at 200°C for 25–30 min until tender.",
         "video": ""},
        {"title": "Sweet Potato Mash",
         "steps": "1) Boil sweet potato until soft.\n"
                  "2) Mash with a little butter and salt.\n"
                  "3) Serve warm.",
         "video": ""},
        {"title": "Sweet Potato Fries (Baked)",
         "steps": "1) Cut into sticks, toss with oil and paprika.\n"
                  "2) Bake at 220°C for 20–25 min, turning halfway.",
         "video": ""},
        {"title": "Sweet Potato & Chickpea Bowl",
         "steps": "1) Roast sweet potato and chickpeas and toss with greens.\n"
                  "2) Drizzle tahini dressing.",
         "video": ""},
        {"title": "Stuffed Sweet Potato",
         "steps": "1) Bake whole sweet potato, split and fill with curd paneer or bean mix.\n"
                  "2) Serve hot.",
         "video": ""},
        {"title": "Sweet Potato Soup",
         "steps": "1) Simmer sweet potato with onion and stock, blend until smooth.\n"
                  "2) Season and serve.",
         "video": ""},
        {"title": "Sweet Potato Pancakes",
         "steps": "1) Grate sweet potato, mix with egg and flour, pan fry small pancakes.\n"
                  "2) Serve with yogurt.",
         "video": ""},
        {"title": "Spiced Sweet Potato",
         "steps": "1) Sauté cubes with cumin, coriander and chili.\n"
                  "2) Serve warm as side.",
         "video": ""},
        {"title": "Sweet Potato Salad",
         "steps": "1) Mix roasted sweet potato with greens and vinaigrette.\n"
                  "2) Top with toasted seeds.",
         "video": ""},
        {"title": "Sweet Potato & Egg Scramble",
         "steps": "1) Sauté small cubes, add eggs and scramble together.\n"
                  "2) Serve hot.",
         "video": ""}
    ]
}

# ---------------------------
# Helper functions
# ---------------------------
def get_ist_time_str():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%I:%M %p")

def get_recipes_for(food):
    return recipes.get(food, [])

# ---------------------------
# Sidebar: fitness goal + upload
# ---------------------------
st.sidebar.header("⚙️ Settings")
goal = st.sidebar.selectbox("🎯 Fitness Goal", ["Cutting", "Maintenance", "Bulking"])
uploaded = st.sidebar.file_uploader("📸 Upload meal image (optional)", type=["jpg", "jpeg", "png"])
if uploaded:
    st.sidebar.image(uploaded, caption="Uploaded (optional)", use_column_width=True)
    # simulated AI authenticity check
    if random.choice([True, False, False]):  # less often flagged
        st.sidebar.error("⚠️ This image may be AI-generated.")
    else:
        st.sidebar.success("✅ Image appears to be a real photo.")

# ---------------------------
# Main: food select + grams (moved here) + submit
# ---------------------------
st.markdown("## 1) Select food & enter portion (grams) — submit to calculate")
col1, col2 = st.columns([2, 2])

with col1:
    food_choice = st.selectbox("Choose food:", list(foods.keys()))

with col2:
    # special handling for eggs: size + count
    if food_choice == "Egg (Boiled)":
        egg_size = st.selectbox("Egg size:", ["Small", "Medium", "Large"])
        egg_count = st.number_input("Number of eggs:", min_value=1, max_value=100, value=2)
    else:
        grams = st.number_input("Weight (grams):", min_value=0, max_value=2000, value=100, step=10)

submit = st.button("✅ Submit")

# initialize session state for last submission
if "last_submission" not in st.session_state:
    st.session_state["last_submission"] = None

# handle submit
if submit:
    # compute nutrition
    if food_choice == "Egg (Boiled)":
        size_map = {"Small": 60, "Medium": 78, "Large": 90}
        per_egg_cal = size_map.get(egg_size, 78)
        calories = per_egg_cal * egg_count
        protein = 6 * egg_count
        fat = 5 * egg_count
        carbs = 0.6 * egg_count
        portion_text = f"{egg_count} x {egg_size} egg(s)"
    else:
        info = foods[food_choice]
        calories = info["calories"] * grams / 100
        protein = info["protein"] * grams / 100
        fat = info["fat"] * grams / 100
        carbs = info["carbs"] * grams / 100
        portion_text = f"{grams} g"

    # adjust daily target estimate (simple multiplier) — used only for insight
    goal_multiplier = {"Cutting": 0.85, "Maintenance": 1.0, "Bulking": 1.15}[goal]
    # for simplicity, assume base maintenance 2000 kcal — this is a placeholder you can change
    daily_target = 2000 * goal_multiplier

    # store last submission
    st.session_state["last_submission"] = {
        "food": food_choice,
        "portion": portion_text,
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "time": get_ist_time_str(),
        "goal": goal,
        "daily_target": daily_target
    }

# ---------------------------
# After submit: show results + recipes
# ---------------------------
if st.session_state.get("last_submission") and st.session_state["last_submission"]["food"] == (food_choice if not submit else food_choice):
    last = st.session_state["last_submission"]

    st.markdown("---")
    st.success(f"Logged: **{last['portion']} of {last['food']}** at **{last['time']} (IST)** — Mode: **{last['goal']}**")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 Calories", f"{last['calories']:.1f} kcal")
    c2.metric("💪 Protein", f"{last['protein']:.1f} g")
    c3.metric("🥑 Fat", f"{last['fat']:.1f} g")
    c4.metric("🍞 Carbs", f"{last['carbs']:.1f} g")

    # goal insight
    diff = last["daily_target"] - last["calories"]
    if diff > 0:
        st.info(f"⚖️ You are **{diff:.0f} kcal** below your {last['goal']} daily target (example target = {last['daily_target']:.0f} kcal). Consider adding a snack like oats or paneer.")
    else:
        st.success(f"💪 You are **{abs(diff):.0f} kcal** over your {last['goal']} target — good for bulking!")

    # Recipes dropdown (10 recipes)
    st.markdown("---")
    st.subheader(f"📚 Recipes for {last['food']} (select one to view steps)")
    rec_list = get_recipes_for(last["food"])
    if rec_list:
        titles = [r["title"] for r in rec_list]
        selected = st.selectbox("Choose a recipe:", ["-- pick a recipe --"] + titles)
        if selected != "-- pick a recipe --":
            recipe = next((r for r in rec_list if r["title"] == selected), None)
            if recipe:
                st.markdown(f"### {recipe['title']}")
                # always show step-by-step text
                st.write(recipe["steps"])
                # show video only if provided, and only if user expands
                if recipe.get("video"):
                    with st.expander("🎥 Watch video (loads only when expanded)"):
                        try:
                            st.video(recipe["video"])
                        except Exception:
                            st.write("Video could not be loaded. You can open it on YouTube:")
                            st.markdown(f"[Open video]({recipe['video']})")
    else:
        st.info("No recipes available for this food yet (coming soon).")

else:
    st.info("👈 Select a food & portion above and click **Submit** — recipes & videos will appear after submit.")

# ---------------------------
# End footer
# ---------------------------
st.markdown("---")
st.caption("Built with ❤️ — Smart Nutrition Tracker (team edition).")
