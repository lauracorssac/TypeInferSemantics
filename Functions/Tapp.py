from Definitions.types import TYPE

# node2 = {
#     "description": "tfun",
#     "elements": {
#         "e1": "x",
#         "e2": TYPE.INT,
#         "e3": {
#             "description": "tbool",
#             "elements": {
#                 "e1": "true"
#             }
#         }
#     }
# }
#
# node3 = {
#     "description": "tint",
#     "elements": {
#         "e1": 5
#     }
# }
#
# node = {
#     "description": "tapp",
#     "elements": {
#         "e1": node2,
#         "e2": node3,
#     }
# }
# environment = {}
# Return:
#   TYPE.BOOL
#

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"] and "e2" in node["elements"]:
        return True
    else:
        return False

def get_expected_parameter(term):
    lastIndex = 0
    pilha = []
    for count,element in enumerate(term):
        if (element == '('):
            pilha.append(element)
        if(element == ')'):
            if (pilha[-1] == '('):
                pilha.pop()
                lastIndex = count
                if(len(pilha) ==0):
                    break
            else:
                raise Exception()

    expected_parameter = term[1:lastIndex]
    return expected_parameter, lastIndex

def apply_parameter(term, lastIndex):
    result = term[lastIndex+3:] # the index indicates the closing ), so we have to remove the remaining ')->'
    return result

def t_app(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    from main import infer_type

    term = infer_type(environment, node["elements"]["e1"])
    if term == TYPE.UNDEFINED:
        return TYPE.ERROR

    expected_parameter, ending_index = get_expected_parameter(term)
    received_parameter = infer_type(environment, node["elements"]["e2"])

    if expected_parameter == received_parameter or received_parameter == TYPE.UNDEFINED:
        result = apply_parameter(term, ending_index)
        return result
    else:
        return TYPE.ERROR
