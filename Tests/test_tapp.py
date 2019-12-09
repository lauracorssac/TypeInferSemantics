import sys
sys.path.insert(1, '../')

from Functions.Tapp import *
from Definitions.types import TYPE

class TestTApp:

    def test_tapp_atomic_ok(self):
        node2 = {
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
        }

        node3 = {
            "description": "tint",
            "elements": {
                "e1": 5
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.BOOL

    def test_tapp_parameter_functional_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.FUNC(TYPE.INT, TYPE.INT),
                "e3": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                }
            }
        }

        node3 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": {
                    "description": "tint",
                    "elements": {
                        "e1": 5
                    }
                }
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.BOOL

    def test_tapp_output_functional_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.INT,
                "e3": {
                    "description": "tfun",
                    "elements": {
                        "e1": "x",
                        "e2": TYPE.BOOL,
                        "e3": {
                            "description": "tbool",
                            "elements": {
                                "e1": "true"
                            }
                        }
                    }
                }
            }
        }

        node3 = {
            "description": "tint",
            "elements": {
                "e1": 5
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.FUNC(TYPE.BOOL, TYPE.BOOL)

    def test_tapp_full_functional_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.FUNC(TYPE.BOOL, TYPE.INT),
                "e3": {
                    "description": "tfun",
                    "elements": {
                        "e1": "x",
                        "e2": TYPE.INT,
                        "e3": {
                            "description": "tint",
                            "elements": {
                                "e1": 5
                            }
                        }
                    }
                }
            }
        }

        node3 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.BOOL,
                "e3": {
                    "description": "tint",
                    "elements": {
                        "e1": 5
                    }
                }
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.FUNC(TYPE.INT, TYPE.INT)

    def test_tapp_chaotic_output_functional_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.FUNC(TYPE.BOOL, TYPE.INT),
                "e3": {
                    "description": "tfun",
                    "elements": {
                        "e1": "x",
                        "e2": TYPE.FUNC(TYPE.INT, TYPE.INT),
                        "e3": {
                            "description": "tfun",
                            "elements": {
                                "e1": "x",
                                "e2": TYPE.FUNC(TYPE.BOOL, TYPE.BOOL),
                                "e3": {
                                    "description": "tbool",
                                    "elements": {
                                        "e1": "true"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        node3 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.BOOL,
                "e3": {
                    "description": "tint",
                    "elements": {
                        "e1": 5
                    }
                }
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.FUNC(TYPE.FUNC(TYPE.INT, TYPE.INT),TYPE.FUNC(TYPE.FUNC(TYPE.BOOL, TYPE.BOOL),TYPE.BOOL))


    def test_tapp_chaotic_paramater_functional_ok(self):
        node2 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.FUNC(TYPE.FUNC(TYPE.BOOL, TYPE.INT), TYPE.FUNC(TYPE.FUNC(TYPE.INT, TYPE.INT), (TYPE.FUNC(TYPE.FUNC(TYPE.BOOL, TYPE.BOOL), TYPE.INT)))),
                "e3": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                }
            }
        }

        node3 = {
            "description": "tfun",
            "elements": {
                "e1": "x",
                "e2": TYPE.FUNC(TYPE.BOOL, TYPE.INT),
                "e3": {
                    "description": "tfun",
                    "elements": {
                        "e1": "x",
                        "e2": TYPE.FUNC(TYPE.INT, TYPE.INT),
                        "e3": {
                            "description": "tfun",
                            "elements": {
                                "e1": "x",
                                "e2": TYPE.FUNC(TYPE.BOOL, TYPE.BOOL),
                                "e3": {
                                    "description": "tint",
                                    "elements": {
                                        "e1": "5"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.BOOL


    def test_tapp_raise_paramater_ok(self):
        node2 = {
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
        }

        node3 = {
            "description": "traise",
            "elements": {
                "e1": "raise"
            }
        }

        node = {
            "description": "tapp",
            "elements": {
                "e1": node2,
                "e2": node3,
            }
        }
        environment = {}

        assert t_app(environment, node) == TYPE.BOOL
