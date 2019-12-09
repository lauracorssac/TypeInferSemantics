import sys
sys.path.insert(1, '../')

from Functions.Tcons import *
from Definitions.types import TYPE

class TestTcons:

    def test_tcons_nested1_ok(self):
        node = {
            "description": "tcons",
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
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                },
                "e2": {
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
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_nested2_ok(self):
        node = {
            "description": "tcons",
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
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_nested_raise_ok(self):
        node = {
            "description": "tcons",
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
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.UNDEFINED))

    def test_tcons_nested_raise2_ok(self):
        node = {
            "description": "tcons",
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
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.UNDEFINED))

    def test_tcons_nested_raise3_ok(self):
        node = {
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
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.UNDEFINED)

    def test_tcons_nested_empty_ok(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tempty",
                            "elements": {"e1": "empty"}
                        },
                        "e2" : {
                            "description": "tcons",
                            "elements": {
                                "e1": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.EMPTY)

    def test_tcons_nested_raiseint_ok(self):
        node = {
            "description": "tcons",
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
                                    "elements": {"e1": "1"}
                                },
                                "e2": {
                                    "description": "tempty",
                                    "elements": {"e1": "empty"}
                                }
                            }
                        }
                    }
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_nested_raiseint2_ok(self):
        node = {
            "description": "tcons",
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
                },
                "e2": {
                    "description": "tempty",
                    "elements": {"e1" : "empty"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_nested_raiseint3_ok(self):
        node = {
            "description": "tcons",
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
                            "elements": { "e1": "empty"}
                        }
                    }
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tcons",
                            "elements": {
                                "e1" : {
                                    "description": "traise",
                                    "elements": {"e1": "raise"}
                                },
                                "e2" : {
                                    "description": "tempty",
                                    "elements": { "e1": "empty"}
                                }
                            }
                        },
                        "e2" : {
                            "description": "tempty",
                            "elements": { "e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_nested_raiseint4_ok(self):
        node = {
            "description": "tcons",
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
                            "elements": { "e1": "empty"}
                        }
                    }
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "traise",
                            "elements": { "e1": "raise"}
                        },
                        "e2" : {
                            "description": "tempty",
                            "elements": { "e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.INT))

    def test_tcons_int_ok(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {"e1": "1"}
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tint",
                            "elements": {"e1": "2"}
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
        assert t_cons(environment, node) == TYPE.LIST(TYPE.INT)

    def test_tcons_nested_bools_ok(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tbool",
                            "elements": {"e1": "true"}
                        },
                        "e2" : {
                            "description": "tempty",
                            "elements": { "e1": "empty"}
                        }
                    }
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tcons",
                            "elements": {
                                "e1" : {
                                    "description": "tbool",
                                    "elements": {"e1": "false"}
                                },
                                "e2" : {
                                    "description": "tempty",
                                    "elements": { "e1": "empty"}
                                }
                            }
                        },
                        "e2" : {
                            "description": "tempty",
                            "elements": { "e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.LIST(TYPE.BOOL))

    def test_tcons_fun_ok(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tfun",
                    "elements": {
                        "e1": "x",
                        "e2": TYPE.INT,
                        "e3": {
                            "description": "tbool",
                            "elements": {
                                "e1": "true"
                            }
                        }
                    }
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1": {
                            "description": "tfun",
                            "elements": {
                                "e1": "x",
                                "e2": TYPE.INT,
                                "e3": {
                                    "description": "tbool",
                                    "elements": {
                                        "e1": "false"
                                    }
                                }
                            }
                        },
                        "e2": {
                            "description": "tempty",
                            "elements": {"e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.LIST(TYPE.FUNC(TYPE.INT, TYPE.BOOL))

    def test_tcons_error_2types_nested(self):
        node = {
            "description": "tcons",
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
                            "elements": { "e1": "empty"}
                        }
                    }
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tcons",
                            "elements": {
                                "e1" : {
                                    "description": "tbool",
                                    "elements": {"e1": "false"}
                                },
                                "e2" : {
                                    "description": "tempty",
                                    "elements": { "e1": "empty"}
                                }
                            }
                        },
                        "e2" : {
                            "description": "tempty",
                            "elements": { "e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.ERROR

    def test_tcons_error_2types(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {"e1": "1"}
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tbool",
                            "elements": {"e1": "true"}
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
        assert t_cons(environment, node) == TYPE.ERROR


    def test_tcons_error_empty_first(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tempty",
                    "elements": {"e1": "empty"}
                },
                "e2": {
                    "description": "tcons",
                    "elements": {
                        "e1" : {
                            "description": "tbool",
                            "elements": {"e1": "true"}
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
        assert t_cons(environment, node) == TYPE.ERROR

    def test_tcons_error_e2_not_list(self):
        node = {
            "description": "tcons",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {"e1": "1"}
                },
                "e2": {
                    "description": "tint",
                    "elements": {"e1" : "2"}
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.ERROR
