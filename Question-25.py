% --- FACTS: Gender ---
male(john).
male(bob).
male(tom).
male(sam).

female(mary).
female(lisa).
female(ann).
female(sara).

% --- FACTS: Parent-Child Relationships ---
% parent(Parent, Child).
parent(john, bob).
parent(john, lisa).
parent(mary, bob).
parent(mary, lisa).

parent(bob, tom).
parent(bob, ann).
parent(sara, tom).
parent(sara, ann).

parent(lisa, sam).

% --- RULES: Immediate Family ---
father(X, Y) :- 
    parent(X, Y), 
    male(X).

mother(X, Y) :- 
    parent(X, Y), 
    female(X).

child(X, Y) :- 
    parent(Y, X).

sibling(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

brother(X, Y) :- 
    sibling(X, Y), 
    male(X).

sister(X, Y) :- 
    sibling(X, Y), 
    female(X).

% --- RULES: Extended Family ---
grandparent(X, Z) :- 
    parent(X, Y), 
    parent(Y, Z).

grandfather(X, Z) :- 
    grandparent(X, Z), 
    male(X).

grandmother(X, Z) :- 
    grandparent(X, Z), 
    female(X).

uncle(X, Y) :- 
    brother(X, Z), 
    parent(Z, Y).

aunt(X, Y) :- 
    sister(X, Z), 
    parent(Z, Y).

cousin(X, Y) :- 
    parent(P1, X), 
    parent(P2, Y), 
    sibling(P1, P2).

% --- RULES: Recursive Ancestor ---
ancestor(X, Y) :- 
    parent(X, Y).
ancestor(X, Y) :- 
    parent(X, Z), 
    ancestor(Z, Y).
