import sys
sys.path.insert(1, '../')

from Functions.Tfun import *
from Definitions.types import TYPE

class TestTFun:

    def test_tfun_var_ok(self):
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

    def test_tfun_bool_ok(self):
        node = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                }
            }
        }
        environment = {}
        assert t_fun(environment, node) == "(" + TYPE.INT + ")->" + TYPE.BOOL
        assert t_fun(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.BOOL)

    def test_tfun_int_ok(self):
        node = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": {
                    "description": "tint",
                    "elements": {
                        "e1": "5"
                    }
                }
            }
        }
        environment = {}
        assert t_fun(environment, node) == "(" + TYPE.INT + ")->" + TYPE.INT
        assert t_fun(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.INT)


