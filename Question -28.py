% --- Facts: fruit(Name, Color) ---
fruit(apple, red).
fruit(apple, green).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grape, purple).
fruit(grape, green).
fruit(cherry, red).
fruit(lemon, yellow).
fruit(blueberry, blue).

% --- Rules ---

% 1. Basic lookup rule (relies on user pressing ';' to backtrack)
has_color(Fruit, Color) :-
    fruit(Fruit, Color).

% 2. Forced backtracking using 'fail' to print all fruits of a given color
print_fruits_by_color(Color) :-
    fruit(Fruit, Color),
    write(Fruit), nl,
    fail.
print_fruits_by_color(_). % Catch-all rule so the query ends with 'true'

% 3. Forced backtracking to display the entire knowledge base
show_all_fruits :-
    fruit(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl,
    fail.
show_all_fruits.
