import csv
with open('task/calls.csv','r') as f:
    reader = csv.reader(f)
    print(f.name)
    print(f.closed)
    # f.write('aaa')
    # calls = list(reader)
    # print(f.closed)

print(f.closed)