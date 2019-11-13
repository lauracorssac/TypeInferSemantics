import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from Functions.Tlet import t_let

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
