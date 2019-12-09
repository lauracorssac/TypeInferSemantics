from main import *

node_function = {
    "description": "tfun",
    "elements": {
        "e1": "x",
        "e2": TYPE.FUNC(TYPE.INT, TYPE.INT),
        "e3": {
            "description": "tbool",
            "elements": {
                "e1": "true"
            }
        }
    }
}

node_root = {
    "description": "tapp",
    "elements": {
        "e1": node_function,
        "e2": {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        },
    }
}

print(infer_type({}, node_root))
