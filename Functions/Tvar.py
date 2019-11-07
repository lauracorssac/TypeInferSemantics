import mainFunction
from Definitions.types import TYPE

def t_var(environment, term):
    
    if environment and term in environment:
        return environment[term]
    else:
        return TYPE.ERROR 
        
assert(t_var({"x": TYPE.BOOL}, "x") == TYPE.BOOL)
assert(t_var({"x": TYPE.BOOL}, "y") == TYPE.ERROR)
assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, "y") == TYPE.ERROR)
assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, "x") == TYPE.BOOL)
assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, "z") == TYPE.FUNC(TYPE.INT, TYPE.INT))
assert(t_var({}, "x") == TYPE.ERROR)
assert(t_var(None, "x") == TYPE.ERROR)
