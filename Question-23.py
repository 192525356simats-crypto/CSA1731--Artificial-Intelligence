% Base Case: Move a single disk directly from Source to Target
move(1, Source, Target, _) :-
    write('Move top disk from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.

% Recursive Case: Move N disks from Source to Target using Auxiliary
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(M, Auxiliary, Target, Source).
