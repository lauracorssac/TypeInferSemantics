#import mainFunction
from Definitions.types import TYPE

# Expected Node
# {
#   description: "qqr coisa",
#   elements: { "x" : nome_var, "T", "TYPE.INT", "e1": nodo_1, "e2" : nodo_2 }
# }

# TODO: - Tirar esse mock da main_function

def main_function(environment, node):
    return environment[node["description"]]

def t_let(environment, node):

    if environment and node and "elements" in node:
        elements = node["elements"]

        if "x" in elements and "T" in elements and "e1" in elements and "e2" in elements:
            param = elements["x"]
            param_type = elements["T"]
            e1 = elements["e1"]
            e2 = elements["e2"]

            if main_function(environment, e1) == param_type:
                environment[param] = param_type
                return main_function(environment, e2)

    return TYPE.ERROR

node_e2 = {
    "description": "y",
}

node_e1 = {
    "description": "z",
}

node_let = {
    "description": "let",
    "elements": {
        "x" : "y",
        "T": TYPE.INT,
        "e1": node_e1,
        "e2" : node_e2
    }
}

# entrada let y:INT = "z" in y

# teste sucesso
assert(t_let({"z": TYPE.INT}, node_let) == TYPE.INT)
# entrada tipo invalido
assert(t_let({"z": TYPE.BOOL}, node_let) == TYPE.ERROR)
# entrada nao declarada
assert(t_let({}, node_let) == TYPE.ERROR)
assert(t_let(None, node_let) == TYPE.ERROR)
assert(t_let({"z": TYPE.BOOL}, None) == TYPE.ERROR)

node_e22 = {
    "description": "w",
}

node_e12 = {
    "description": "z",
}

node_let2 = {
    "description": "let",
    "elements": {
        "x" : "y",
        "T": TYPE.INT,
        "e1": node_e12,
        "e2" : node_e22
    }
}

# entrada let y:INT = "z" in "w"

# w é um bool, entrada certa
assert(t_let({"w": TYPE.BOOL, "z": TYPE.INT}, node_let2) == TYPE.BOOL)

# w é um bool, entrada errada
assert(t_let({"w": TYPE.BOOL, "z": TYPE.BOOL}, node_let2) == TYPE.ERROR)

node_let3 = {
    "description": "let",
    "elements": {
        "x" : "w",
        "T": TYPE.BOOL,
        "e1": node_e12,
        "e2" : node_e22
    }
}

# entrada let w:BOOL = "z" in "w"

# entrada certa, muda dict
assert(t_let({"w": TYPE.INT, "z": TYPE.BOOL}, node_let3) == TYPE.BOOL)

print("Testes t-let passaram")
