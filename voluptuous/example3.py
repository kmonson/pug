from voluptuous import Schema, Required, All, Length, Range, Url

schema = Schema(set)

result = schema({21})

print(result)
