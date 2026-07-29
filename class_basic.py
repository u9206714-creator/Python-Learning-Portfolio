#1、类定义属性
'''
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

cat1 = CuteCat('jojo',2,'orange')
'''

#2、类定义方法 -> 调用类方法：对象.方法名 ; 在class中定义函数

#practice

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.number = student_id
        self.grades = {'chinese':0,'maths':0,'english':0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f'{self.name}(number:{self.number}) test scores:')
        for course in self.grades:
            print(f'{course}:{self.grades[course]}')
    def get_grade(self,course):
        if course in self.grades:
            return self.grades[course]
        else:
            return 'None such course!'
    def average_grade(self):
        total = 0
        for course in self.grades:
            total += self.grades[course]
        return total / len(self.grades)
    def highest_grade(self):
        highest_course = ""
        highest_score = -1
        for course in self.grades:
            if self.grades[course] > highest_score:
                highest_score = self.grades[course]
                highest_course = course
        return highest_course, highest_score
    def print_result(self):
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
    # 打印每门成绩
        self.print_grades()
    # 打印平均分
        print(f"Average : {self.average_grade():.2f}")
    # 打印最高分
        course, score = self.highest_grade()
        print(f"Highest : {course} ({score})")

#4、
stu1 = Student("Jack","01")
stu1.set_grade("chinese",95)
stu1.set_grade("maths",94)
stu1.set_grade("english",88)
stu1.print_result()


#3、
#stu1 = Student('Jack','01')
#stu1.set_grade('chinese',95)
#stu1.set_grade('maths',97)
#stu1.set_grade('english',98)
#stu1.highest_grade()

#2、
#stu1 = Student('Jack','01') 
#stu1.set_grade('chinese',95)
#stu1.set_grade('maths',97)
#stu1.set_grade('english',98)
#print(stu1.average_grade())

#1、
#stu1 = Student('Jack','01')
#stu1.set_grade('english',88)
#print(stu1.get_grade('english'))

#stu1 = Student('Jack','01',)
#stu1.set_grade('chinese',95)
#stu1.set_grade('maths',94)
#stu1.print_grades()
#stu2 = Student('Alice','02')
#print(stu1.name)
#stu2.set_grade('maths',95)
#print(stu2.grades)

 

