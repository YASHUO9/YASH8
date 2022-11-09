class Student:
    pass

si = Student()
s2 = Student()
s3 = Student()



si.name = "mohann"
s2.name = "rohan"
s3.name = "Mohit"

si.roll = 1
s2.roll = 2

print(si.roll)
print(si.name)
print(si.__dict__)
# print(s3.roll)


#this method is used to find the attribute is present or not by giving the true or  false sign
ok = hasattr(si,"name")
print(ok)





#this method attribute is used to delete the attribute
delattr(si,"name")
print(si.name)








