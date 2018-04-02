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

def readable_timedelta(days):
    temp_days = round(days % 7)
    temp_weeks = int(days / 7)
    return str(temp_weeks) + ' week(s) and ' + str(temp_days) + ' day(s)'
    # return "{} week(s) and {} day(s)".format(temp_weeks, temp_days)