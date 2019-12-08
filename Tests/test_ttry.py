import sys
sys.path.insert(1, '../')

from Functions.Ttry import t_try as t_try
from Definitions.types import TYPE as TYPE

class TestTTry:

    # try raise with x
    def test_t_try0(self):
        node = {
            "description": "ttry",
            "elements": {
                "e1": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                },
                "e2": {
                    "description": "tvar",
                    "elements": {
                        "e1": "x"
                    }
                }
            }
        }

        assert t_try({"x": TYPE.BOOL}, node) == TYPE.BOOL

    # try true with raise
    def test_t_try1(self):
        node = {
            "description": "ttry",
            "elements": {
                "e1": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                },
                "e2": {
                    "description": "traise",
                    "elements": {
                        "e1": "raise"
                    }
                }
            }
        }

        assert t_try({"x": TYPE.BOOL}, node) == TYPE.BOOL

    # try raise with raise
    def test_t_try2(self):
        node = {
            "description": "ttry",
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
                }
            }
        }

        assert t_try({}, node) == TYPE.UNDEFINED

    # try x with true
    def test_t_try3(self):
        node = {
            "description": "ttry",
            "elements": {
                "e1": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                },
                "e2": {
                    "description": "tvar",
                    "elements": {
                        "e1": "x"
                    }
                }
            }
        }

        assert t_try({"x": TYPE.BOOL}, node) == TYPE.BOOL

    # try x with true
    # x not valid
    def test_t_try4(self):
        node = {
            "description": "ttry",
            "elements": {
                "e1": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                },
                "e2": {
                    "description": "tvar",
                    "elements": {
                        "e1": "x"
                    }
                }
            }
        }

        assert t_try({}, node) == TYPE.ERROR

    # try true with blaa
    # blaa not valid
    def test_t_try5(self):
        node = {
            "description": "ttry",
            "elements": {
                "e1": {
                    "description": "tbool",
                    "elements": {
                        "e1": "true"
                    }
                },
                "e2": {
                    "description": "traise",
                    "elements": {
                        "e1": "blaa"
                    }
                }
            }
        }

        assert t_try({}, node) == TYPE.ERROR
