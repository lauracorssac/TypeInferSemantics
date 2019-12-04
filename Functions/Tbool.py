from Definitions.types import TYPE

# Input example:
#
# node = {
#   "description": "tbool"
#   "elements": {
#        "e1": "true"
#   }
# }
#
# environment = {}
#
# Return:
#    TYPE.BOOL
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_bool(environment, term):

    word = node['elements']['e1'].lower()

    if (word == "true") or (word == "false")
        return TYPE.BOOL
    else:
        return TYPE.ERROR
