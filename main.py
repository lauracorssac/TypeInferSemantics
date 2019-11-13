from Functions import type_rules
from Definitions.types import TYPE
import collections
from Functions.Tletrec import *

def infer_type(node, environment):
    return TYPE.ERROR


if __name__ == "__main__":
    infer_type(None,{})
