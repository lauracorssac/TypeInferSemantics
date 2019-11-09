from Definitions.types import TYPE

def t_letrec(environment, term):
    from mainFunction import main_function
    main_function(environment, term)

    return TYPE.ERROR
