
% Enter your KB below this line:

restaurant('Taragui') :- price('$'), distance('close'), cuisine_type('argentinian').
restaurant('Santos Manjares') :- price('$$'), distance('close'), cuisine_type('argentinian').
restaurant('Ditali') :- price('$'), distance('close'), cuisine_type('argentinian').
restaurant('Elena') :- price('$$$'), distance('medium'), cuisine_type('argentinian').
restaurant('Las Cabras') :- price('$$'), distance('far'), cuisine_type('argentinian').
restaurant('Chori') :- price('$'), distance('far'), cuisine_type('argentinian').
restaurant('Pizzeria Guerrin') :- price('$'), distance('medium'), cuisine_type('argentinian').
restaurant('El Cuartito') :- price('$'), distance('medium'), cuisine_type('argentinian').
restaurant('Saigon Noodle Bar') :- price('$'), distance('close'), cuisine_type('asian').
restaurant('Fa Song Song') :- price('$'), distance('close'), cuisine_type('asian').
restaurant('Bao Kitchen') :- price('$$'), distance('medium'), cuisine_type('asian').
restaurant('Tea Connection') :- price('$'), distance('medium'), cuisine_type('cafe').
restaurant('All Saints') :- price('$'), distance('medium'), cuisine_type('cafe').
restaurant('Ninina') :- price('$'), distance('far'), cuisine_type('cafe').
restaurant('Cuervo') :- price('$'), distance('far'), cuisine_type('cafe').
restaurant('Le Pain Quotidien') :- price('$'), distance('medium'), cuisine_type('cafe').
restaurant('Hacienda') :- price('$'), distance('far'), cuisine_type('cafe').
restaurant('Negro') :- price('$'), distance('close'), cuisine_type('cafe').
restaurant('Casa Cavia') :- price('$$$'), distance('far'), cuisine_type('contemporary').
restaurant('El Baqueano') :- price('$$$'), distance('medium'), cuisine_type('contemporary').
restaurant('Lucciano') :- price('$'), distance('far'), cuisine_type('ice cream').
restaurant('Alchemy') :- price('$'), distance('far'), cuisine_type('ice cream').
restaurant('Rapa Nui') :- price('$'), distance('close'), cuisine_type('ice cream').
restaurant('Heladeria Esmeralda') :- price('$'), distance('close'), cuisine_type('ice cream').
restaurant('Brocollino') :- price('$$'), distance('close'), cuisine_type('italian').
restaurant('Sottovoce') :- price('$$$'), distance('medium'), cuisine_type('italian').
restaurant('Piola') :- price('$$'), distance('medium'), cuisine_type('italian').
restaurant('Core Italian') :- price('$'), distance('close'), cuisine_type('italian').
restaurant('Tanta') :- price('$$'), distance('close'), cuisine_type('peruvian').
restaurant('La Mar') :- price('$$$'), distance('far'), cuisine_type('peruvian').

price(X) :- ask_list(price, X, '[$, $$, $$$]'). 
distance(X) :- ask_list(distance, X, '[close, medium, far]'). 
cuisine_type(X) :- ask_list(cuisine_type, X, '[asian, argentinian, cafe, contemporary, ice cream, peruvian, italian]').

% The code below implements the prompting to ask the user:

ask_list(A, V, List):-
known(yes, A, V), 
!.

ask_list(A, V, List):-
known(yes, A, _),
!, fail.

ask_list(A, V, List):-
read_list_choice_py(A, V, Y),
asserta(known(yes, A, Y)), 
Y = V.
