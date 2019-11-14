import sys
sys.path.insert(1, '../')

from Functions.batata import *
from Functions.Tfun import *
from Definitions.types import TYPE

# class TestTfun:
    # def test_tfun_ok():
node = {
    "description": "tfun",
    "elements": {
        "e1": "x",
        "e2": TYPE.INT,
        "e3": {
            "description": "tvar",
            "elements": {
                "e1": "x"
            }
        }
    }
}
environment = {}
assert t_fun(environment, node) == "(" + TYPE.INT + ") -> " + TYPE.INT
