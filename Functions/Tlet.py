from Definitions.types import TYPE

# Example Node
#
# let x: int = 2 in x
#
# {
#    description: "tlet",
#    elements: {
#        "e1": {
#            "description": "tint",
#            "elements": {
#                 "e1" : "2"
#            }
#        },
#        "e2" : {
#            "description": "tvar",
#            "elements": {
#                "e1": "x"
#            }
#        },
#        "e3" : "x",
#        "e4": TYPE.INT
# }

def t_let(environment, node):
    from main import infer_type

    if node and "elements" in node:
        elements = node["elements"]
    else:
        return TYPE.ERROR

    if "e1" in elements and "e2" in elements and "e3" in elements and "e4" in elements:
        param = elements["e3"]
        param_type = elements["e4"]
        e1 = elements["e1"]
        e2 = elements["e2"]
    else:
        return TYPE.ERROR

    if infer_type(environment, e1) == param_type:
        if not environment:
            environment = {}
        environment[param] = param_type
        return infer_type(environment, e2)

    return TYPE.ERROR
