from Definitions.types import TYPE

# Input example:
#
# cons 1 (cons 2 empty)
#
# node = {
#     "description": "tcons",
#     "elements": {
#         "e1" : {
#             "description": "tint",
#             "elements": {"e1": "1"}
#         },
#         "e2" : {
#             "description": "tcons",
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

def t_cons(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    new = node["elements"]["e1"]
    list = node["elements"]["e2"]
    list_type = infer_type(environment, list)

    if isList(list_type):
        new_type = infer_type(environment, new)
        empty = TYPE.LIST(TYPE.EMPTY)
        list_of = innerType(list_type)
        
        if new_type == empty and list_type == empty:
            return empty
        if new_type != empty and TYPE.EMPTY in list_type:
            return TYPE.LIST(new_type)
        elif (new_type == list_of) or (new_type == TYPE.UNDEFINED):
            return list_type
        elif new_type != empty and TYPE.UNDEFINED in list_type:
            return TYPE.LIST(new_type)

        else:
            return TYPE.ERROR

    else:
        return TYPE.ERROR
