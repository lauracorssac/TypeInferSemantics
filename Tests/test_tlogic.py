import sys
sys.path.insert(1, '../')

from Functions.TopLogic import *
from Definitions.types import TYPE

class TestTLogic:

    def test_tlogic_ok_greater(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "50"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "2"
                    }
                },
                "e3": ">"
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_less(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "700"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "400"
                    }
                },
                "e3": "<"
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_equal(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "5"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "3"
                    }
                },
                "e3": "=="
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_different(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "50"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "2"
                    }
                },
                "e3": "!="
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_greater_equal(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "5"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "3"
                    }
                },
                "e3": ">="
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_less_equal(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "5"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "3"
                    }
                },
                "e3": "=<"
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_raise_e1(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "2"
                    }
                },
                "e3": ">"
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_raise_e2(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "200"
                    }
                },
                "e2": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e3": "!="
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_ok_raise_e1_e2(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e2": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e3": "!="
            }    
        }        
        environment = {}
        assert t_logic(environment, node) == TYPE.BOOL

    def test_tlogic_error_type(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tbool",
                    "elements": {
                        "e1": "50"
                    }
                },
                "e2": {
                    "description": "tbool",
                    "elements": {
                        "e1": "false"
                    }
                },
                "e3": ">"
            }    
        }
        environment = {}
        assert t_logic(environment, node) == TYPE.ERROR

    def test_tlogic_error_operation(self):
        node = {
            "description": "tlogic",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "50"
                    }
                },
                "e2": {
                    "description": "tint",
                    "elements": {
                        "e1": "700"
                    }
                },
                "e3": "$"
            }    
        }
        environment = {}
        assert t_logic(environment, node) == TYPE.ERROR