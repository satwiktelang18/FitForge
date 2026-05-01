MEAL_PLANS = {
    'Fat Loss': {
        'Vegetarian': [
            {'meal': 'Breakfast',     'option': 'Greek yogurt parfait with granola, mixed berries & chia seeds', 'cal': 320},
            {'meal': 'Mid-Morning',   'option': 'Apple + 15 almonds + green tea', 'cal': 160},
            {'meal': 'Lunch',         'option': 'Paneer bhurji with 2 whole wheat rotis + cucumber raita', 'cal': 450},
            {'meal': 'Evening Snack', 'option': 'Roasted chickpeas + black coffee', 'cal': 140},
            {'meal': 'Dinner',        'option': 'Dal tadka + 1 roti + steamed broccoli & carrot salad', 'cal': 420},
        ],
        'Non-Vegetarian': [
            {'meal': 'Breakfast',     'option': '3 boiled eggs + 1 slice whole wheat toast + black coffee', 'cal': 310},
            {'meal': 'Mid-Morning',   'option': 'Apple + 10 almonds', 'cal': 150},
            {'meal': 'Lunch',         'option': 'Grilled chicken breast (150g) + quinoa + cucumber salad with lemon dressing', 'cal': 430},
            {'meal': 'Evening Snack', 'option': 'Tuna (canned in water) + rice cakes', 'cal': 160},
            {'meal': 'Dinner',        'option': 'Baked salmon (150g) + steamed broccoli + mixed greens salad', 'cal': 420},
        ],
    },
    'Muscle Gain': {
        'Vegetarian': [
            {'meal': 'Breakfast',     'option': 'Oats cooked in milk + 2 boiled eggs + banana + peanut butter', 'cal': 650},
            {'meal': 'Mid-Morning',   'option': 'Paneer cubes (100g) + mixed nuts + whole fruit', 'cal': 400},
            {'meal': 'Lunch',         'option': 'Rajma or chole (1 cup) + 2 cups rice + curd + salad', 'cal': 720},
            {'meal': 'Evening Snack', 'option': 'Whey protein shake (if using) or 250ml full-fat milk + banana', 'cal': 380},
            {'meal': 'Dinner',        'option': 'Tofu stir fry with vegetables + 1.5 cups brown rice + dal', 'cal': 680},
        ],
        'Non-Vegetarian': [
            {'meal': 'Breakfast',     'option': '5 scrambled eggs + 2 whole wheat toast + glass of whole milk + banana', 'cal': 700},
            {'meal': 'Mid-Morning',   'option': 'Whey protein shake + peanut butter + oats', 'cal': 420},
            {'meal': 'Lunch',         'option': 'Chicken breast (200g) + 2 cups white rice + vegetables + curd', 'cal': 780},
            {'meal': 'Evening Snack', 'option': 'Boiled eggs (3) + peanut butter on toast', 'cal': 380},
            {'meal': 'Dinner',        'option': 'Beef or mutton (150g) + sweet potato + steamed veggies + salad', 'cal': 720},
        ],
    },
    'Maintenance': {
        'Vegetarian': [
            {'meal': 'Breakfast',     'option': 'Vegetable oats upma + 2 boiled eggs + tea', 'cal': 420},
            {'meal': 'Mid-Morning',   'option': 'Mixed fruit bowl + handful of walnuts', 'cal': 200},
            {'meal': 'Lunch',         'option': 'Whole wheat roti (2) + sabzi + dal + curd + salad', 'cal': 520},
            {'meal': 'Evening Snack', 'option': 'Sprout chaat + buttermilk', 'cal': 200},
            {'meal': 'Dinner',        'option': 'Paneer tikka + brown rice (1 cup) + raita + salad', 'cal': 520},
        ],
        'Non-Vegetarian': [
            {'meal': 'Breakfast',     'option': 'Egg omelette (3 eggs) with veggies + 2 whole wheat toast + orange juice', 'cal': 430},
            {'meal': 'Mid-Morning',   'option': 'Greek yogurt + mixed berries', 'cal': 190},
            {'meal': 'Lunch',         'option': 'Chicken curry (medium portion) + 2 rotis + dal + salad', 'cal': 540},
            {'meal': 'Evening Snack', 'option': 'Boiled egg (2) + fruit', 'cal': 200},
            {'meal': 'Dinner',        'option': 'Grilled fish or chicken (120g) + vegetables + 1 cup rice', 'cal': 490},
        ],
    }
}

def recommend_meals(goal, diet_type='Non-Vegetarian'):
    goal_plans = MEAL_PLANS.get(goal, MEAL_PLANS['Maintenance'])
    return goal_plans.get(diet_type, goal_plans['Non-Vegetarian'])