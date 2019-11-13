from Definitions.types import TYPE

# Expected Node
# {
#   description: "qqr coisa",
#   elements: { "x" : nome_var, "T", "TYPE.INT", "e1": nodo_1, "e2" : nodo_2 }
# }

def t_let(environment, node):
    from main import infer_type
    if environment and node and "elements" in node:
        elements = node["elements"]

        if "x" in elements and "T" in elements and "e1" in elements and "e2" in elements:
            param = elements["x"]
            param_type = elements["T"]
            e1 = elements["e1"]
            e2 = elements["e2"]

            if infer_type(environment, e1) == param_type:
                environment[param] = param_type
                return infer_type(environment, e2)

    return TYPE.ERROR
