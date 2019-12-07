from Definitions.types import TYPE

# Input example:
#
# cons 1 [2]
#
# node = {
#     "description": "tcons",
#     "elements": {
#         "e1" : {
#             "description": "tint",
#             "elements": {"e1": "1"}
#         },
#         "e2" : {
#             "description": "tlist",
#             "elements": {
#                 "e1": {
#                     "description": "tint",
#                     "elements": {"e1": "2"}
#                 },
#                 "e2": {
#                     "description": "tempty",
#                     "elements": {"e1": "empty"}
#                 }
#             }
#         }
#     }
# }
#
# Return:
#    TYPE.LIST(TYPE.INT)

def isList(expression):
    if TYPE.LIST('') in expression:
        return True
    else:
        return False

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" and "e2" in node["elements"]:
        return True
    else:
        return False

def t_list(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    new = node["elements"]["e1"]
    list = node["elements"]["e2"]
    list_type = infer_type(environment, list)
    new_type = infer_type(environment, new)

    if isList(list_type): # consider case that is cons to a empty list!
        _, type = list_type.split(".", 1)

        if type == new_type: # both are undefined (cons undef empty) or tail not empty
            return list_type

        elif type == TYPE.UNDEFINED: # tail is empty but head is defined
            return TYPE.LIST(new_type)

        else:
            return TYPE.ERROR

    else:
        return TYPE.ERROR
