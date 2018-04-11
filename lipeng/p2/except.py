import keyword

print(keyword.kwlist)


try:
    x = int(input('Enter a number:'))
except:
    print('That\'s not a valid number')