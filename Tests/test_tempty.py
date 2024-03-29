import sys
sys.path.insert(1, '../')

from Functions.Tempty import *
from Definitions.types import TYPE

class TestTempty:

    def test_tempty_ok(self):
        node = {
            "description": "tempty",
            "elements": {
                "e1": "empty"
            }
        }
        environment = {}
        assert t_empty(environment, node) == TYPE.LIST(TYPE.EMPTY)

    def test_tint_error1(self):
        node = {
            "description": "tempty",
            "elements": {
                "e1": "true"
            }
        }
        environment = {}
        assert t_empty(environment, node) == TYPE.ERROR

    def test_tint_error2(self):
        node = {
            "description": "tempty",
            "elements": {
                "e1": "1"
            }
        }
        environment = {}
        assert t_empty(environment, node) == TYPE.ERROR
