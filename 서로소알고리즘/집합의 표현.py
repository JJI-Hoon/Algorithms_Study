from collections import defaultdict

a = defaultdict(list)
a['1'] = [2]
print(a['1'])
if 0 in a['2']:
    print(1)