from Definitions.types import TYPE

# let rec f : T1 → T2 = (fn x:T1 ⇒ e1) in e2
# let rec f: INT -> INT = (fn x: INT => 2) in 4
#{
#    "description": "tletrec",
#    "elements": {
#       "function_name": "f",
#       "type1": TYPE.INT,
#       "type2": TYPE.INT,
#       "param": {
#           "description": "tvar",
#           "elements": {
#               "e1": "x"
#           }
#       },
#       "e1": {
#           "description": "tint",
#           "elements": {
#               "e1": "2"
#           }
#       },
#       "e2": {
#           "description": "tint",
#           "elements": {
#               "e1": "4"
#           }
#       },
#    }
#}

# Output: INT

def parameters_are_valid(environment, term):
    return ( term and
    'elements' in term and
    'function_name' in term['elements'] and
    'type1' in term['elements'] and
    'type2' in term['elements'] and
    'param' in term['elements'] and
    'e1' in term['elements'] and
    'e2' in term['elements'] and
    'elements' in term['elements']['param'] and
    'e1' in term['elements']['param']['elements'])

def t_letrec(environment, term):
    from main import infer_type

    if not parameters_are_valid(environment, term):
        return TYPE.ERROR

    if not environment:
        environment = {}

    function_name = term['elements']['function_name']
    input_type = term['elements']['type1']
    output_type = term['elements']['type2']
    param_name = term['elements']['param']['elements']['e1']
    e1 = term['elements']['e1']
    e2 = term['elements']['e2']

    environment[function_name] = TYPE.FUNC(input_type, output_type)
    type_e2 = infer_type(environment, e2)

    environment[param_name] = input_type
    type_e1 = infer_type(environment, e1)

    if type_e2 == TYPE.ERROR or type_e1 == TYPE.ERROR:
        return TYPE.ERROR

    if type_e1 == output_type or type_e1 == TYPE.UNDEFINED:
        return type_e2

    return TYPE.ERROR
