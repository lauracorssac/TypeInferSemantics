import sys
sys.path.insert(1, '../')

from Functions.Traise import t_raise as t_raise
from Definitions.types import TYPE as TYPE

class TestTRaise:

    # Input:
    def test_right_input(self):
        node = {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        }
        assert t_raise({}, node) == TYPE.UNDEFINED

    def test_wrong_input(self):

        node = {
            "description": "traise",
            "elements": {
                "e1": "BLA"
            }
        }
        assert t_raise({}, node) == TYPE.ERROR

    def test_invalid_input(self):

        node_no_ele = {
            "description": "traise"
        }
        assert t_raise({}, node_no_ele) == TYPE.ERROR

        node_no_e1 = {
            "description": "traise",
            "elements": {}
        }
        assert t_raise({}, node_no_e1) == TYPE.ERROR
