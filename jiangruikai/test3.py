L = ['Adam', 'Lisa', 'Bart', 'Paul']

print L[0:1]

for i in range(1, 101):
    if i % 7 == 0:
        print i

for index, name in enumerate(L):
    print index, '-', name

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v

for key, value in d.items():
     print key, ':', value

print [x * x for x in range(1, 11)]

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print [x * x for x in range(1, 11) if x % 2 == 0]
print [[m + n for m in 'ABC' for n in '123']]