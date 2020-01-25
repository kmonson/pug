from voluptuous import Schema

person = Schema({'name': str})

person_with_age = person.extend({'age': int})


sorted(list(person_with_age.schema.keys()))
['age', 'name']

