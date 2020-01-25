from voluptuous import Schema, Required, All, Length, Range, Url, Invalid
from datetime import datetime


def Coerce(type, msg=None):
    """Coerce a value to a type.

    If the type constructor throws a ValueError, the value will be marked as
    Invalid.
    """
    def f(v):
        try:
            return type(v)
        except ValueError:
            raise Invalid(msg or ('expected %s' % type.__name__))
    return f


schema = Schema(Coerce(int))

result = schema('123')

print(result)
