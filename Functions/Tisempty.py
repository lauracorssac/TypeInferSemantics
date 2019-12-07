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

    list = node["elements"]["e1"]
    list_type = infer_type(environment, list) # garantir que se lista não é possível,
                                 # retornar TYPE.ERROR e não LIST[TYPE.ERROR]
    # se a list é de fato do tipo lista, então retorna bool!
    # verificação de lista impede que e1 seja empty e e2 não seja
    # se for uma lista, e não for outro tipo, retorna bool!
    # se for qualquer outra coisa q não seja lista, retorna erro
    if TYPE.LIST('') in list_type:
        return TYPE.BOOL
    else:
        return TYPE.ERROR

    # if e1 and e2(false) are empty or e1(true) is not empty, returns bools
    # else returns error
    # check if type is correct? That is, if every element of the list shares
    # the same type or let this to 'tl'?
    # you have to check if is a list, them it's automatic to test, since tlist
    # does it... Check if return is list or anything else...

    return TYPE.ERROR
