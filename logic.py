from main import infer_type

node = {
    "description": "tlogic",
    "elements": {
        "e1": {
            "description": "tint",
            "elements": {
                "e1": "50"
            }
        },
        "e2": {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        },
        "e3": ">"
    }
}

print(infer_type({},node))
