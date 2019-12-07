import sys
sys.path.insert(1, '../')

from Functions.Tif import *
from Definitions.types import TYPE

class TestTif:

    def test_tif_ok_numbers(self):
        node = {
            "description": "tif",
            "elements": {
                "e1": "true",
                "e2": "40",
                "e3": "70"
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.INT

    def test_tif_ok_boolean(self):
        node = {
            "description": "tif",
            "elements": {
                "e1": "false",
                "e2": "true",
                "e3": "false"
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.BOOL

    def test_tif_error_not_boolean(self):
        node = {
            "description": "tif",
            "elements": {
                "e1": "30",
                "e2": "true",
                "e3": "false"
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.ERROR

    def test_tif_error_different_return(self):
        node = {
            "description": "tif",
            "elements": {
                "e1": "true",
                "e2": "13",
                "e3": "false"
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.ERROR

    def test_tif_error_incorrect_description(self):
        node = {
            "description": "invalida",
            "elements": {
                "e1": "true",
                "e2": "7",
                "e3": "9"
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.ERROR