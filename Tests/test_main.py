import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from main import infer_type

class TestMain:

    # "(fn x: int => 2 + x) raise"
    def test_0(self):

        node_raise = {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        }

        node_add = {
            "description": "tarithm",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "2"
                    }
                },
                "e2": {
                    "description": "tvar",
                    "elements": {
                        "e1": "x"
                    }
                },
                "e3": "+"
            }
        }
        node_function = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": node_add
            }
        }

        node_app = {
            "description": "tapp",
            "elements": {
                "e1": node_function,
                "e2": node_raise
            }
        }

        assert infer_type({}, node_app) == TYPE.INT

    # "(fn x: int => 2 + raise) raise"
    def test_1(self):

        node_raise = {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        }

        node_add = {
            "description": "tarithm",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "2"
                    }
                },
                "e2": node_raise,
                "e3": "+"
            }
        }
        node_function = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": node_add
            }
        }

        node_app = {
            "description": "tapp",
            "elements": {
                "e1": node_function,
                "e2": node_raise
            }
        }

        assert infer_type({}, node_app) == TYPE.INT
