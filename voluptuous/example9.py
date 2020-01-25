from voluptuous import Schema, Invalid, All, Required


def passwords_must_match(passwords):
    if passwords['password'] != passwords['password_again']:
        raise Invalid('passwords must match')
    return passwords


s = Schema(All(
    # First "pass" for field types
    {Required('password'):str, Required('password_again'):str},
    # Follow up the first "pass" with your multi-field rules
    passwords_must_match
))

# valid
# s({'password':'123', 'password_again':'123'})

# raises MultipleInvalid: passwords must match
# s({'password':'123', 'password_again':'and now for something completely different'})

s({'password': '123'})
