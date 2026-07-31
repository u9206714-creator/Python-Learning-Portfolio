#1、同时获取一个函数的索引和值
'''
fruits = ['apple','banana','orange']
for index, fruit in enumerate(fruits) :
    index = index + 1    
    print(f'第{index}个水果是：{fruit}')
'''
    
#2、圆的面积公式
'''
different_radius = range(1,6)
pi = 3.14
for radius in different_radius:
    area = pi*(radius**2)
    print(f'the area of the circle is {area}')
'''

#3、分别用f-str和.format的方法表示同一项数据
'''
gpa_dict = {'小明':3.251,'小花':3.869,'小李':2.683,'小张':3.685}
'''
#1）.format
'''
for name1, gpa1 in gpa_dict.items():
    print('{0}你好，你当前绩点为：{1:.2f}'.format(name1,gpa1))
'''
#2) f-str
'''
for name2, gpa2 in gpa_dict.items():
    print(f'{name2}你好，你当前绩点为：{gpa2:.2f}')
'''
