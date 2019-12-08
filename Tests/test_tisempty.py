import sys
sys.path.insert(1, '../')

from Functions.Tisempty import *
from Definitions.types import TYPE

class TestTisempty:

    def test_tisempty_bool_ok(self):
        node = {
            "description": "tisempty",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tbool",
                            "elements": {"e1": "true"}
                        },
                        "e2" : {
                            "description": "tcons",
                            "elements": {
                                "e1": {
                                    "description": "tbool",
                                    "elements": {"e1": "false"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_isempty(environment, node) == TYPE.BOOL

    def test_tisempty_int_ok(self):
        node = {
            "description": "tisempty",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tint",
                            "elements": {"e1": "1"}
                        },
                        "e2" : {
                            "description": "tcons",
                            "elements": {
                                "e1": {
                                    "description": "tint",
                                    "elements": {"e1": "2"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_isempty(environment, node) == TYPE.BOOL

    def test_tisempty_empty_ok(self):
        node = {
          "description": "tisempty",
          "elements": {
               "e1": {
                   "description": "tcons",
                   "elements": {
                       "e1" : {
                           "description": "tempty",
                           "elements": {"e1": "empty"}
                       },
                       "e2" : {
                           "description": "tempty",
                           "elements": {"e1": "empty"}
                       }
                   }
               }
            }
        }
        environment = {}
        assert t_isempty(environment, node) == TYPE.BOOL

    def test_tisempty_error_2types(self):
        node = {
            "description": "tisempty",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tbool",
                            "elements": {"e1": "true"}
                        },
                        "e2" : {
                            "description": "tcons",
                            "elements": {
                                "e1": {
                                    "description": "tint",
                                    "elements": {"e1": "2"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_isempty(environment, node) == TYPE.ERROR
