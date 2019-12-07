from Definitions.types import TYPE

# Input example:
#
# empty
#
# node = {
#     "description": "tempty",
#     "elements": {
#         "e1": "empty"
#     }
# }
#
# Return:
#    TYPE.EMPTY


def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_empty(environment, term):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type

    value = int(node['elements']['e1'])

    if value is "empty": # it is "every type" type. Set it as the type of the list
                         # Only determines something if the list itself is empty
                         # but them the list can be a list of anything
        return TYPE.EMPTY
    else:
        return TYPE.ERROR
