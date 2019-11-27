import sys
sys.path.insert(1, '../')

from Functions.Tvar import t_var as t_var
from Definitions.types import TYPE as TYPE

class TestTVar:

    # Input:
    #     variable: x
    #     environment: {"x": TYPE.INT}
    def test_t_var_happy_path(self):

        node_x = {
            "description": "tvar",
            "elements": {"e1": "x"}
        }
        node_y = {
            "description": "tvar",
            "elements": {"e1": "y"}
        }

        assert t_var({"x": TYPE.INT}, node_x) == TYPE.INT
        assert t_var({"y": TYPE.BOOL}, node_y) == TYPE.BOOL
        assert t_var({"e1": TYPE.INT, "y": TYPE.BOOL}, node_y) == TYPE.BOOL

    def test_t_var_errors(self):

        node_x = {
            "description": "tvar",
            "elements": {"e1": "x"}
        }

        assert t_var({}, node_x) == TYPE.ERROR
        assert t_var(None, node_x) == TYPE.ERROR
        assert t_var(None, None) == TYPE.ERROR
        assert t_var({"x": TYPE.INT}, None) == TYPE.ERROR
        assert t_var({"x": TYPE.INT}, {}) == TYPE.ERROR
        assert t_var({"y": TYPE.INT}, node_x) == TYPE.ERROR
