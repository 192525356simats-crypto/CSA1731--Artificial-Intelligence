% --- Facts: Defining birds ---
bird(sparrow).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).
bird(kiwi).

% --- Facts: Exceptions (Birds that cannot fly) ---
cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% --- Rules ---
% A bird can fly if it is a bird and is NOT in the cannot_fly list.
can_fly(X) :- 
    bird(X), 
    \+ cannot_fly(X).

% Helper predicate to print the result clearly
check_flight(X) :-
    can_fly(X),
    write(X), write(' can fly.'), nl, !.

check_flight(X) :-
    bird(X),
    cannot_fly(X),
    write(X), write(' cannot fly.'), nl, !.

check_flight(X) :-
    write(X), write(' is not a known bird in the database.'), nl.
