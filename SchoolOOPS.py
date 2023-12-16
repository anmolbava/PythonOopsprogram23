class Student():
    school = "Bishops School"
    passoutyear = 2012
    def __init__(self,name,roll,house,standard):
        self.name= name
        self.rollno=roll
        self.house=house
        self.standard=standard
    def plays(self,name):
        print(s1.name,"plays football")

s1 = Student("anmol",4,"arnold",10)
s1.plays("anmol")
s1.school = "Army Public School"
print(s1.school)
s2 = Student("varun",9,"red",20)
print(Student.school)
print("anmol is from the following school",Student.school)
print(s2.school)
print(Student.school)

