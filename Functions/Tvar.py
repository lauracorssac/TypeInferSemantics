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

    e1 = node['elements']['e1']
    if environment and e1 in environment:
        return environment[e1]
    else:
        return TYPE.ERROR
