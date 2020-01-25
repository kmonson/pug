from voluptuous import Schema, Required, All, Length, Range, Url, Invalid
from datetime import datetime


def Date(fmt='%Y-%m-%d'):
    return lambda v: datetime.strptime(v, fmt)

schema = Schema(Date())

result = schema('2013-03-03')

print(result)
