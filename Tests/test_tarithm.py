import sys
sys.path.insert(1, '../')

from Functions.TopArithm import *
from Definitions.types import TYPE

class TestTArithm:

    def test_tarithm_ok_plus(self):
        node = {
            "description": "tarithm",
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
                "e3": "+"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT

    def test_tarithm_ok_minus(self):
        node = {
            "description": "tarithm",
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
                "e3": "-"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT

    def test_tarithm_ok_times(self):
        node = {
            "description": "tarithm",
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
                "e3": "*"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT

    def test_tarithm_ok_raise_e1(self):
        node = {
            "description": "tarithm",
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
                        "e1": "3"
                    }
                },
                "e3": "*"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT

    def test_tarithm_ok_raise_e2(self):
        node = {
            "description": "tarithm",
            "elements": {
                "e1": {
                    "description": "tint",
                    "elements": {
                        "e1": "5"
                    }
                },
                "e2": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e3": "-"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT

    def test_tarithm_ok_raise_e1_e2(self):
        node = {
            "description": "tarithm",
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
                "e3": "+"
            }    
        }        
        environment = {}
        assert t_arithm(environment, node) == TYPE.INT    

    def test_tarithm_error_type(self):
        node = {
            "description": "tarithm",
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
                "e3": "+"
            }    
        }
        environment = {}
        assert t_arithm(environment, node) == TYPE.ERROR

    def test_tarithm_error_operation(self):
        node = {
            "description": "tarithm",
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
        assert t_arithm(environment, node) == TYPE.ERROR