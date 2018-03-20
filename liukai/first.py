python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[0])
print(python_versions[-1])

def how_many_days(mounth_num):
    days_in_mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_mounth[mounth_num]

print(how_many_days(2))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[3:6])
print(months[3:])
print(months[:3])
print(months[-3:])

sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
print(sample_list[3])
print(sample_string[2])
print(len(sample_string))
print(len(sample_list))

batch_sizes = [6, 15, 34, 35, 65, 89, 8]
print(sorted(batch_sizes))

nautical_directions = "**".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python', 'Blood Python']
python_varieties.append('Blood Python3')
print(python_varieties)

def top_three(num):
    num.sort()
    return num[-3:]

print(top_three([6, 15, 34, 35, 65, 89, 8]))

# 中位数
def median(num_list):
    num_list.sort()
    if len(num_list) % 2:
        mid_index = int(len(num_list) / 2)
        return num_list[mid_index]
    else:
        right_num = int(len(num_list) // 2)
        left_num = right_num - 1
        return (num_list[left_num] + num_list[right_num]) / 2



print(median([1,2,3]))
print(median([1,2,3,4]))


names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
for name in names:
    print(name.title())


company = 'fangxin'
print(company.title())

def list_sum(lists):
    sum = 0
    for num in lists:
        sum += num

    return sum
print(list_sum([2,9,4]))