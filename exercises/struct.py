years_list = [1985, 1986, 1987, 1988, 1989]

# for year in years_list:
#     print(year)

print(years_list[3])

print(max(years_list))

things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].title()

print(things)

things[0] = things[0].upper()

print(things)

things.remove("salmonella")

print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()
surprise[2] = surprise[2][::-1]
surprise[2] = surprise[2].title()
print(surprise)

# e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
e2f_tuple = ['dog', 'chien'], ['cat', 'chat'], ['walrus', 'morse']
e2f = dict(e2f_tuple)
print(e2f)
print(e2f['walrus'])

f2e = {}
for key, value in e2f.items():
    f2e[value] = key

print(f2e['chien'])

print(set(e2f.keys()))


life = {
    'animals':
        {'cats': ['Henry', 'Grumpy', 'Lucy'],
         'octopi': {},
         'emus': {} },
    'plants': {},
    'other': {}
}

# print(life.keys())
(print(key) for key in list(life.keys()))
print(life['animals'])
print(life['animals']['cats'])