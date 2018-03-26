#算术运算符

#加法：+
print(3+4)

#减法：-
print(3-5)

#乘法：*
print(3*5)

#乘方：**
print(3**2) #9  3*3
print(3**4)  #81 3*3*3*3

#模运算：%
print(9%2) #1

#整数除法: //   结果向下取整,即使是负数，也向下取整
print(9//2) #4
print(-9//2) #-5

#整型：int
print(int(4.9))  #4
#浮点型
print(float(4)) #4.0

#变量：多重变量赋值
a,b=300,400
print(a)
print(b)

#变量：更改变量的值:代码按顺序执行，导致表达式之后的变量重新赋值并不会改变该表达式的值，除非在变量更改之后，重新计算该表达式
c=300
d=10
e=c/d
print(e) #30
d=20
print(e) #30
e=c/d
print(e) #15

#Bool值：True,False

#内置函数： len()  type()