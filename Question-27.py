% State Representation:
% state(MonkeyHorizontalPos, MonkeyVerticalPos, BoxPos, HasBanana)
% Positions: at_door, at_window, middle
% Vertical: on_floor, on_box
% Possession: has, has_not

% 1. Grasp the banana
% Possible only if the monkey is in the middle, on the box, and doesn't have the banana.
move(state(middle, on_box, middle, has_not),
     grasp,
     state(middle, on_box, middle, has)).

% 2. Climb the box
% Possible if the monkey and the box are at the same location and the monkey is on the floor.
move(state(Pos, on_floor, Pos, Has),
     climb,
     state(Pos, on_box, Pos, Has)).

% 3. Push the box from Pos1 to Pos2
% Possible if both monkey and box are at Pos1 and the monkey is on the floor.
move(state(Pos1, on_floor, Pos1, Has),
     push(Pos1, Pos2),
     state(Pos2, on_floor, Pos2, Has)).

% 4. Walk from Pos1 to Pos2
% Possible if the monkey is on the floor (box position doesn't change).
move(state(Pos1, on_floor, BoxPos, Has),
     walk(Pos1, Pos2),
     state(Pos2, on_floor, BoxPos, Has)).

% Base Case: Goal state reached when the monkey has the banana.
canget(state(_, _, _, has), []).

% Recursive Case: Find a valid move to transition to a new state, then solve from there.
canget(State1, [Action | RestOfActions]) :-
    move(State1, Action, State2),
    canget(State2, RestOfActions).

% Helper predicate to run the standard scenario:
% Monkey starts at the door on the floor, box is at the window, monkey has no banana.
solve(Actions) :-
    canget(state(at_door, on_floor, at_window, has_not), Actions).
