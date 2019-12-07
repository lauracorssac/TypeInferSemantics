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
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL


    def test_tbool_lower_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "false"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL

    def test_tbool_upper_true(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "TRUE"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL

    def test_tbool_upper_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "FALSE"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL

    def test_tbool_mid_false(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "False"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.BOOL

    def test_tbool_error_number(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "8"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.ERROR

    def test_tbool_error_string(self):
        node = {
            "description": "tbool",
            "elements": {
                "e1": "BLABLABLA"
            }
        }
        environment = {}
        assert t_bool(environment, node) == TYPE.ERROR
