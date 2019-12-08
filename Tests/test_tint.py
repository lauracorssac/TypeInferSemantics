import sys
sys.path.insert(1, '../')

from Functions.Tint import *
from Definitions.types import TYPE

class TestTint:

    def test_tint_ok(self):
        node = {
            "description": "tint",
            "elements": {
                "e1": "7"
            }
        }

        environment = {}
        assert t_int(environment, node) == TYPE.INT

    def test_tint_ok_giant_number(self):
        node = {
            "description": "tint",
            "elements": {
                "e1": "789637895059"
            }
        }

        environment = {}
        assert t_int(environment, node) == TYPE.INT

    def test_tint_error_boolean(self):
        node = {
            "description": "tint",
            "elements": {
                "e1": "true"
            }
        }    
    
        environment = {}
        assert t_int(environment, node) == TYPE.ERROR 

    def test_tint_error_symbol(self):
        node = {
            "description": "tint",
            "elements": {
                "e1": "#$%¨&*()"
            }
        }    
    
        environment = {}
        assert t_int(environment, node) == TYPE.ERROR 