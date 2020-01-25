from voluptuous import Schema, Self
recursive = Schema({"more": Self, "value": int})
recursive({"more": {"value": 42}, "value": 41})
