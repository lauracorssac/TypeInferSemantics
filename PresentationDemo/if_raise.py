import sys
sys.path.insert(1, '../')

from Definitions.types import TYPE
from main import infer_type

node_if_son = {
    "description": "tif",
    "elements": {
          "e1": {
              "description": "tbool",
              "elements":{
                  "e1": "false"
              }
           },
          "e2": {
              "description": "traise",
              "elements": {
                  "e1": "raise"
              }
          },
          "e3": {
              "description": "traise",
              "elements": {
                  "e1": "raise"
              }
          }
    }
}

node_normal = {
    "description": "tint",
    "elements": {
        "e1": "5"
    }
}

node_clausula = {
    "description": "tbool",
    "elements": {
        "e1": "true"
    }
}

node_root = {
    "description": "tif",
    "elements": {
          "e1": {
              "description": "tbool",
              "elements": {
                  "e1": "true"
              }
          },
          "e2": node_if_son,
          "e3": {
              "description": "tint",
              "elements": {
                  "e1": "5"
              }
          }
    }
}

# print(infer_type({}, node_if_son))
print(infer_type({}, node_root))
