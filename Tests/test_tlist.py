import sys
sys.path.insert(1, '../')

from Functions.Tlist import *
from Definitions.types import TYPE

class TestTint:

    def test_tlist_int_ok(self):
        node = {
            "description": "tlist",
            "elements": {
                "e1" : {
                    "description": "tint",
                    "elements": {"e1": "1"}
                },
                "e2" : {
                    "description": "tlist",
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
        environment = {}
        assert t_list(environment, node) == TYPE.LIST(TYPE.INT)

    def test_tlist_empty_ok(self):
        node = {
            "description": "tlist",
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
        environment = {}
        assert t_list(environment, node) == TYPE.LIST(TYPE.UNDEFINED)

    def test_tlist_error(self):
        node = {
            "description": "tlist",
            "elements": {
                "e1" : {
                    "description": "tempty",
                    "elements": {"e1": "empty"}
                },
                "e2" : {
                    "description": "tlist",
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
        environment = {}
        assert t_list(environment, node) == TYPE.ERROR


    def test_tlist_error_2types(self):
        node = {
            "description": "tlist",
            "elements": {
                "e1" : {
                    "description": "tint",
                    "elements": {"e1": "1"}
                },
                "e2" : {
                    "description": "tlist",
                    "elements": {
                        "e1": {
                            "description": "tbool",
                            "elements": {"e1": "true"}
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
        assert t_list(environment, node) == TYPE.ERROR
