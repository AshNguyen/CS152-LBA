from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # Global handle to interpreter


def query_the_KB(query): 
    price, distance, cuisine_type = query
    retractall = Functor("retractall")
    known = Functor("known",3)
    
    def read_list_choice_py(A, V, Y): 
        if str(A) == 'price':
            Y.unify(price.lower())
            return True
        elif str(A) == 'distance':
            Y.unify(distance.lower())
            return True
        elif str(A) == 'cuisine_type':
            Y.unify(cuisine_type.lower())
            return True

    read_list_choice_py.arity = 3
    registerForeign(read_list_choice_py)


    prolog.consult("KB.pl") # open the KB
    call(retractall(known))

    results = []
    for result in prolog.query("restaurant(X).", maxresult=30):
        results.append(result['X'])
    return results

for query in queries_from_GUI: 
	print(query_the_KB(query))