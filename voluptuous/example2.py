from voluptuous import Schema, Required, All, Length, Range, Url

schema = Schema(Url())

result = schema('w3.org')

print(result)
