WORKOUT_PLANS = {
    'Fat Loss': {
        'plan': 'Strength + Cardio Circuit (5 days)',
        'days': [
            {
                'day': 'Monday',
                'focus': 'Upper Body Strength',
                'workout': 'Bench Press 3×10 · Dumbbell Rows 3×12 · Overhead Press 3×10 · Tricep Pushdowns 3×15 · Face Pulls 3×15'
            },
            {
                'day': 'Tuesday',
                'focus': 'Cardio Burn',
                'workout': '30 min moderate run or cycling · 3 rounds: 20 Jump Squats + 15 Burpees + 10 Push-ups (60 sec rest)'
            },
            {
                'day': 'Wednesday',
                'focus': 'Lower Body Strength',
                'workout': 'Barbell Squats 4×8 · Romanian Deadlifts 3×10 · Leg Press 3×12 · Walking Lunges 3×20 · Calf Raises 4×15'
            },
            {
                'day': 'Thursday',
                'focus': 'Active Recovery',
                'workout': '20 min brisk walk · Full body stretching · Foam rolling · Core: Planks 3×45 sec + Dead Bug 3×10'
            },
            {
                'day': 'Friday',
                'focus': 'Full Body Power',
                'workout': 'Deadlifts 4×6 · Pull-ups or Lat Pulldown 3×10 · Dumbbell Lunges 3×12 · Skull Crushers 3×12 · Bicep Curls 3×12'
            },
            {
                'day': 'Saturday',
                'focus': 'Cardio + Core',
                'workout': '20 min cycling or stair climber · Core circuit: Crunches 3×20 + Leg Raises 3×15 + Russian Twists 3×20 + Plank 3×45 sec'
            },
            {
                'day': 'Sunday',
                'focus': 'Rest',
                'workout': 'Complete rest or 20 min light yoga / stretching'
            },
        ]
    },
    'Muscle Gain': {
        'plan': 'Push / Pull / Legs — PPL Split (6 days)',
        'days': [
            {
                'day': 'Monday',
                'focus': 'Push (Chest · Shoulders · Triceps)',
                'workout': 'Barbell Bench Press 4×6 · Incline Dumbbell Press 3×10 · Overhead Press 4×8 · Lateral Raises 4×15 · Skull Crushers 3×12 · Tricep Dips 3×10'
            },
            {
                'day': 'Tuesday',
                'focus': 'Pull (Back · Biceps)',
                'workout': 'Deadlifts 4×5 · Pull-ups 4×8 · Barbell Rows 4×8 · Lat Pulldown 3×10 · Face Pulls 3×15 · Hammer Curls 3×12 · Preacher Curls 3×10'
            },
            {
                'day': 'Wednesday',
                'focus': 'Legs (Quads · Hamstrings · Glutes)',
                'workout': 'Barbell Back Squat 4×6 · Romanian Deadlifts 3×10 · Leg Press 4×12 · Leg Curls 3×12 · Walking Lunges 3×16 · Calf Raises 5×15'
            },
            {
                'day': 'Thursday',
                'focus': 'Push (Progressive overload)',
                'workout': 'Incline Bench Press 4×8 · Dumbbell Shoulder Press 3×10 · Cable Crossover 3×15 · Tricep Pushdowns 4×12 · Overhead Tricep Extension 3×12'
            },
            {
                'day': 'Friday',
                'focus': 'Pull (Progressive overload)',
                'workout': 'Weighted Pull-ups 4×6 · Seated Cable Rows 4×10 · Single-Arm Dumbbell Row 3×10 · Reverse Flyes 3×15 · Barbell Curl 4×10 · Concentration Curls 3×12'
            },
            {
                'day': 'Saturday',
                'focus': 'Legs + Core',
                'workout': 'Front Squats 4×8 · Sumo Deadlifts 3×8 · Leg Press 3×15 · Hip Thrusts 4×12 · Plank 3×60 sec · Cable Crunches 3×20'
            },
            {
                'day': 'Sunday',
                'focus': 'Rest',
                'workout': 'Complete rest · Light stretching · Prioritize 8h sleep for muscle recovery'
            },
        ]
    },
    'Maintenance': {
        'plan': 'Full Body Training — 4 days/week',
        'days': [
            {
                'day': 'Monday',
                'focus': 'Full Body Strength A',
                'workout': 'Barbell Squats 3×8 · Bench Press 3×8 · Barbell Rows 3×8 · Overhead Press 3×10 · Dips 2×12 · Pull-ups 2×8'
            },
            {
                'day': 'Tuesday',
                'focus': 'Cardio + Mobility',
                'workout': '30 min jog or cycling at moderate pace · Hip flexor stretches · Shoulder mobility drills · Foam rolling'
            },
            {
                'day': 'Wednesday',
                'focus': 'Active Recovery',
                'workout': 'Light walking · Yoga or stretching · Core: Planks 3×45 sec + Bird Dog 3×10 each side'
            },
            {
                'day': 'Thursday',
                'focus': 'Full Body Strength B',
                'workout': 'Deadlifts 3×6 · Incline Dumbbell Press 3×10 · Lat Pulldown 3×10 · Leg Press 3×12 · Bicep Curls 3×12 · Tricep Pushdowns 3×12'
            },
            {
                'day': 'Friday',
                'focus': 'Cardio + Core',
                'workout': '20 min cycling · Core circuit: Crunches 3×20 + Leg Raises 3×15 + Russian Twists 3×20 + Side Planks 2×30 sec each'
            },
            {
                'day': 'Saturday',
                'focus': 'Sport / Recreation',
                'workout': 'Basketball · Swimming · Tennis · Hiking · or any sport you enjoy — keep it fun'
            },
            {
                'day': 'Sunday',
                'focus': 'Rest',
                'workout': 'Complete rest — recovery is as important as training'
            },
        ]
    }
}

def recommend_workout(goal):
    return WORKOUT_PLANS.get(goal, WORKOUT_PLANS['Maintenance'])