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

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_tl(environment, term):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    
    return TYPE.ERROR
