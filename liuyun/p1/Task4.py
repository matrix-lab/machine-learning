import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) 

def get_numbers(records,list1,list2):
	for record in records:
		if record[0] not in list1:
				list1.append(record[0])
		elif record[1] not in list2:
				list2.append(record[1])

def is_promote(result,lists):
	for record in call_record:
		if record not in lists:
			if record not in result:
				result.append(record) 				

call_record = [];#主叫号码
called_record = [];#被叫号码
text_record = [];#短信号码
promote = [];#电话推销员

#提取出短信号码、电话号码
get_numbers(calls,call_record,called_record)
get_numbers(texts,text_record,text_record)

#判断是否是电话推销员
is_promote(promote,text_record)
is_promote(promote,called_record)


promote =  "\n".join(sorted(promote))

print("These numbers could be telemarketers:")
print(promote)
