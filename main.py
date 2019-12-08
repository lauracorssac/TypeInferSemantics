from Functions import type_rules
from Definitions.types import TYPE
import collections
from Functions.Tfun import *
from Functions.Tvar import *
from Functions.Tlet import *
from Functions.Tint import *
from Functions.Tbool import *
from Functions.Tapp import *
from Functions.Tempty import *
from Functions.Thd import *
from Functions.Tcons import *
from Functions.Ttl import *
from Functions.Tisempty import *
from Functions.TopArithm import *
from Functions.TopLogic import *
from Functions.Tif import *

rules_dictionary = {
    'tfun': t_fun,
    'tvar': t_var,
    'tlet': t_let,
    'tint': t_int,
    'tbool': t_bool,
    'tapp': t_app,
    'tempty': t_empty,
    'thd': t_hd,
    'tcons': t_cons,
    'ttl': t_tl,
    'tisempty': t_isempty,
    'tarithm': t_arithm,
    'tlogic': t_logic,
    'tif': t_if
}

def infer_type(environment, node):
    type_rule = rules_dictionary[node['description']]
    return type_rule(environment, node)

if __name__ == "__main__":
    infer_type({}, none)
