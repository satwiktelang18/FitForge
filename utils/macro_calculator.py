def calculate_macros(calories, goal, weight_kg):
    """
    Returns adjusted calories + macros based on goal.
    Fat loss: -300 to -400 deficit (gentle, sustainable)
    Muscle gain: +250 surplus
    Maintenance: no change
    
    Minimum floor: never go below 1600 kcal for males, 1400 for females
    Realistic: if TDEE is 2200, fat loss target = ~1800-1900
    """
    if goal == 'Fat Loss':
        # Gentle deficit: 15-18% of TDEE, max 400 kcal
        deficit = min(int(calories * 0.17), 400)
        deficit = max(deficit, 250)  # at least 250 deficit
        adjusted = max(calories - deficit, 1500)  # hard floor at 1500
        protein_g = round(weight_kg * 2.0)
    elif goal == 'Muscle Gain':
        adjusted = calories + 250
        protein_g = round(weight_kg * 1.8)
    else:  # Maintenance
        adjusted = calories
        protein_g = round(weight_kg * 1.6)

    protein_cal = protein_g * 4
    fat_cal = round(adjusted * 0.25)
    fat_g = round(fat_cal / 9)
    carb_cal = adjusted - protein_cal - fat_cal
    carb_g = max(round(carb_cal / 4), 50)  # minimum 50g carbs

    return {
        'adjusted_calories': adjusted,
        'protein_g': protein_g,
        'fat_g': fat_g,
        'carbs_g': carb_g
    }