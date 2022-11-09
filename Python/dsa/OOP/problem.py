class Student:
    name = "Parikh"
    def store_detail(self):
        self.age = 60
    def print_age(self):
        print(Student.store_detail(self))
s = Student()
s.store_detail()
s1 = Student()
s1.print_age()



#you call store_detail on s1.s1 entity doesnot have age attribute yet


















