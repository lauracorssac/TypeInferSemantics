import sys
sys.path.insert(1, '../')

from Functions.Tfun import *
from Definitions.types import TYPE

class TestTFun:

    def test_tfun_ok(self):
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
        assert t_fun(environment, node) == "(" + TYPE.INT + ")->" + TYPE.INT
        assert t_fun(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.INT)
