from Functions import type_rules
from Definitions.types import TYPE
import collections
from Functions.Tfun import *
from Functions.Tvar import *
from Functions.Tlet import *
from Functions.Tint import *
from Functions.Tbool import *

rules_dictionary = {
    'tfun': t_fun,
    'tvar': t_var,
    'tlet': t_let,
    'tint': t_int,
    'tbool': t_bool
}

def infer_type(environment, node):
    type_rule = rules_dictionary[node['description']]
    return type_rule(environment, node)


if __name__ == "__main__":
    infer_type({}, none)
