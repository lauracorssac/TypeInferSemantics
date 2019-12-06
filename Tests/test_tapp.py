import sys
sys.path.insert(1, '../')

from Functions.Tapp import *
from Definitions.types import TYPE

class TestTApp:

    def test_tapp_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": {
                    "description": "tvar",
                    "elements": {
                        "e1": "x"
                    }
                }
            }
        }

        node3 = {
            "description": "tint",
            "elements": {
                "e1": "7"
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}
        # result, expected_parameter, received_parameter = t_app(environment, node)

        # print('como')
        # print(expected_parameter)
        # print('ratata')
        # print(received_parameter)
        # print('demonio')
        # print(result)
        assert t_app(environment, node) == TYPE.INT
        # assert t_fun(environment, node) == "(" + TYPE.INT + ")->" + TYPE.INT
        # assert t_fun(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.INT)
