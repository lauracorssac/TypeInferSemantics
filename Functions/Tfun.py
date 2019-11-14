import main
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
def t_fun(environment, node):
    from main import infer_type
    
    parameter = node["elements"]["e1"]
    parameter_type = node["elements"]["e2"]

    environment[parameter] = parameter_type

    body_type = infer_type(environment, node["elements"]["e3"])

    return TYPE.FUNC(parameter_type, body_type)
