import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from main import infer_type

param = {
    "description": "tvar",
    "elements": {
       "e1": "x"
    }
}
e1 = {
    "description": "tvar",
    "elements": { "e1": "x" }
}

e2 = {
    "description": "tapp",
    "elements": {
       "e1": {
           "description": "tvar",
           "elements": {
               "e1": "f"
           }
       },
       "e2": {
           "description": "tint",
           "elements": {
               "e1" : "4"
           }
       }
   }
}

node = {
    "description": "tletrec",
    "elements": {
        "function_name": "f",
         "type1": TYPE.INT,
         "type2": TYPE.INT,
         "param": param,
         "e1": e1,
         "e2": e2
    }
}

# Input: let rec f: INT -> INT = (fn x: INT => x) in f 4
# Output: INT
print(infer_type({}, node))
