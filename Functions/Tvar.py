from Definitions.types import TYPE

# Input example:
#
# node = {
#   "description": "tvar"
#   "elements": {"e1": "x"}
# }
#
# environment = {
#   "x": TYPE.INT
# }
#
# Return:
#   TYPE.INT
def t_var(environment, node):
    from main import infer_type

    if node and "elements" in node:
        elements = node['elements']
    else:
        return TYPE.ERROR

    if elements and "e1" in elements:
        e1 = elements['e1']
    else:
        return TYPE.ERROR

    if environment and e1 in environment:
        return environment[e1]
    else:
        return TYPE.ERROR
