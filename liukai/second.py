f = open('countries.py')
file_content = f.read()
f.close()
# for i in file_content:
#     print("***{}***".format(i))
# print(file_content)

company = 'fangxin'
print("this is {}".format(company))

# files = []
# for i in range(100000):
#     files.append(open('countries.py'))
#     print(i)
#

# print(len(files))

a = open('countries.py','a')
# a.write('hello zz')
a.close()

