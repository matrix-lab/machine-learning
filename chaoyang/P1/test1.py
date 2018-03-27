#-*- coding: UTF-8 -*-
#print ('你好，晁阳')

#SyntaxError: unexpected EOF while parsing
#print(17*16) - (5*7) -(9*7) 

#print((17*16)-(5*7 + 9*7))


#print(11.1e2)
#1110

#print(len('abc))
#3

#print(type("ac"))
#<class 'str'>

#print(type("abc"*2))
#<class 'str'>

#print(int('123'))
#123

#"abc".islower()
#true

#12.islower()
#发生错误

#print('chaoyang'.count('a'))
#2


#user_ip = '127.0.0.1'
#url='www.baidu.com'
#from datetime import datetime
#print( "IP address {} accessed {} at {}".format(user_ip, url, datetime.now()))
#IP address 127.0.0.1 accessed www.baidu.com at 2018-03-15 23:25:07.477517

#dimensions = 50,60,70
#length,width,height = dimensions
#print("The dimensions are {}*{}*{}".format(length,width,height))


#def check_num(num):
	#if num%3==0:
		#print("11111")
	#elif num%3==1:
		#print('2222')
	#else:
		#print('3333')

#check_num(4)

#def check_num(a,b,c):
	#if a==1 and (b>1 or c>a):
		#print('111')
	#elif a==1 and (not c):
		#print('2222')
	#else:
		#print('3333')

#check_num(1,0,0)


#def cylinder_surface_area(radius, height,has_top_and_bottom = False):
	#if has_top_and_bottom:
		#空心
		#return  2* 3.14 * float(radius) * float(height)
	#else:
		#return  2* 3.14 * float(radius) * (float(height+2))

#print(cylinder_surface_area(4,3,False))


#def list_sum(input_lists):
	#sum = 0
	#for input_list in input_lists:
		#sum += input_list

	#return sum

#print(list_sum([1,2,3]))


#def hours2days(hours):
#print(int(hours / 24), hours % 24)
#hours2days(25)

#def todo_list(new_task, base_list=['wake up']):
    #base_list.append(new_task)
    #return base_list
#todo_list("check the mail")


	



	
	



 