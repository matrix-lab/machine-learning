import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print("First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]))
