
"""
whihe循环 练习.
pop 从列表最后移出一个元素；append 把一个元素从开始位置放到列表中
"""
card_deck = [4,11,8,5,13,2,8,10]
hand = []

while sum(hand) <= 21:
	hand.append(card_deck.pop())
	
print(hand)



def nearest_square(limit):
	"""
		获取小于参数的最大立方数
	"""
	num = 1
	while num**3 <= limit:
		num += 1
	return (num - 1)**3
	
print(nearest_square(128))


"""
break 的使用
"""
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []
for cargo in manifest:
	if	cargo_weight + cargo[1] >= 100:
		break
	else:
		cargo_hold.append(cargo[0])
		cargo_weight += cargo[1]
print(cargo_weight)


"""
集合 练习,
"""
def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target

print(remove_duplicates(['one','one','three','four','two','five','three']
))


def nearest_square_new(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
    
squares = set()

start = 2000
while True:
    square_number = nearest_square_new(start)
    
    if square_number == 0:
        break
    
    squares.add(square_number)
    start = square_number
    
print(squares)