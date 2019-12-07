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

    def test_tint_error(self):
        node = {
            "description": "tint",
            "elements": {
                "e1": "true"
            }
        }    
    
        environment = {}
        assert t_int(environment, node) == TYPE.INT 