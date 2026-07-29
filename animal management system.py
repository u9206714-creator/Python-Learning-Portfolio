class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'My name is {self.name} , and I am {self.age} years old!'

    def make_sound(self):
        return f'this is an unfamiliar sound!'

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

    def make_sound(self):
        return f'wangwang'

    def introduce(self):
        return f'My name is {self.name} , a {self.age} years old dog , and I am a {self.breed}'

class Cat(Animal):
    def make_sound(self):
        return f'wowwow'

xiaobai = Dog('xaiobai',3,'Golden Rertiever')
mimi = Cat('mimi',2)
print(xiaobai.introduce())
print(xiaobai.make_sound())

print(mimi.introduce())
print(mimi.make_sound())



