% Facts: planet(Name, Type, PositionFromSun, NumberOfMoons)
planet(mercury, rocky, 1, 0).
planet(venus, rocky, 2, 0).
planet(earth, rocky, 3, 1).
planet(mars, rocky, 4, 2).
planet(jupiter, gas_giant, 5, 95).
planet(saturn, gas_giant, 6, 146).
planet(uranus, ice_giant, 7, 28).
planet(neptune, ice_giant, 8, 16).

% Rule: Find planets with no moons
no_moons(Planet) :-
    planet(Planet, _, _, 0).

% Rule: Find all rocky planets
is_rocky(Planet) :-
    planet(Planet, rocky, _, _).
