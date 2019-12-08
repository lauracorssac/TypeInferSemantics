from Definitions.types import TYPE

# Input example:
#
# fn x:INT -> x
#
# node = {
#   "description": "tfun"
#   "elements": {
#        "e1": "x",
#        "e2": TYPE.INT,
#        "e3": {
#            "description": "tvar",
#            "elements":
#                {"e1": "x"}}}
# }
#
# environment = {}
#
# Return:
#   (TYPE.INT) -> (TYPE.INT)
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"] and "e2" in node["elements"] and "e3" in node["elements"]:
        return True
    else:
        return False

def t_fun(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type

    parameter = node["elements"]["e1"]
    parameter_type = node["elements"]["e2"]

    if parameter_type != TYPE.BOOL and parameter_type != TYPE.INT:
        parameter_type = infer_type(environment, parameter_type)

    environment[parameter] = parameter_type

    body_type = infer_type(environment, node["elements"]["e3"])
    if body_type != TYPE.UNDEFINED and parameter_type != TYPE.UNDEFINED:
        return TYPE.FUNC(parameter_type, body_type)

    return TYPE.ERROR
