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
#   TYPE.INT

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_hd(environment, term):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
    list = node["elements"]["e1"]
    list_type = infer_type(environment, list)
    if TYPE.LIST('') in list_type:
        _, type = list_type.split(".", 1)
        return type

    else:
        return TYPE.ERROR
