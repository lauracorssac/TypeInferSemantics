from Definitions.types import TYPE

# Input example:

# node = {
#    "description": "traise"
#    "elements": {
#        "e1": "raise"
#    }
# }

# Expected Output
# TYPE.UNDEFINED

def terms_are_valid(term):
    return term and "elements" in term and "e1" in term["elements"]


def t_raise(environment, term):

    if not terms_are_valid(term):
        return TYPE.ERROR

    e1 = term["elements"]["e1"]
    if e1.lower() == "raise":
        return TYPE.UNDEFINED

    return TYPE.ERROR
