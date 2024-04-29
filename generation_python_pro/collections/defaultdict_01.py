from collections import defaultdict

data = defaultdict(list)
print(data['key'])

data.default_factory = dict
print(data['key'])

data.default_factory = tuple
print(data['key'])
