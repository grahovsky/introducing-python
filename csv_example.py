import csv


villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
    ]

with open('villains.csv', 'wt', newline='') as fout:  # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains.csv', 'rt') as fin:  # context manager
    cin = csv.reader(fin)
    villains = [row for row in cin]  # a list comprehension

print(villains)

# DictReader()
with open('villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

# DictWriter()
with open('villains.csv', 'wt', newline='') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# By omitting the fieldnames argument in the DictReader() call
with open('villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)
