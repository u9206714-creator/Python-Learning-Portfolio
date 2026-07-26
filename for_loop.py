#1、打印一到十的所有数字
'''
for i in range(1,11):
    print(i)
'''
    
#2、计算1到100的总和
'''
total = 0
for i in range(1,101):
    total = i + total
print(total)
'''

#3、打印列表中所有大于60的成绩
'''
student_score = [1,3,47,56,67,79,85,92]
for score in student_score:
    if score > 60:
        print(score)
'''

#4、遍历一个字典，打印所有key和value
'''
dict = {'student_A':'01','student_B':'02','student_C':'03','student_D':'04'}
for student, code in dict.items():
    print(student,code)
'''



