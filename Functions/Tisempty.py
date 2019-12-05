from Definitions.types import TYPE

# Input example:
#
# isempty [1, 2]
#
# node = {
#   "description": "tisempty"
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
#   TYPE.BOOL
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_isempty(environment, term):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type

    # if e1 and e2(false) are empty or e1(true) is not empty, returns bools
    # else returns error
    # check if type is correct? That is, if every element of the list shares
    # the same type or let this to 'tl'?

    return TYPE.ERROR
