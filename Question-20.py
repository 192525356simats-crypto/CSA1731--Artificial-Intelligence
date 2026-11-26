% Facts: dob(Name, Day, Month, Year)
dob(arun, 12, may, 2002).
dob(priya, 25, august, 2001).
dob(rahul, 4, january, 2003).
dob(deepa, 19, november, 2002).

% Rule to find people born in a specific year
born_in_year(Name, Year) :-
    dob(Name, _, _, Year).

% Rule to find people born in a specific month
born_in_month(Name, Month) :-
    dob(Name, _, Month, _).
