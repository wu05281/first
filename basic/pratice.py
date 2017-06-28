class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def get_name():
        return 'alex.'

    def description(self):
        print('this is Person class')


class Student:
    def __new__(cls, *args, **kwargs):
        print('this\'s new method')
        print(args)
        print(kwargs)
        return super(Student, cls).__new__(cls)

    def __init__(self, name, age, language):
        print('this\' init method.')
        # 这个方法是以父类的初始化方式初始化子类属性
        self.name = name
        self.age = age
        self.language = language


    def description(self):
        print('this is Student class')


if __name__ == '__main__':
    stu = Student(name='alex', age=20, language='cn')
    print(stu)
