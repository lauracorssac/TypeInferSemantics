from Definitions.types import TYPE

# Input example:
#
# isempty [1, 2]
#
# node = {
#   "description": "thd"
#   "elements": {
#        "e1": {
#            "description": "tlist",
#            "elements": {
#                 "e1" : {
#                       "description": "tint",
#                       "elements": {"e1": "1"}
#                 },
#                 "e2": {
#                      "description": "tlist",
#                      "elements": {
#                           "e1": {
#                                "description": "tint",
#                                "elements": {"e1": "2"}
#                           },
#                           "e2": {
#                                "description": "tempty",
#                                "elements": {"e1": "empty"}
#                           }
#                      }
#                 }
#             }
#         }
#   }
#
# environment = {}
#
# Return:
#   TYPE.LIST(TYPE.INT)

def isList(expression):
    if TYPE.LIST('') in expression:
        return True
    else:
        return False

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_tl(environment, term):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    list = node["elements"]["e1"]
    list_type = infer_type(environment, list)
    if isList(list_type): # e2(tail) is validated in the infer_type of the list
        return list_type # if tail is empty, it returns the type of the list!

    else:
        return TYPE.ERROR
