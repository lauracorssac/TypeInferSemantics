from Definitions.types import TYPE

#node
#{
# "description": "top"
# "elements: {
#    "e1" : "+",
#    "e2": {
#    "description": "tint",
#    "elements": "2"
#    },
#    "e3": {
#        "description": "tint",
#        "elements": "50"
#    }
# }
#
def t_op(environment, term):
    return TYPE.ERROR
