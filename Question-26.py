% --- KNOWLEDGE BASE: Recommended & Restricted Foods ---
% Format: diet_plan(Disease, RecommendedFoods, FoodsToAvoid, GeneralAdvice).

diet_plan(diabetes, 
    ['Whole grains (oats, brown rice)', 'Leafy greens (spinach, kale)', 'Legumes and beans', 'Fatty fish', 'Nuts and seeds'],
    ['Sugary drinks and sodas', 'White bread and refined pasta', 'Sweets and pastries', 'Fried foods'],
    'Focus on low-glycemic index foods and eat at regular intervals to maintain steady blood sugar.'
).

diet_plan(hypertension, 
    ['Bananas and potassium-rich fruits', 'Leafy greens', 'Oatmeal', 'Berries', 'Low-fat yogurt', 'Garlic and herbs'],
    ['Table salt and high-sodium foods', 'Canned soups and processed meats', 'Pickles', 'Alcohol and excess caffeine'],
    'Follow the DASH diet approach: limit sodium intake to under 1,500-2,300 mg per day.'
).

diet_plan(anemia, 
    ['Red meat and poultry', 'Spinach and dark leafy greens', 'Lentils and chickpeas', 'Pumpkin seeds', 'Citrus fruits (for Vitamin C)'],
    ['Tea and coffee during meals', 'Calcium-rich foods right alongside iron-rich meals', 'Processed grains'],
    'Pair iron-rich foods with Vitamin C (like lemon or oranges) to boost iron absorption.'
).

diet_plan(gastritis, 
    ['Bananas', 'Oatmeal and plain rice', 'Boiled vegetables', 'Ginger tea', 'Lean proteins (chicken breast, tofu)', 'Probiotic yogurt'],
    ['Spicy foods and chili', 'Citrus fruits and tomatoes', 'Coffee and carbonated drinks', 'Fried and fatty foods', 'Alcohol'],
    'Eat smaller, more frequent meals to prevent stomach acid buildup.'
).

diet_plan(heart_disease, 
    ['Salmon and mackerel (Omega-3)', 'Avocados and olive oil', 'Walnuts and almonds', 'Whole grains', 'Fresh vegetables and berries'],
    ['Trans fats and hydrogenated oils', 'Red and processed meats', 'Full-fat dairy', 'Excess salt and sugar'],
    'Prioritize healthy unsaturated fats and high-fiber foods to lower LDL cholesterol.'
).

% --- RULES FOR QUERYING ---

% Rule to check if a specific food is safe for a disease
is_safe(Food, Disease) :-
    diet_plan(Disease, Recommended, _, _),
    member(Food, Recommended).

% Rule to check if a specific food should be avoided
should_avoid(Food, Disease) :-
    diet_plan(Disease, _, Avoid, _),
    member(Food, Avoid).

% Helper predicate to print lists neatly
print_list([]).
print_list([Head|Tail]) :-
    write('  - '), write(Head), nl,
    print_list(Tail).

% --- INTERACTIVE USER INTERFACE ---

start :-
    nl,
    write('========================================='), nl,
    write('   PROLOG DISEASE-BASED DIET ADVISOR     '), nl,
    write('========================================='), nl,
    write('Available conditions in database:'), nl,
    write('  1. diabetes'), nl,
    write('  2. hypertension'), nl,
    write('  3. anemia'), nl,
    write('  4. gastritis'), nl,
    write('  5. heart_disease'), nl, nl,
    write('Enter the disease name followed by a period (e.g., diabetes.): '),
    read(Disease),
    suggest_diet(Disease).

suggest_diet(Disease) :-
    diet_plan(Disease, Recommended, Avoid, Advice), !,
    nl,
    write('--- DIET PLAN FOR: '), write(Disease), write(' ---'), nl, nl,
    write('[+] RECOMMENDED FOODS:'), nl,
    print_list(Recommended), nl,
    write('[-] FOODS TO AVOID:'), nl,
    print_list(Avoid), nl,
    write('[*] KEY ADVICE: '), write(Advice), nl,
    write('========================================='), nl.

suggest_diet(_) :-
    nl,
    write('Sorry, that condition is not in our current knowledge base.'), nl,
    write('Please check your spelling and ensure it ends with a period.'), nl.
