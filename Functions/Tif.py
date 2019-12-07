from Definitions.types import TYPE

# Input example:
#
# if e1 then e2 else e3
#
# node = {
#   "description": "tif"
#   "elements": {
#        "e1": "TYPE.BOOL",
#        "e2": TYPE,
#        "e3": TYPE
#    }
#            
# }
#
# environment = {}
#
# Return:
#   TYPE
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"] and "e2" in node["elements"] and "e3" in node["elements"]:
        return True
    else:
        return False

def t_if(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type 

    elem1 = node["elements"]["e1"]
    elem2 = node["elements"]["e2"]
    elem3 = node["elements"]["e3"]

    tipo1 = infer_type(environment, elem1)
    tipo2 = infer_type(environment, elem2)
    tipo3 = infer_type(environment, elem3)

    if (tipo1 == TYPE.BOOL):
        if(tipo2 == tipo3):            
            return tipo2
        else:
            return TYPE.ERROR
    else:        
        return TYPE.ERROR
