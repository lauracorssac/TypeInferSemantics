from Definitions.types import TYPE

#Input example:
#
# e1 > e2 / e1 < e2 / e1 == e2 / e1 =< e2 / e1 >= e2 
#
# node = {
#   "description": "tlogic"
#   "elements: {
#        "e1": {
#            "description": "tint",
#            "elements": {
#                "e1": "50"
#             }
#        },
#        "e2": {
#            "description": "tint",
#            "elements": {
#                "e1": "2"
#            }
#        },
#        "e3": ">"
#    }
# }
#
# environment = {}
#
# Return:
#   TYPE.BOOL
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"] and "e2" in node["elements"] and "e3" in node["elements"]:
        return True
    else:
        return False

def t_logic(environment, node):
    if not validParameters(environment, node):
      return TYPE.ERROR

    from main import infer_type

    elem1 = node["elements"]["e1"]
    elem2 = node["elements"]["e2"]

    tipo1 = infer_type(environment, elem1)
    tipo2 = infer_type(environment, elem2)

    if (((tipo1 == TYPE.INT) and (tipo2 == TYPE.INT)) 
    or ((tipo1 == TYPE.UNDEFINED) and (tipo2 == TYPE.INT)) 
    or ((tipo1 == TYPE.INT) and (tipo2 == TYPE.UNDEFINED)) 
    or ((tipo1 == TYPE.UNDEFINED) and (tipo2 == TYPE.UNDEFINED))):
      if ((node["elements"]["e3"] == ">") 
      or (node["elements"]["e3"] == "<") 
      or (node["elements"]["e3"] == "==") 
      or (node["elements"]["e3"] == "!=") 
      or (node["elements"]["e3"] == "=<") 
      or (node["elements"]["e3"] == ">=")):
        return TYPE.BOOL
      else:
        return TYPE.ERROR        
    else:
      return TYPE.ERROR
