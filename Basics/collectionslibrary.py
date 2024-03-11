from collections import Counter, defaultdict, OrderedDict

lst = [1,2,2,3,4,4,4,5]
print(Counter(lst))
print('-'*30)

d = defaultdict(int)
d['a'] += 2
print(d)

d = OrderedDict()
d['1'] = 'One'
d['2'] = 'Two'
print(d)

