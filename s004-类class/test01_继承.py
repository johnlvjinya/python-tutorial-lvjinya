
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num



if __name__=='__main__':
    P = Person('lvjinya', 18)
    E = Employee('帅哥', 12, 4)
    print(P.__dict__)
    print(E.__dict__)