import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

lists = {};  

def get_datas(recordes):	
	for recorde in recordes:
		i = 0		
		while i<2:			
			lists[recorde[i]] = lists.get(recorde[i],0)+int(recorde[3])
			i=i+1			 

get_datas(calls)

print(lists)
