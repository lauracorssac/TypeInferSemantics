import sys
sys.path.insert(1, '../')

from Functions.Ttl import *
from Definitions.types import TYPE

class TestTtl:

    def test_ttl_bool_ok(self):
        node = {
            "description": "ttl",
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
        assert t_tl(environment, node) == TYPE.LIST(TYPE.BOOL)

    def test_ttl_int_ok(self):
        node = {
            "description": "ttl",
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
        assert t_tl(environment, node) == TYPE.LIST(TYPE.INT)

    def test_ttl_empty_ok(self):
        node = {
          "description": "ttl",
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
        assert t_tl(environment, node) == TYPE.LIST(TYPE.EMPTY)

    def test_ttl_single_ok(self):
        node = {
          "description": "ttl",
          "elements": {
               "e1": {
                   "description": "tcons",
                   "elements": {
                       "e1" : {
                           "description": "tint",
                           "elements": {"e1": "1"}
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
        assert t_tl(environment, node) == TYPE.LIST(TYPE.INT)


    def test_thd_error_2types(self):
        node = {
            "description": "ttl",
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
        assert t_tl(environment, node) == TYPE.ERROR

    def test_ttl_error_int(self):
        node = {
            "description": "thd",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": { "e1": "2"}
                }
            }
        }
        environment = {}
        assert t_tl(environment, node) == TYPE.ERROR
