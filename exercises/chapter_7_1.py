import unicodedata

mystery = '\U0001f4a9'

print(mystery)

name = unicodedata.name(mystery)
print(name)

pop_bytes = mystery.encode('utf-8')
print(type(pop_bytes))
print(pop_bytes)

pop_string = pop_bytes.decode('utf-8')
print(pop_string)

poem = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
""" % ('roast beef', 'ham', 'head', 'clam')
print(poem)

letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""

response = {
    'salutation': 'Colonel',
    'name': 'Hackenbush',
    'product': 'duck blind',
    'verbed': 'imploded',
    'room': 'conservatory',
    'animals': 'emus',
    'amount': '$1.38',
    'percent': '1',
    'spokesman': 'Edgar Schmeltz',
    'job_title': 'Lecensed Podiatrist'
}

print(letter.format(**response))