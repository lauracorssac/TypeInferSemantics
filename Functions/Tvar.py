import main
from Definitions.types import TYPE

def t_var(environment, node):

    if node and "description" in node:
        term = node["description"]
        if environment and term in environment:
            return environment[term]
        else:
            return TYPE.ERROR
    else:
        return TYPE.ERROR
