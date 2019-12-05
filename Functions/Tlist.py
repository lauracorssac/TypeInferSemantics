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


def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" and "e2" in node["elements"]:
        return True
    else:
        return False

def t_list(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    # go from the inside out to find type, if consistent, put TYPE.LIST(...)
    # around and build it... check if everything is the same type... hard and
    # trick part (check cap. 22)
    # if list is empty type of list is...? TYPE.LIST(TYPE.EMPTY)?

    return TYPE.ERROR
