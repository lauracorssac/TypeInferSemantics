import sys
sys.path.insert(1, '../')

from Functions.Tbool import *
from Definitions.types import TYPE

class TestTbool:

    def test_tbool_lower_true(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "true"
            }
        }

    def test_tbool_lower_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "false"
            }
        }

    def test_tbool_upper_true(self):
            node = {
                "description": "tbool",
                "elements": {
                    "e1": "TRUE"
                }
            }

    def test_tbool_upper_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "FALSE"
            }
        }

    def test_tbool_mid_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "False"
            }
        }    

    def test_tbool_error(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "8"
            }
        }    
    
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL 
