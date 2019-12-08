import sys
sys.path.insert(1, '../')

from Functions.Thd import *
from Definitions.types import TYPE

class TestThd:

    def test_thd_bool_ok(self):
        node = {
            "description": "thd",
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
        assert t_hd(environment, node) == TYPE.BOOL

    def test_thd_int_ok(self):
        node = {
            "description": "thd",
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
        assert t_hd(environment, node) == TYPE.INT

    def test_thd_raiseint_ok(self):
        node = {
            "description": "thd",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "traise",
                            "elements": {"e1": "raise"}
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
        assert t_hd(environment, node) == TYPE.INT

    def test_thd_raiseint2_ok(self):
        node = {
            "description": "thd",
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
                                    "description": "traise",
                                    "elements": {"e1": "raise"}
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
        assert t_hd(environment, node) == TYPE.INT

    def test_thd_empty_ok(self):
        node = {
          "description": "thd",
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
        assert t_hd(environment, node) == TYPE.UNDEFINED


    def test_thd_error_2types(self):
        node = {
            "description": "thd",
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
        assert t_hd(environment, node) == TYPE.ERROR

    def test_thd_error_int(self):
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
        assert t_hd(environment, node) == TYPE.ERROR
