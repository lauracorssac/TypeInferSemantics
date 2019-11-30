import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from Functions.Tletrec import t_letrec
from Functions.Tletrec import parameters_are_valid

class TestTLetRec:

    def test_invalid_inputs(self):

        wrong_elements = {
            "function_name": "f",
             "type1": TYPE.INT,
             "type2": TYPE.INT,
             "param": {
                 "description": "tvar",
                 "elements": {}
             },
             "e1": {
                 "description": "tint",
                 "elements": { "e1": "2" }
             },
             "e2": {
                 "description": "tint",
                 "elements": { "e1": "4" }
             },
        }

        assert t_letrec({}, {}) == TYPE.ERROR
        assert t_letrec({"x": TYPE.INT}, {}) == TYPE.ERROR
        assert t_letrec({"x": TYPE.INT}, {"description": "tletrec" }) == TYPE.ERROR
        assert t_letrec( {"x": TYPE.INT}, {
            "description": "tletrec",
            "elements": {}
        }) == TYPE.ERROR
        assert t_letrec( {"x": TYPE.INT}, {
            "description": "tletrec",
            "elements": wrong_elements
        }) == TYPE.ERROR


    def test_t_letrec_int(self):

        elements = {
            "function_name": "f",
             "type1": TYPE.INT,
             "type2": TYPE.INT,
             "param": {
                 "description": "tvar",
                 "elements": {
                    "e1": "x"
                 }
             },
             "e1": {
                 "description": "tint",
                 "elements": { "e1": "2" }
             },
             "e2": {
                 "description": "tint",
                 "elements": { "e1": "4" }
             },
        }

        node = {
            "description": "tletrec",
            "elements": elements
        }

        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.INT


    # Input: let rec f: INT -> BOOL = (fn x: INT => True) in f 4
    # Output: BOOL
    def test_t_letrec_app(self):

        elements = {
            "function_name": "f",
             "type1": TYPE.INT,
             "type2": TYPE.BOOL,
             "param": {
                 "description": "tvar",
                 "elements": {
                    "e1": "x"
                 }
             },
             "e1": {
                 "description": "tbool",
                 "elements": { "e1": "True" }
             },
             "e2": {
                 "description": "tapp",
                 "elements": {
                    "e1": {
                        "description": "tvar",
                        "elements": {
                            "e1": "f"
                        }
                    },
                    "e2": {
                        "description": "tint",
                        "elements": {
                            "e1" : "4"
                        }
                    }
                }
             },
        }

        node = {
            "description": "tletrec",
            "elements": elements
        }

        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.BOOL
