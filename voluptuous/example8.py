from voluptuous import Any, Schema

schema = Schema(Any(None, int, str))

schema(None)

schema(5)
