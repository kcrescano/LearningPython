import operator

catalog = {'a': 1, 'd': 2, 'c': 3, 'b': 4}
catalog_ = dict(sorted(catalog.items(), key=operator.itemgetter(0)))

print(catalog_)
