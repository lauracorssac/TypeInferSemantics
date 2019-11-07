import mainFunction
from Definitions.types import TYPE

# o que eu to pesando como entrada mas por enquanto mockei: [let-x-T, e1, e2]

def t_let(environment, term):
    
    param = "x" # como??
    param_type = "INT" #como??
    e1 = term[1]
    e2 = term[2]
    
    if main_function(environment, e1) == param_type:
        environment[param] = param_type
        return main_function(environment, e2)
    
    return TYPE.ERROR
