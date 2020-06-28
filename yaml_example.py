import yaml

with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()

# print(text)

data = yaml.safe_load(text)
print(data['details'])

print(data['poems'])