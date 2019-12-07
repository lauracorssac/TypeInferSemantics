from Definitions.types import TYPE

# Input example:
#
# [1, 2]
#
# node = {
#     "description": "tlist",
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

def innerType(list):
    _, inner_type = list.split(".", 1)
    return inner_type

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
    head = node["elements"]["e1"]
    tail = node["elements"]["e2"]
    tail_type = infer_type(environment, tail)

    if isList(tail_type):
        head_type = infer_type(environment, head)
        empty = TYPE.LIST(TYPE.UNDEFINED)
        list_type = innerType(tail_type)

        if head_type == empty and tail_type == empty:
            return empty
        elif (head_type == list_type) or (head_type == TYPE.UNDEFINED):
            return tail_type
        elif head_type != empty and TYPE.UNDEFINED in list_type:
            return TYPE.LIST(head_type)

        else:
            return TYPE.ERROR

    else:
        return TYPE.ERROR
