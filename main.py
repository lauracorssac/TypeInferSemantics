from Functions import type_rules
from Definitions.types import TYPE
import collections
from Functions.Tletrec import *

def infer_type(node, environment):
    return TYPE.ERROR

infer_type("", "")
