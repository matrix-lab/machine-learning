# 列表索引
python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[-1])

# 列表切片
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[6:9])
print(months[:5])
print(months[5:])

# len   max   min   sorted
arr = [5, 8, 6, 2.2, 3]
print(len(arr))
print(max(arr))
print(min(arr))
print(sorted(arr))

# join 连接列表
names = ["García", "Kelly", "Davis"]
print('-'.join(names))

# 追加到列表 append
names.append('Jack')
print(names)

def top_three(arr):
    new_arr = sorted(arr, reverse=True)
    return new_arr[:3]
print(top_three([8, 9, 1, 12, 6, 8, 6, 21]))

# 求中位数
def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        right_of_middle = len(numbers)//2
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2
print(median([8, 5, 9, 12, 6]))
print(median([8, 9, 12, 6]))

#    for 循环
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']
capitalized_names = []
for name in names:
    capitalized_names.append(name.title())

# range()
# 覆盖names，转换为大写
for index in range(len(names)):
    names[index] = names[index].title()
print(names)
print(capitalized_names)

def html_list(lists):
    htmls = ['<ul>']
    for item in lists:
        htmls.append('<li>'+item+'</li>')
    htmls.append('</ul>')
    return '\n'.join(htmls)
print(html_list(['first string', 'second string', 'third string']))

def starbox(width, height):
    print('*' * width)
    for _ in range(height - 2):
        print('*' + ' ' * (width - 2) + '*')
    print('*' * width)
print("Test 1:")
starbox(5, 5)

print("Test 2:")
starbox(2, 3)

#    while 循环
card_deck = [4, 11, 8, 5, 13, 2, 8, 3]
hand = []
while sum(hand) <= 17:      # sum 用于计算列表中元素的总和
    hand.append(card_deck.pop())    # pop 从列表中移除一个元素并返回它, 与append相反
print(hand)

def nearest_square(limit):
    num = 1
    while num**2 <= limit:
        num += 1
    return (num - 1)**2
print(nearest_square(40))

# break
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []
for cargo in manifest:
    if cargo_weight + cargo[1] >= 100:
        break
    else:
        cargo_weight += cargo[1]
        cargo_hold.append(cargo[0])
print(cargo_weight)
print(cargo_hold)

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""
for headline in headlines:
    if len(news_ticker) + len(headline) > 140:
        news_ticker += headline[:(140 - len(news_ticker))]
        if len(news_ticker) == 140:
            break
    news_ticker += (headline + ' ')
print(news_ticker)

# 删除重复数据
target = []
source = ['one', 'two', 'three', 'four', 'two', 'five', 'three']
for element in source:
    if element not in target:
        target.append(element)
print(target)
source_set = set(source)
print(len(source_set))
source_set.add('six')
print(source_set)

squares = set()
def nearest(limit):
    answer = 0
    while (answer+1)**2 < limit:
        squares.add(answer**2)
        answer += 1
    print(squares)
print(nearest(2000))

obj1 = {
    'name': 'Jake',
    'age': 26,
    'address': 'jusfksdfkdsfjkf 201'
}
if 'title' in obj1:
    print('real!')
else:
    print('wrong!')
print(obj1.get('name', 'There\'s no such element!'))
print(obj1.get('title', 'There\'s no such element!'))   # 当未找到键时，指定返回一个默认值

print(obj1.get('name'))

Beatles_Discography = {
    "Please Please Me": 1963,
    "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970
}

def most_prolific(list):
    list_count = {}
    for name in list:
        year = list[name]
        list_count[year] = list_count.get(year, 0) + 1
    print(list_count)
print(most_prolific(Beatles_Discography))



















