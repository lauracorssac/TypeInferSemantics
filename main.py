from Functions import type_rules
from Definitions.types import TYPE
import collections
from Functions.Tfun import *
from Functions.Tvar import *

rules_dictionary = {
    'tfun': t_fun,
    'tvar': t_var
}

def infer_type(environment, node):
    type_rule = rules_dictionary[node['description']]
    return type_rule(environment, node)


if __name__ == "__main__":
    # infer_type({}, none)
    node = {
        "description": "tfun",
        "elements": {
            "e1": "x",
            "e2": TYPE.INT,
            "e3": {
                "description": "tvar",
                "elements": {
                    "e1": "x"
                }
            }
        }
    }
    print(infer_type({}, node))
