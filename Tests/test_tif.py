import sys
sys.path.insert(1, '../')

from Functions.Tif import *
from Definitions.types import TYPE

class TestTif:

    def test_tif_ok_numbers(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "tbool",
                      "elements":{
                          "e1": "true"
                      }
                   },
                  "e2": {
                      "description": "tint",
                      "elements":{
                          "e1": "40"
                      }
                   },
                  "e3": {
                      "description": "tint",
                      "elements":{
                          "e1": "70"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.INT

    def test_tif_ok_boolean(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "tbool",
                      "elements":{
                          "e1": "false"
                      }
                   },
                  "e2": {
                      "description": "tbool",
                      "elements":{
                          "e1": "true"
                      }
                   },
                  "e3": {
                      "description": "tbool",
                      "elements":{
                          "e1": "false"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.BOOL

    def test_tif_ok_fun(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "tbool",
                      "elements":{
                          "e1": "false"
                      }
                   },
                  "e2": {
                      "description": "tfun",
                      "elements":{
                          "e1": "x",
                          "e2": TYPE.INT,
                          "e3": {
                              "description": "tvar",
                              "elements": {
                                  "e1": "x"
                              }
                          }
                      }
                   },
                  "e3": {
                      "description": "tfun",
                      "elements":{
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
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.INT)

    def test_tif_ok_raise(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   },
                  "e2": {
                      "description": "tint",
                      "elements":{
                          "e1": "40"
                      }
                   },
                  "e3": {
                      "description": "tint",
                      "elements":{
                          "e1": "70"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.INT

    def test_tif_ok_raise_2_elements(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   },
                  "e2": {
                      "description": "tint",
                      "elements":{
                          "e1": "40"
                      }
                   },
                  "e3": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.INT

    def test_tif_ok_raise_3_elements(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   },
                  "e2": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   },
                  "e3": {
                      "description": "traise",
                      "elements":{
                          "e1": "raise"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.INT

    def test_tif_error_not_boolean(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "tint",
                      "elements":{
                          "e1": 30
                      }
                   },
                  "e2": {
                      "description": "tbool",
                      "elements":{
                          "e1": "true"
                      }
                   },
                  "e3": {
                      "description": "tbool",
                      "elements":{
                          "e1": "false"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.ERROR

    def test_tif_error_different_return(self):
        node = {
            "description": "tif",
            "elements": {
                  "e1": {
                      "description": "tbool",
                      "elements":{
                          "e1": "true"
                      }
                   },
                  "e2": {
                      "description": "tint",
                      "elements":{
                          "e1": "13"
                      }
                   },
                  "e3": {
                      "description": "tbool",
                      "elements":{
                          "e1": "false"
                      }
                   }
            }
        }
        environment = {}
        assert t_if(environment, node) == TYPE.ERROR

#    def test_tif_error_incorrect_description(self):
#        node = {
#            "description": "invalida",
#            "elements": {
#                  "e1": {
#                      "description": "tbool",
#                      "elements":{
#                          "e1": "true"
#                      }
#                   },
#                  "e2": {
#                      "description": "tbool",
#                      "elements":{
#                          "e1": "true"
#                      }
#                   },
#                  "e3": {
#                      "description": "tbool",
#                      "elements":{
#                          "e1": "false"
#                      }
#                   }
#            }
#        }
#        environment = {}
#        assert t_if(environment, node) == TYPE.ERROR