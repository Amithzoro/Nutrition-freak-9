def generate_goal_advice(goal, protein, calories):
    if goal == "Cutting":
        if calories > 650:
            return "⚠️ Slightly high calories for fat loss — reduce carbs next meal & add more greens."
        if protein < 25:
            return "🔶 Protein is low — add chicken / egg / whey to speed up fat loss."
        return "🔥 Great for cutting — high protein & moderate calories. Try to avoid carbs after 7 PM."

    elif goal == "Bulking":
        if calories < 600:
            return "💪 Increase calories for bulking — add rice/oats or peanut butter next meal."
        if protein < 35:
            return "🍗 Boost protein — add eggs or paneer to hit hypertrophy range."
        return "🔥 Perfect for bulking — strong protein + good calories for muscle growth."

    elif goal == "Maintenance":
        if calories > 700:
            return "⚠️ High calories for maintenance — add more veggies for balance."
        return "👌 Balanced meal — fits well for maintenance. Keep hydration high."

    return ""
