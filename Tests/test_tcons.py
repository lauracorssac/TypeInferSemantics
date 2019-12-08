import sys
sys.path.insert(1, '../')

from Functions.Tcons import *
from Definitions.types import TYPE

class TestTint:

    def test_tcons_nested_ok(self):
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

    def test_tcons_nested_error(self):
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
                    "elements": {
                        "e1" : {
                            "description": "tempty",
                            "elements": {"e1": "empty"}
                        }
                    }
                }
            }
        }
        environment = {}
        assert t_cons(environment, node) == TYPE.ERROR

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
