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
