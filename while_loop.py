#1、打印表格中的字符串（与for in函数比较）
'''
list1 = ['H','e','l','l','o']
for char in list1:
    print(char)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1
'''

#2、写一个对用户输入数字求平均值的计算器
'''
user_input = input('请输入数字,输完记得按q:')
total = 0
count = 0
while user_input != 'q':
    num = float(user_input)
    total += num
    count += 1
    user_input = input('请输入数字,输完记得按q:')
if count == 0:  #== is to compare ; = is to assign a value to a valuable
    result = 0
else :
    result = total / count
print(f'你输入的值为：{result}')
'''

#3、使用 while 循环打印数字 1 到 20，每行打印一个数字。
'''
i = 1
while i <= 20:
    print(i)
    i += 1
'''

#4、使用 while 循环计算 1 + 2 + 3 + ... + 100 的总和，并打印结果。
'''
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)
'''

#5、让用户输入一个正整数。如果输入的数字<=0, /
   #就一直提示“请输入一个正整数：”重新输入，直到用户输入正确的正整数为止。最后打印“你输入的数字是：xxx”
'''
user_input = int(input('请输入一个正整数:'))
while user_input <= 0 :
    print('请输入一个正整数,重新输入:')
    user_input = int(input('请输入一个正整数:'))
print(f'你输入的数字为：{user_input}')
'''

