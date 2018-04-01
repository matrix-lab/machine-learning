def merge_lists(lists):
    return_list = list()
    if len(lists) > 0:
        for list_item in lists:
            return_list.append(list_item[0])
            return_list.append(list_item[1])
    return return_list

a = '95'
b = '91'
lists = ['3232323', '1523']
lists.sort()
print(lists)
print(max(lists))
if a > b:
    print('ok')