# app.py
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="💪 Smart Nutrition Tracker v7.0 — Ultimate Gym Edition", layout="wide")
st.title("💪 Smart Nutrition Tracker — Ultimate Gym Edition")
st.markdown("Track meals, get accurate macros, view 10 recipes per food (text + optional videos). Submit first → then view recipes.")

# ---------------------------
# Helper functions
# ---------------------------
def now_ist_str():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%I:%M %p")

def apply_goal_multiplier(calories, goal):
    if goal == "Cutting":
        return calories * 0.8
    if goal == "Bulking":
        return calories * 1.15
    return calories

# ---------------------------
# Foods data
# Each food: types -> nutrition per 100g (cal, prot, fat, carbs)
# and recipes: list of dict {title, steps, video}
# ---------------------------
foods_data = {
    # Non-veg / high protein
    "Chicken": {
        "types": {
            "Grilled": {"calories":165, "protein":31, "fat":3.6, "carbs":0},
            "Baked": {"calories":170, "protein":30, "fat":4, "carbs":0},
            "Stir-Fry": {"calories":190, "protein":29, "fat":6, "carbs":2}
        },
        "recipes": [
            {"title":"Grilled Lemon Garlic Chicken",
             "steps":"1) Trim 200g chicken breast and pat dry.\n2) Mix 1 tbsp olive oil, 1 tbsp lemon juice, 1 tsp garlic paste, 1/2 tsp salt, pepper.\n3) Marinate 20–30 min.\n4) Grill 6–8 min per side until 74°C internal temp.\n5) Rest 3 min, slice and serve with greens.",
             "video":"https://www.youtube.com/watch?v=4UHVxRjYX8E"},
            {"title":"Classic Chicken Curry (Lean)",
             "steps":"1) Sear 200g chicken pieces; set aside.\n2) In same pan, sauté 1 onion until golden, add ginger-garlic paste.\n3) Add 1 cup pureed tomatoes and spices (turmeric, cumin, coriander, chili) and cook till oil separates.\n4) Add chicken + 100 ml water, simmer 20 min until tender.\n5) Garnish coriander.",
             "video":"https://www.youtube.com/watch?v=Wy4U5J0lYtY"},
            {"title":"Chicken Stir Fry with Veggies",
             "steps":"1) Slice chicken thinly.\n2) Heat 1 tbsp oil, stir-fry bell peppers and broccoli 2–3 min.\n3) Add chicken and 1 tbsp soy, cook 5–7 min.\n4) Finish with sesame oil and spring onion.\n5) Serve over brown rice.",
             "video":"https://www.youtube.com/watch?v=Qv6F7D8l8wk"},
            {"title":"Tandoori-style Oven Chicken",
             "steps":"1) Mix 3 tbsp yogurt, 1 tsp turmeric, 1 tsp red chili, 1 tsp garam masala, 1 tsp ginger-garlic paste.\n2) Coat chicken, marinate 1–2 hours.\n3) Bake 200°C 20–25 min; broil 2–3 min for char.\n4) Serve with lemon and salad.",
             "video":"https://www.youtube.com/watch?v=4oPOkzqYx1c"},
            {"title":"Honey Lemon Chicken (Light)",
             "steps":"1) Sear cooked chicken pieces.\n2) Mix 1 tbsp honey, 1 tbsp lemon juice, 1 tsp soy; toss chicken in glaze briefly.\n3) Serve immediately.",
             "video":""},
            {"title":"Chicken Salad Bowl",
             "steps":"1) Grill 150–200g chicken and chop.\n2) Toss rocket, spinach, cucumber, tomato, 1 tbsp olive oil + lemon.\n3) Top with chicken and seeds.",
             "video":""},
            {"title":"Chicken Wrap (Whole Wheat)",
             "steps":"1) Slice grilled chicken.\n2) Mix with yogurt, herbs, lettuce, cucumber.\n3) Wrap in whole-wheat tortilla.",
             "video":""},
            {"title":"One-pan Roast Chicken & Veg",
             "steps":"1) Toss chicken chunks + carrots, potatoes, broccoli with oil and herbs.\n2) Roast 200°C for 25–30 min until cooked.",
             "video":""},
            {"title":"Chicken Soup (Clear)",
             "steps":"1) Boil chicken bones with onion, carrot, celery 30–45 min.\n2) Strain, add shredded chicken and simmer 5 min.\n3) Season and serve.",
             "video":""},
            {"title":"Spicy Chicken Skewers",
             "steps":"1) Marinate cubes in chili, garlic, lemon.\n2) Skewer with onion/pepper; grill till charred.\n3) Serve with mint chutney.",
             "video":""}
        ]
    },

    "Egg": {
        "types": {
            "Boiled": {"calories":78, "protein":6, "fat":5, "carbs":0.6},
            "Scrambled": {"calories":90, "protein":6.3, "fat":7, "carbs":1},
            "Omelette": {"calories":100, "protein":7, "fat":8, "carbs":1.2}
        },
        "recipes":[
            {"title":"Perfect Boiled Eggs",
             "steps":"1) Place eggs in cold water, bring to boil.\n2) Boil 7–9 min for medium-hard yolk.\n3) Cool in ice water, peel and serve.",
             "video":"https://www.youtube.com/watch?v=8U3Y2tYQK8I"},
            {"title":"Masala Omelette",
             "steps":"1) Beat 2 eggs, add onion, tomato, green chili, salt.\n2) Cook on medium heat 2–3 min each side until set.\n3) Serve hot with toast.",
             "video":"https://www.youtube.com/watch?v=DNfLvJ4zAY8"},
            {"title":"Egg Bhurji (Indian Scramble)",
             "steps":"1) Sauté onion, tomato, green chili; add beaten eggs and scramble quickly.\n2) Finish with coriander.",
             "video":""},
            {"title":"Scrambled Eggs (Creamy)",
             "steps":"1) Whisk eggs + pinch salt + splash milk.\n2) Cook on low heat stirring until creamy.\n3) Serve with avocado.",
             "video":"https://www.youtube.com/watch?v=1S5aZlHgb7U"},
            {"title":"Poached Egg on Greens",
             "steps":"1) Poach egg 3–4 min.\n2) Lay over sautéed spinach and serve.",
             "video":""},
            {"title":"Deviled Eggs",
             "steps":"1) Halve boiled eggs, mash yolks with mustard & mayo, refill whites.\n2) Sprinkle paprika.",
             "video":""},
            {"title":"Egg Sandwich",
             "steps":"1) Slice boiled eggs, layer with lettuce & mustard on multigrain bread.\n2) Toast if desired.",
             "video":""},
            {"title":"Egg Fried Rice",
             "steps":"1) Scramble eggs and set aside.\n2) Stir-fry cooked rice + veg, add egg & soy sauce.",
             "video":"https://www.youtube.com/watch?v=EhhRy0eC1tk"},
            {"title":"Spiced Egg Wrap",
             "steps":"1) Make omelette with masala, fold into a wrap with salad.",
             "video":""},
            {"title":"Herbed Egg Toast",
             "steps":"1) Smash boiled egg with herbs, spread on toast and enjoy.",
             "video":""}
        ]
    },

    "Fish": {
        "types": {
            "Grilled": {"calories":206, "protein":22, "fat":12, "carbs":0},
            "Baked": {"calories":210, "protein":21, "fat":11.5, "carbs":0},
            "Curry": {"calories":220, "protein":20, "fat":13, "carbs":2}
        },
        "recipes":[
            {"title":"Simple Grilled Fish",
             "steps":"1) Pat fillet dry.\n2) Marinate with lemon, garlic, salt 10 min.\n3) Grill 3–4 min per side depending on thickness.\n4) Serve with lemon.",
             "video":"https://www.youtube.com/watch?v=kHkzp1YvYuI"},
            {"title":"Baked Herb Fish",
             "steps":"1) Brush fillet with oil and herbs, bake 12–15 min at 200°C.",
             "video":""},
            {"title":"Fish Curry (Coconut)",
             "steps":"1) Make light coconut-tomato gravy; add fish and simmer 8–10 min.",
             "video":""},
            {"title":"Pan-seared Lemon Fish",
             "steps":"1) Sear for 2–3 min each side, finish with lemon-butter sauce.",
             "video":""},
            {"title":"Fish Tacos (Light)",
             "steps":"1) Grill fish, flake and serve in tortillas with slaw.",
             "video":""},
            {"title":"Foil-baked Fish & Veg",
             "steps":"1) Place fish & veg on foil with herbs, seal and bake 12–15 min.",
             "video":""},
            {"title":"Mediterranean Fish Salad",
             "steps":"1) Flake grilled fish over salad with olives & feta.",
             "video":""},
            {"title":"Garlic Chili Fish",
             "steps":"1) Sauté garlic & chili, add fish pieces and cook briefly.",
             "video":""},
            {"title":"Fish Soup (Light)",
             "steps":"1) Boil fish heads/bones for broth; add veg and flaky fish pieces.",
             "video":""},
            {"title":"Herb-crusted Fish",
             "steps":"1) Coat fillet with breadcrumbs/herbs and bake until crisp.",
             "video":""}
        ]
    },

    "Prawns": {
        "types": {
            "Garlic Butter": {"calories":99, "protein":24, "fat":0.3, "carbs":0.2},
            "Spicy": {"calories":110, "protein":23, "fat":1.5, "carbs":1},
            "Grilled": {"calories":95, "protein":24, "fat":0.5, "carbs":0.2}
        },
        "recipes":[
            {"title":"Garlic Butter Prawns",
             "steps":"1) Sauté garlic in butter, add prawns and cook 2–3 min per side.\n2) Finish with lemon and parsley.",
             "video":""},
            {"title":"Spicy Prawn Curry",
             "steps":"1) Make onion-tomato masala, add prawns and simmer 6–8 min.",
             "video":""},
            {"title":"Grilled Prawns Skewers",
             "steps":"1) Marinate prawns, skewer with veg and grill 2–3 min per side.",
             "video":""},
            {"title":"Prawn Fried Rice",
             "steps":"1) Stir-fry prawns, add rice & veg, soy sauce.", "video":""},
            {"title":"Lemon Pepper Prawns", "steps":"Sear prawns and season with lemon pepper.", "video":""},
            {"title":"Prawn Salad", "steps":"Toss grilled prawns with greens and lemon dressing.", "video":""},
            {"title":"Prawn Pasta", "steps":"Cook prawns, toss with pasta and light sauce.", "video":""},
            {"title":"Coconut Prawn Curry", "steps":"Cook prawns in coconut milk and spices.", "video":""},
            {"title":"Prawn Tacos", "steps":"Fill tortillas with prawns and cabbage slaw.", "video":""},
            {"title":"Herbed Prawn Skillet", "steps":"Sear prawns with herbs and garlic.", "video":""}
        ]
    },

    # Veg / plant protein
    "Paneer": {
        "types": {
            "Grilled": {"calories":265, "protein":18, "fat":21, "carbs":2.4},
            "Curry": {"calories":300, "protein":17, "fat":22, "carbs":6},
            "Stir-Fry": {"calories":270, "protein":18, "fat":20, "carbs":3}
        },
        "recipes":[
            {"title":"Paneer Tikka",
             "steps":"1) Marinate paneer cubes in yogurt, turmeric, chili, garam masala 30 min.\n2) Skewer & grill 10–12 min.\n3) Serve with chutney.",
             "video":"https://www.youtube.com/watch?v=6xUwN0GJXIU"},
            {"title":"Paneer Bhurji",
             "steps":"1) Crumble paneer, sauté onion & tomato and mix paneer until warm.", "video":""},
            {"title":"Shahi Paneer (Light)", "steps":"Make a light tomato-onion gravy and add paneer.", "video":""},
            {"title":"Paneer Salad", "steps":"Grill paneer and toss with salad greens.", "video":""},
            {"title":"Paneer Wrap", "steps":"Mix paneer with herbs & yogurt, wrap with veggies.", "video":""},
            {"title":"Paneer Stir Fry", "steps":"Pan-fry paneer with bell peppers and soy.", "video":""},
            {"title":"Grilled Paneer Sandwich", "steps":"Grill paneer and assemble with bread & greens.", "video":""},
            {"title":"Paneer Rice Bowl", "steps":"Combine paneer with rice, veggies and lemon.", "video":""},
            {"title":"Chilli Paneer (Light)", "steps":"Quick Indo-Chinese toss with peppers and soy.", "video":""},
            {"title":"Paneer Skewers", "steps":"Thread paneer & veg and grill.", "video":""}
        ]
    },

    "Tofu": {
        "types": {
            "Stir-Fry": {"calories":76, "protein":8, "fat":4.8, "carbs":1.9},
            "Grilled": {"calories":90, "protein":9, "fat":5, "carbs":2},
            "Baked": {"calories":85, "protein":8, "fat":4.5, "carbs":2}
        },
        "recipes":[
            {"title":"Tofu Stir Fry", "steps":"1) Press tofu, cube and pan-fry until golden.\n2) Stir-fry veg and toss tofu with soy & ginger.", "video":""},
            {"title":"Baked Tofu", "steps":"Marinate and bake tofu cubes 20 min.", "video":""},
            {"title":"Tofu Curry", "steps":"Add tofu cubes to light tomato or coconut curry.", "video":""},
            {"title":"Tofu Salad", "steps":"Bake tofu and toss with salad & dressing.", "video":""},
            {"title":"Tofu Wrap", "steps":"Fill tortilla with tofu, hummus & veg.", "video":""},
            {"title":"Mapo-style Tofu (light)", "steps":"Stir-in spicy-savoury sauce with tofu and serve on rice.", "video":""},
            {"title":"Tofu Scramble", "steps":"Crumble tofu and cook with turmeric & veggies.", "video":""},
            {"title":"Crispy Tofu Bites", "steps":"Coat in cornflour, pan-fry until crisp.", "video":""},
            {"title":"Tofu Rice Bowl", "steps":"Top rice with tofu, greens and sesame sauce.", "video":""},
            {"title":"Herbed Tofu Skewers", "steps":"Marinate and grill tofu with peppers.", "video":""}
        ]
    },

    "Lentils": {
        "types": {
            "Boiled": {"calories":116, "protein":9, "fat":0.4, "carbs":20},
            "Dal Tadka": {"calories":130, "protein":8, "fat":1, "carbs":22}
        },
        "recipes":[
            {"title":"Dal Tadka", "steps":"Cook lentils, prepare tadka of cumin, garlic and mix.", "video":""},
            {"title":"Masoor Dal Soup", "steps":"Cook red lentils with veggies and blend lightly.", "video":""},
            {"title":"Khichdi (Light)", "steps":"Cook dal and rice with turmeric and salt.", "video":""},
            {"title":"Lentil Salad", "steps":"Toss cooked lentils with cucumber, tomato & lemon dressing.", "video":""},
            {"title":"Lentil Patties", "steps":"Mash lentils, form patties and pan-fry until golden.", "video":""},
            {"title":"Spiced Lentil Stew", "steps":"Simmer lentils with spices and tomatoes.", "video":""},
            {"title":"Lentil Rice", "steps":"Mix lentils with rice and herbs.", "video":""},
            {"title":"Lentil Wrap", "steps":"Fill wraps with spiced lentils and veggies.", "video":""},
            {"title":"Lentil & Spinach", "steps":"Add spinach to cooked lentils and heat through.", "video":""},
            {"title":"Coconut Lentil Curry", "steps":"Cook with light coconut milk and spices.", "video":""}
        ]
    },

    "Oats": {
        "types": {
            "Porridge": {"calories":389, "protein":17, "fat":7, "carbs":66},
            "Overnight": {"calories":350, "protein":14, "fat":6, "carbs":60}
        },
        "recipes":[
            {"title":"Classic Oatmeal", "steps":"Boil oats in milk/water 3–5 min; top with fruit & nuts.", "video":"https://www.youtube.com/watch?v=QnWcHR2v3io"},
            {"title":"Overnight Oats", "steps":"Mix oats, milk and chia; refrigerate overnight; top with berries.", "video":""},
            {"title":"Oats Pancakes", "steps":"Blend oats, banana, egg; cook pancakes until golden.", "video":""},
            {"title":"Savory Masala Oats", "steps":"Temper mustard seeds, add veggies and oats, cook till soft.", "video":""},
            {"title":"Oats Smoothie", "steps":"Blend soaked oats with milk and whey protein.", "video":""},
            {"title":"Baked Oat Cups", "steps":"Mix oats, egg, fruit and bake in muffin tray.", "video":""},
            {"title":"Oats Energy Balls", "steps":"Mix oats, peanut butter and honey, roll into balls.", "video":""},
            {"title":"Oats Upma", "steps":"Roast oats and cook with veg tempering.", "video":""},
            {"title":"Oats Bircher", "steps":"Soak oats with yogurt and apple overnight.", "video":""},
            {"title":"Oats Protein Bar", "steps":"Mix oats, whey, nut butter and press into tray; chill.", "video":""}
        ]
    },

    "Greek Yogurt": {
        "types": {
            "Plain": {"calories":59, "protein":10, "fat":0.4, "carbs":3.6},
            "With Fruit": {"calories":90, "protein":9, "fat":1, "carbs":12}
        },
        "recipes":[
            {"title":"Yogurt Parfait", "steps":"Layer yogurt, granola and fruit in a glass.", "video":""},
            {"title":"Greek Yogurt Dip", "steps":"Mix with herbs, garlic and lemon for dip.", "video":""},
            {"title":"Protein Yogurt Bowl", "steps":"Mix yogurt with whey and top with nuts.", "video":""},
            {"title":"Frozen Yogurt Bites", "steps":"Spoon yogurt with fruit into molds and freeze.", "video":""},
            {"title":"Yogurt Smoothie", "steps":"Blend yogurt with fruit and a scoop of protein.", "video":""},
            {"title":"Savory Yogurt Salad", "steps":"Mix yogurt with cucumber and mint for raita.", "video":""},
            {"title":"Yogurt Overnight Oats", "steps":"Combine with oats and refrigerate.", "video":""},
            {"title":"Honey Yogurt", "steps":"Sweeten yogurt with honey and serve.", "video":""},
            {"title":"Cucumber Yogurt Bowl", "steps":"Mix yogurt with cucumber, salt and pepper.", "video":""},
            {"title":"Yogurt Pancake Topping", "steps":"Top pancakes with Greek yogurt and berries.", "video":""}
        ]
    },

    "Peanut Butter": {
        "types": {
            "Natural": {"calories":588, "protein":25, "fat":50, "carbs":20},
            "Crunchy": {"calories":590, "protein":24, "fat":52, "carbs":20}
        },
        "recipes":[
            {"title":"PB Banana Toast", "steps":"Spread PB on toast, top with banana and cinnamon.", "video":""},
            {"title":"PB Protein Smoothie", "steps":"Blend PB, banana, milk and whey.", "video":""},
            {"title":"PB Energy Balls", "steps":"Mix PB, oats and honey; roll into balls.", "video":""},
            {"title":"PB Oats Bowl", "steps":"Add PB to warm oats and top with nuts.", "video":""},
            {"title":"PB Pancakes", "steps":"Add PB into pancake batter and cook.", "video":""},
            {"title":"PB Overnight Oats", "steps":"Mix PB, oats and milk; refrigerate overnight.", "video":""},
            {"title":"PB Yogurt Mix", "steps":"Stir PB into yogurt for dip.", "video":""},
            {"title":"PB Cookies", "steps":"Mix PB with oats and bake small cookies.", "video":""},
            {"title":"PB Sandwich", "steps":"Spread PB with apple slices in between bread.", "video":""},
            {"title":"PB Protein Bars", "steps":"Combine PB, whey & oats; press and chill.", "video":""}
        ]
    },

    "Chickpeas": {
        "types": {
            "Boiled": {"calories":164, "protein":9, "fat":2.6, "carbs":27},
            "Roasted": {"calories":180, "protein":8, "fat":4, "carbs":25}
        },
        "recipes":[
            {"title":"Chickpea Salad", "steps":"Toss boiled chickpeas with cucumber, tomato and lemon dressing.", "video":""},
            {"title":"Hummus", "steps":"Blend chickpeas with tahini, lemon and garlic.", "video":""},
            {"title":"Chickpea Curry", "steps":"Cook chickpeas with onion-tomato masala.", "video":""},
            {"title":"Roasted Spicy Chickpeas", "steps":"Toss with spices and roast until crisp.", "video":""},
            {"title":"Chickpea Wrap", "steps":"Fill wrap with spiced chickpeas and salad.", "video":""},
            {"title":"Chickpea Soup", "steps":"Simmer chickpeas with veg and blend lightly.", "video":""},
            {"title":"Chickpea Patties", "steps":"Mash and form patties; pan-fry.", "video":""},
            {"title":"Chickpea Bowl", "steps":"Top grains with chickpeas, avocado and salsa.", "video":""},
            {"title":"Chickpea Stir Fry", "steps":"Stir-fry with peppers and soy.", "video":""},
            {"title":"Chickpea Rice", "steps":"Mix with rice and herbs.", "video":""}
        ]
    },

    "Sweet Potato": {
        "types": {
            "Baked": {"calories":86, "protein":1.6, "fat":0.1, "carbs":20},
            "Mashed": {"calories":90, "protein":1.6, "fat":0.2, "carbs":21}
        },
        "recipes":[
            {"title":"Roasted Sweet Potato", "steps":"Cube and roast with oil & herbs 25–30 min.", "video":""},
            {"title":"Sweet Potato Mash", "steps":"Boil then mash with a little butter.", "video":""},
            {"title":"Sweet Potato Fries", "steps":"Cut into fries, toss with oil; bake 20–25 min.", "video":""},
            {"title":"Stuffed Sweet Potato", "steps":"Bake whole, split and fill with curd paneer or chickpeas.", "video":""},
            {"title":"Sweet Potato Soup", "steps":"Boil and blend with onion & stock.", "video":""},
            {"title":"Sweet Potato Pancakes", "steps":"Grate and mix with egg; pan fry small pancakes.", "video":""},
            {"title":"Sweet Potato Bowl", "steps":"Combine roasted sweet potato with greens & protein.", "video":""},
            {"title":"Sweet Potato Salad", "steps":"Toss cubes with greens and vinaigrette.", "video":""},
            {"title":"Spiced Sweet Potato", "steps":"Sauté cubes with cumin and chili.", "video":""},
            {"title":"Sweet Potato & Egg Scramble", "steps":"Sauté cubes, then scramble with eggs.", "video":""}
        ]
    },

    # Supplements & high-protein snack categories
    "Whey Protein": {
        "types": {
            "Shake (Water)": {"calories":120, "protein":24, "fat":1, "carbs":3},
            "Shake (Milk)": {"calories":200, "protein":28, "fat":3, "carbs":10}
        },
        "recipes":[
            {"title":"Chocolate Whey Shake", "steps":"Blend 1 scoop chocolate whey with water/milk and ice.", "video":"https://www.youtube.com/watch?v=dvQDaWj1gkM"},
            {"title":"Banana Whey Smoothie", "steps":"Blend whey, 1 banana and milk.", "video":""},
            {"title":"Whey Oats Smoothie", "steps":"Blend oats, whey and water/milk.", "video":""},
            {"title":"Peanut Butter Whey Shake", "steps":"Blend whey, 1 tbsp peanut butter, milk and ice.", "video":""},
            {"title":"Green Protein Smoothie", "steps":"Blend whey with spinach, banana and water.", "video":""},
            {"title":"Coffee Whey Shake", "steps":"Blend whey with cold coffee and milk.", "video":""},
            {"title":"Whey Pancakes", "steps":"Mix whey, oats and egg to make batter; cook pancakes.", "video":""},
            {"title":"Frozen Whey Bites", "steps":"Mix whey with yogurt and freeze in molds.", "video":""},
            {"title":"Mass Gainer Shake", "steps":"Blend whey with oats, banana and milk.", "video":""},
            {"title":"Berry Whey Smoothie", "steps":"Blend whey with mixed berries and water.", "video":""}
        ]
    },

    "Protein Bar": {
        "types": {
            "Store-bought": {"calories":350, "protein":30, "fat":10, "carbs":40},
            "Homemade": {"calories":300, "protein":20, "fat":12, "carbs":30}
        },
        "recipes":[
            {"title":"No-Bake Oats Protein Bar", "steps":"Mix oats, PB, whey and honey; press into pan and chill.", "video":""},
            {"title":"Peanut Butter Protein Bars", "steps":"Mix PB, oats, protein and bake.", "video":""},
            {"title":"Chocolate Protein Brownie Bars", "steps":"Combine whey, cocoa, oats and bake.", "video":""},
            {"title":"Coconut Protein Bars", "steps":"Mix coconut, dates, protein and press.", "video":""},
            {"title":"Almond Protein Bars", "steps":"Mix ground almonds, dates and protein powder.", "video":""},
            {"title":"Banana Date Bars", "steps":"Blend banana & dates with oats and bake small bars.", "video":""},
            {"title":"Crunchy Protein Bars", "steps":"Combine puffed rice, nut butter & whey and press.", "video":""},
            {"title":"Seeded Protein Bars", "steps":"Mix seeds, honey and protein, press and chill.", "video":""},
            {"title":"Energy Protein Balls", "steps":"Roll mixture of oats, PB & whey into balls and chill.", "video":""},
            {"title":"Baked Protein Bars", "steps":"Combine protein, oats & egg; bake in tray and slice.", "video":""}
        ]
    },

    "Milk": {
        "types": {
            "Cow Milk (Full)": {"calories":60, "protein":3.2, "fat":3.5, "carbs":5},
            "Cow Milk (Skim)": {"calories":40, "protein":3.4, "fat":0.1, "carbs":5}
        },
        "recipes":[
            {"title":"Masala Milk (Light)", "steps":"Warm milk with a pinch of cardamom and a tiny bit of honey.", "video":""},
            {"title":"Milk & Oats Shake", "steps":"Blend milk with oats and banana.", "video":""},
            {"title":"Golden Milk (Turmeric)", "steps":"Warm milk with turmeric and honey.", "video":""},
            {"title":"Protein Milkshake", "steps":"Mix milk with whey protein and fruit.", "video":""},
            {"title":"Chocolate Milk (Healthy)", "steps":"Mix cocoa powder, milk, and a teaspoon of honey.", "video":""},
            {"title":"Milk Smoothie", "steps":"Blend milk with fruit and yogurt.", "video":""},
            {"title":"Milk Pudding (Light)", "steps":"Simmer milk with a bit of cornstarch and fruit.", "video":""},
            {"title":"Milk & Almonds", "steps":"Soak almonds overnight and blend with milk for a creamy drink.", "video":""},
            {"title":"Iced Milk Coffee (Protein)", "steps":"Mix cold milk, coffee and whey for a protein boost.", "video":""},
            {"title":"Milk Cereal Bowl", "steps":"Pour milk over whole-grain cereal and top with fruit.", "video":""}
        ]
    },

    # Fruits / nuts / extras
    "Banana": {
        "types": {"Raw": {"calories":89, "protein":1.1, "fat":0.3, "carbs":23}},
        "recipes":[
            {"title":"Banana & PB Toast", "steps":"Spread PB on toast and top with banana slices.", "video":""},
            {"title":"Banana Oats Smoothie", "steps":"Blend banana with oats and milk.", "video":""},
            {"title":"Frozen Banana Bites", "steps":"Dip banana slices in yogurt and freeze.", "video":""},
            {"title":"Banana Pancakes", "steps":"Mash banana, mix with egg and cook small pancakes.", "video":""},
            {"title":"Banana Protein Shake", "steps":"Blend banana with whey and milk.", "video":""},
            {"title":"Banana & Yogurt Bowl", "steps":"Combine sliced banana with Greek yogurt and nuts.", "video":""},
            {"title":"Baked Banana Oats", "steps":"Mix banana with oats and bake cups.", "video":""},
            {"title":"Banana Energy Balls", "steps":"Mix banana, oats and PB; roll and chill.", "video":""},
            {"title":"Banana & Almond Butter", "steps":"Top banana with almond butter and cinnamon.", "video":""},
            {"title":"Banana & Chia Pudding", "steps":"Blend banana into chia pudding for sweetness.", "video":""}
        ]
    },

    "Almonds": {
        "types": {"Raw": {"calories":579, "protein":21, "fat":50, "carbs":22}},
        "recipes":[
            {"title":"Roasted Almonds (Light)", "steps":"Toast almonds lightly with a pinch of salt.", "video":""},
            {"title":"Almond Milk (Homemade)", "steps":"Blend soaked almonds with water, strain.", "video":""},
            {"title":"Almond Oats Topper", "steps":"Chop and add almonds to oats or yoghurt.", "video":""},
            {"title":"Almond Butter Toast", "steps":"Spread almond butter on wholegrain toast.", "video":""},
            {"title":"Almond & Date Energy Balls", "steps":"Blend almonds & dates, roll into balls.", "video":""},
            {"title":"Almond Smoothie", "steps":"Blend almonds with milk and fruit.", "video":""},
            {"title":"Almond Protein Bars", "steps":"Combine almonds with protein mix and press.", "video":""},
            {"title":"Cinnamon Almond Snack", "steps":"Toss almonds with cinnamon and bake briefly.", "video":""},
            {"title":"Almond Yogurt Bowl", "steps":"Top Greek yogurt with sliced almonds.", "video":""},
            {"title":"Almond-Crust Fish", "steps":"Crush almonds and coat fish, bake crisp.", "video":""}
        ]
    },

    "Apple": {
        "types": {"Raw": {"calories":52, "protein":0.3, "fat":0.2, "carbs":14}},
        "recipes":[
            {"title":"Sliced Apple with PB", "steps":"Top apple slices with peanut butter.", "video":""},
            {"title":"Baked Apple", "steps":"Core apple, stuff with oats & cinnamon, bake.", "video":""},
            {"title":"Apple Oats Bowl", "steps":"Mix chopped apple with warm oats.", "video":""},
            {"title":"Apple Smoothie", "steps":"Blend apple with yogurt and cinnamon.", "video":""},
            {"title":"Apple & Cheese Plate", "steps":"Serve sliced apple with cottage cheese.", "video":""},
            {"title":"Apple Energy Bites", "steps":"Mix apple with oats & dates and roll.", "video":""},
            {"title":"Apple Pancakes", "steps":"Add apple pieces to pancake batter.", "video":""},
            {"title":"Caramelized Apple", "steps":"Sauté apple in little butter and honey.", "video":""},
            {"title":"Apple Salad", "steps":"Toss apple with greens, nuts and vinaigrette.", "video":""},
            {"title":"Apple Yogurt Parfait", "steps":"Layer apple, yogurt and granola.", "video":""}
        ]
    }
}

# ---------------------------
# Sidebar - select food & type first
# ---------------------------
st.sidebar.header("🍽 Meal Setup (Select first)")

available_foods = list(foods_data.keys())
food_choice = st.sidebar.selectbox("Select a food:", available_foods)

type_choice = None
grams = None
egg_size = None
egg_count = None

if food_choice:
    types = list(foods_data[food_choice]["types"].keys())
    # select type/variant
    type_choice = st.sidebar.selectbox("Select type / cooking variant:", types)

    # Show grams input only after type selected
    if type_choice:
        # special handling: if user picked Egg, allow egg count/size instead of grams
        if food_choice == "Egg":
            egg_size = st.sidebar.selectbox("Select egg size:", ["Small", "Medium", "Large"])
            egg_count = st.sidebar.number_input("Number of eggs:", min_value=1, max_value=100, value=2)
        else:
            grams = st.sidebar.number_input("Enter weight (grams):", min_value=0, max_value=2000, value=100, step=10)

        # goal and upload below grams
        goal = st.sidebar.selectbox("Select fitness goal:", ["Cutting", "Maintenance", "Bulking"])
        uploaded_image = st.sidebar.file_uploader("Upload meal image (optional):", type=["jpg", "jpeg", "png"])
        submit = st.sidebar.button("✅ Submit")
    else:
        # placeholders to keep variables defined
        goal = st.sidebar.selectbox("Select fitness goal:", ["Cutting", "Maintenance", "Bulking"])
        uploaded_image = st.sidebar.file_uploader("Upload meal image (optional):", type=["jpg", "jpeg", "png"])
        submit = False
else:
    submit = False
    goal = "Maintenance"
    uploaded_image = None

# ---------------------------
# Session state for meal history
# ---------------------------
if "meal_history" not in st.session_state:
    st.session_state["meal_history"] = []

# ---------------------------
# Submit handling: show nutrition then optional recipes
# ---------------------------
if submit and type_choice:
    # compute nutrition
    nutrition = foods_data[food_choice]["types"][type_choice]
    if food_choice == "Egg":
        # use per-egg standard sizes
        size_map = {"Small":60, "Medium":78, "Large":90}
        per_egg_cal = size_map.get(egg_size, 78)
        per_egg_pro = 6
        per_egg_fat = 5
        per_egg_carbs = 0.6
        total_cal = per_egg_cal * egg_count
        total_pro = per_egg_pro * egg_count
        total_fat = per_egg_fat * egg_count
        total_carbs = per_egg_carbs * egg_count
        portion_text = f"{egg_count} x {egg_size} egg(s)"
    else:
        total_cal = nutrition["calories"] * (grams / 100.0)
        total_pro = nutrition["protein"] * (grams / 100.0)
        total_fat = nutrition["fat"] * (grams / 100.0)
        total_carbs = nutrition["carbs"] * (grams / 100.0)
        portion_text = f"{grams} g"

    adjusted_cal = apply_goal_multiplier(total_cal, goal)

    # store history entry
    entry = {"Food": food_choice, "Type": type_choice, "Portion": portion_text, "Calories": round(adjusted_cal,1),
             "Protein": round(total_pro,1), "Fat": round(total_fat,1), "Carbs": round(total_carbs,1),
             "Time": now_ist_str(), "Goal": goal}
    st.session_state["meal_history"].append(entry)

    # show summary metrics
    st.markdown("---")
    st.success(f"✅ Submitted: {portion_text} of {food_choice} ({type_choice}) — Logged at {entry['Time']} IST")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 Calories", f"{entry['Calories']} kcal")
    c2.metric("💪 Protein", f"{entry['Protein']} g")
    c3.metric("🥑 Fat", f"{entry['Fat']} g")
    c4.metric("🍞 Carbs", f"{entry['Carbs']} g")

    # goal insight
    # baseline maintenance estimate: 2500 kcal (could be personalized later)
    base_maintenance = 2500
    target = base_maintenance * (0.8 if goal=="Cutting" else 1.15 if goal=="Bulking" else 1.0)
    diff = target - entry['Calories']
    if diff > 0:
        st.info(f"⚖️ You are {diff:.0f} kcal below your {goal} target (example daily target = {target:.0f} kcal). Consider adding a snack like oats or paneer.")
    else:
        st.success(f"💪 You are {abs(diff):.0f} kcal above your {goal} target — good for mass gain!")

    # show uploaded image and AI detection placeholder with 99% real
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Meal Image", use_column_width=True)
        # Placeholder AI detection result (user requested 99% real)
        ai_prob_real = 99.0
        st.info(f"🤖 AI authenticity check: **{ai_prob_real:.0f}% real** (mock detection)")
    else:
        st.info("📸 No image uploaded (optional).")

    # show button to view recipes & videos
    if st.button("🍳 View Recipes & Videos"):
        st.markdown(f"## 🍽 Recipes for {food_choice} — {type_choice}")
        # list of recipes for the food
        recs = foods_data[food_choice]["recipes"]
        for idx, r in enumerate(recs, start=1):
            with st.expander(f"Recipe {idx}: {r['title']}"):
                st.markdown(f"**Step-by-step:**\n{r['steps']}")
                if r.get("video"):
                    try:
                        st.markdown("🎥 **Watch video (loads when you expand)**")
                        st.video(r["video"])
                    except Exception:
                        st.markdown(f"🔗 Video link: {r['video']}")

else:
    st.info("👈 Choose food and type on the left. Grams input appears after selecting type. Click Submit to calculate and unlock recipes.")

# ---------------------------
# Meal history display
# ---------------------------
if st.session_state["meal_history"]:
    st.markdown("---")
    st.subheader("📋 Today's Meal History (Session)")
    # show last 10 entries in reverse order
    history = list(reversed(st.session_state["meal_history"]))[:50]
    st.table(history)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("Built with ❤️ — Smart Nutrition Tracker v7.0 (Ultimate Gym Edition).")
