# ideia de centralizar todas os tipos aqui.
# Para no retorno das funções ao invés de por exemplo "INT"
# colocar "TYPE.INT"

class TYPE():
    INT = "INT"
    BOOL = "BOOL"
    EMPTY = "EMPTY"
    ERROR = "ERROR"

    @staticmethod
    def FUNC(type_param, type_body):
        return "(" + type_param + ")" + " -> " + type_body

    @staticmethod
    def LIST(type_list):
        return "LIST[" + type_list + "]"
