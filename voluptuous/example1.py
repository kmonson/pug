from voluptuous import Schema, Required, Optional, All, Length, Range, ALLOW_EXTRA, REMOVE_EXTRA

schema = Schema({'q': All(str, Length(min=1)),
                 Required('per_page', default=5): All(int, Range(min=1, max=20)),
                 Optional('page'): All(int, Range(min=0))}, extra=REMOVE_EXTRA, required=True)

result = schema({'q': "foo", 'per_page': 10, "foo": 42})

print(result)
