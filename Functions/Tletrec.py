from Definitions.types import TYPE

def t_letrec(environment, term):
    from main import infer_type
    infer_type(environment, term)

    return TYPE.ERROR
