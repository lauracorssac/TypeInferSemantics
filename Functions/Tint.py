from Definitions.types import TYPE

# Input example:
#
# node = {
#   "description": "tint"
#   "elements": {
#        "e1": "7"
#   }
# }
#
# environment = {}
#
# Return:
#    TYPE.INT
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"]:
        return True
    else:
        return False

def t_int(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type
 
    try:
        value = int(node['elements']['e1'])
 
    except ValueError:
        value = TYPE.ERROR    

    if type(value) == int:
        return TYPE.INT
    else:
        return TYPE.ERROR

