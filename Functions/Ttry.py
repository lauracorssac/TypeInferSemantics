from Definitions.types import TYPE

# Input example
# node = {
#    "description": "ttry",
#    "elements": {
#        "e1": {
#            "description": "traise"
#            "elements": {
#                "e1": "raise"
#            }
#        },
#        "e2": {
#            "description": "tbool"
#            "elements": {
#                "e1": "false"
#            }
#        }
#   }
# }
# Expected Output
# TYPE.BOOL

def term_is_valid(term):

    return term and "elements" in term and "e1" in term["elements"] and "e2" in term["elements"]

def t_try(environment, term):

    from main import infer_type

    if not term_is_valid(term):
        return TYPE.ERROR

    type_e1 = infer_type(environment, term["elements"]["e1"])
    type_e2 = infer_type(environment, term["elements"]["e2"])

    if type_e1 == type_e2:
        return type_e1

    if type_e1 == TYPE.UNDEFINED and type_e2 != TYPE.ERROR:
        return type_e2

    if type_e2 == TYPE.UNDEFINED and type_e1 != TYPE.ERROR:
        return type_e1

    return TYPE.ERROR
