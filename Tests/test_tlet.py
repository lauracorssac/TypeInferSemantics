import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from Functions.Tlet import t_let

class TestTLet:

    # Input: let x: int = "2" in x
    # Output: TYPE.INT
    def test_t_let_0(self):

        node_1 = {
            "description": "tint",
            "elements": {
                 "e1" : "2"
            }
        }

        node_2 = {
            "description": "tvar",
            "elements": {
                "e1": "x"
            }
        }

        node_main = {
            "description": "tlet",
            "elements": {
                "e1": node_1,
                "e2" : node_2,
                "e3" : "x",
                "e4": TYPE.INT
            }
        }
        assert t_let({}, node_main) == TYPE.INT
        assert t_let({"x": TYPE.BOOL}, node_main) == TYPE.INT

    # Invalid Inputs
    def test_t_let_1(self):
        assert t_let({"x": TYPE.INT}, {}) == TYPE.ERROR
        assert t_let({}, {"elements": {"e3": "x"}}) == TYPE.ERROR

    # Input: let x: bool = "2" in x
    # Output: TYPE.ERROR (2 not type bool)
    def test_t_let_2(self):
        node_1 = {
            "description": "tint",
            "elements": {
                 "e1" : "2"
            }
        }

        node_2 = {
            "description": "tvar",
            "elements": {
                "e1": "x"
            }
        }

        node_main = {
            "description": "tlet",
            "elements": {
                "e1": node_1,
                "e2" : node_2,
                "e3" : "x",
                "e4": TYPE.BOOL
            }
        }
        assert t_let({}, node_main) == TYPE.ERROR
        assert t_let({"x": TYPE.INT}, node_main) == TYPE.ERROR
        assert t_let({"x": TYPE.BOOL}, node_main) == TYPE.ERROR
