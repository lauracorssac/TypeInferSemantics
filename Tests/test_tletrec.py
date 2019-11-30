import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from Functions.Tletrec import t_letrec
from Functions.Tletrec import parameters_are_valid

# tests are not supposed to pass until all its dependencies are ready
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

    def test_t_letrec_0(self):

        param = {
            "description": "tvar",
            "elements": {
               "e1": "x"
            }
        }
        e1 = {
            "description": "tbool",
            "elements": { "e1": "True" }
        }

        e2 = {
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
        }

        node = {
            "description": "tletrec",
            "elements": {
                "function_name": "f",
                 "type1": TYPE.INT,
                 "type2": TYPE.BOOL,
                 "param": param,
                 "e1": e1,
                 "e2": e2
            }
        }

        # Input: let rec f: INT -> BOOL = (fn x: INT => True) in f 4
        # Output: BOOL
        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.BOOL

    def test_t_letrec_3(self):

        e2 = {
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
        }

        param = {
            "description": "tvar",
            "elements": {
               "e1": "x"
            }
        }

        e1 = param

        node = {
            "description": "tletrec",
            "elements": {
                "function_name": "f",
                 "type1": TYPE.INT,
                 "type2": TYPE.BOOL,
                 "param": param,
                 "e1": e1,
                 "e2": e2
            }
        }

        # Input: let rec f: INT -> BOOL = (fn x: INT => x) in f 4
        # Output: BOOL

        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.ERROR

    def test_t_letrec_2(self):

        e2 = {
            "description": "tapp",
            "elements": {
               "e1": {
                   "description": "tvar",
                   "elements": {
                       "e1": "f"
                   }
               },
               "e2": {
                   "description": "Tbool",
                   "elements": {
                       "e1" : "True"
                   }
               }
           }
        }

        e1 = {
            "description": "tvar",
            "elements": { "e1": "x" }
        }

        param = {
            "description": "tvar",
            "elements": {
               "e1": "x"
            }
        }

        node = {
            "description": "tletrec",
            "elements": {
                "function_name": "f",
                 "type1": TYPE.INT,
                 "type2": TYPE.INT,
                 "param": param,
                 "e1": e1,
                 "e2": e2
            }
        }

        # Input: let rec f: INT -> INT = (fn x: INT => x) in f True
        # Output: ERROR

        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.ERROR

    def test_t_letrec_1(self):

        param = {
            "description": "tvar",
            "elements": {
               "e1": "x"
            }
        }

        e2 = {
            "description": "tvar",
            "elements": {
                "e1": "x"
            }
        }

        e1 = e2

        node = {
            "description": "tletrec",
            "elements": {
                "function_name": "f",
                 "type1": TYPE.INT,
                 "type2": TYPE.INT,
                 "param": param,
                 "e1": e1,
                 "e2": e2
            }
        }

        # Input: let rec f: INT -> INT = (fn x: INT => x) in x
        # env: {} Output: ERROR
        # env: {"x": TYPE.INT} Output: INT

        assert parameters_are_valid({}, node) == True
        assert t_letrec({}, node) == TYPE.ERROR
        assert t_letrec({"x": TYPE.INT}, node) == TYPE.INT
