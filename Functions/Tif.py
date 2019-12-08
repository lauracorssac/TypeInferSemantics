from Definitions.types import TYPE

# Input example:
#
# if e1 then e2 else e3
#
# node = {
#   "description": "tif"
#   "elements": {
#        "e1": {
#            "description": "tbool",
#            "elements":{
#                "e1": "true"
#            }
#        },
#        "e2": {
#            "description": "tint",
#            "elements":{
#                "e1": "700"
#            }
#        },
#        "e3": {
#            "description": "tint",
#            "elements":{
#                "e1": "40"
#            }
#         }
#    }
#            
# }
#
# environment = {}
#
# Return:
#   TYPE.INT (no caso deste exemplo), na realidade o retorno é o tipo do elemento e1 ou e2
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

    if (tipo1 == TYPE.BOOL) or (tipo1 == TYPE.UNDEFINED):
        if(tipo2 == tipo3):            
            return tipo2
        elif (tipo2 == TYPE.UNDEFINED):
            return tipo3
        elif (tipo3 == TYPE.UNDEFINED):
            return tipo2
        else:
            return TYPE.ERROR
    else:        
        return TYPE.ERROR
