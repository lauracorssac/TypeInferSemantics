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
    new_type = infer_type(environment, new)
    list_type = infer_type(environment, list)
    if TYPE.LIST('') in list_type:
        _, type = list_type.split(".", 1)
        if type == new_type:
            return list_type
        else:
            return TYPE.ERROR
    else:
        return TYPE.ERROR
