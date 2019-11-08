from Definitions.types import TYPE
from Functions.Tvar import t_var

def test_tvar():
    node_x = { "description": "x"}
    node_y = { "description": "y"}
    node_z = { "description": "z"}
    node_fake = {"no_desc": "y"}

    assert(t_var({"x": TYPE.BOOL}, node_x) == TYPE.BOOL)
    assert(t_var({"x": TYPE.BOOL}, node_y) == TYPE.ERROR)

    assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, node_y) == TYPE.ERROR)
    assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, node_x) == TYPE.BOOL)
    assert(t_var( {"z": TYPE.FUNC(TYPE.INT, TYPE.INT), "x": TYPE.BOOL}, node_z) == TYPE.FUNC(TYPE.INT, TYPE.INT))
    assert(t_var({}, node_x) == TYPE.ERROR)
    assert(t_var(None, node_x) == TYPE.ERROR)
    assert(t_var({"x": TYPE.BOOL}, node_fake) == TYPE.ERROR)
    assert(t_var({"x": TYPE.BOOL}, None) == TYPE.ERROR)

    print("testes t-var passaram")
