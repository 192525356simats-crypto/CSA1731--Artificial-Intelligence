% --- 1. Graph Definition: edge(From, To) ---
edge(s, a).
edge(s, b).
edge(s, c).
edge(a, d).
edge(a, e).
edge(b, f).
edge(c, h).
edge(h, i).
edge(h, j).

% --- 2. Heuristic Values: h(Node, EstimatedCostToGoal) ---
h(s, 30).
h(a, 25).
h(b, 20).
h(c, 28).
h(d, 15).
h(e, 18).
h(f, 12).
h(h, 5).
h(i, 0).   % Goal node has a heuristic of 0
h(j, 10).

% --- 3. Entry Point ---
best_first_search(Start, Goal, Path) :-
    h(Start, H),
    % Open list stores nodes as: H_Value-[CurrentNode|PathTaken]
    search([H-[Start]], [], Goal, RevPath),
    reverse(RevPath, Path).

% --- 4. Search Loop ---
% Base case: The front node in the Open queue is the Goal
search([_-[Goal|RestPath] | _], _, Goal, [Goal|RestPath]) :- !.

% Recursive step: Expand the node with the lowest heuristic value
search([_-[Current|RestPath] | OpenTail], Closed, Goal, FinalPath) :-
    % Find all unvisited neighbors and pair them with their heuristic value
    findall(
        ChildH-[Child, Current|RestPath],
        (
            edge(Current, Child),
            \+ member(Child, [Current|RestPath]),
            \+ member(Child, Closed),
            h(Child, ChildH)
        ),
        Children
    ),
    % Merge new children into the Open list and sort by heuristic value (keysort)
    append(OpenTail, Children, UnsortedOpen),
    keysort(UnsortedOpen, SortedOpen),
    % Mark Current as visited in Closed and continue
    search(SortedOpen, [Current|Closed], Goal, FinalPath).
