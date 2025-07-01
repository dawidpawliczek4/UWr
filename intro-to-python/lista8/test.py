

e = {'a': 2, 'b': 2, 'c': 1}

maxval = max(e.values())

maxkeys = [ key for key, value in e.items() if value == maxval]

print(maxkeys)