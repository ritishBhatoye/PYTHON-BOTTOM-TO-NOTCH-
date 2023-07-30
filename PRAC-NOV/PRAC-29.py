class Student:
    count = 0
    def __init__(self):
        Student.count += 1
        self.name = input("Enter Your Name : ")
        self.roll_no = input("Enter Your Roll No. : ")
        self.city = input("Enter Your City : " )  
    def display(self):
        print("Student name is : ",self.name)
        print("Student roll no. is : ",self.roll_no)        
        print("Student City is : ",self.city)    
        print("Count is : ",Student.count)

std = Student()
std.display()
print("----------")
std1 = Student()
std1.display()
print("----------")
std2 = Student()
std2.display()
print("----------")
