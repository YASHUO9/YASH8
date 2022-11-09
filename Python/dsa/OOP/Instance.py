class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def studentPrint(self):
        print("Student: " + self.name + " Roll: " + str(self.roll))
        
        
        
s = Student("mog",1)

s.studentPrint()
        
        
        