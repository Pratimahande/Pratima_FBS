class Student:

    def __init__(self,s_id,s_name,age,percentage):

        self.s_id=s_id
        self.s_name=s_name
        self.age=age
        self.percentage=percentage
    
    def accept(self):

        self.s_id=int(input("ENTER THE STUDENT ID : "))
        self.s_name=input("ENTER THE STUDENT NAME : ")
        self.age=input("ENTER THE STUDENT AGE : ")
        self.percentage=float(input("ENTER THE STUDENT PERCENTAGE : "))
    
    def CalculateRank(self):

        if (self.percentage >=85):
            return "Distinction"
        elif(self.percentage >=70):
            return "Frist Class"
        elif(self.percentage >=50):
            return "Second Class"
        elif(self.percentage >=35):
            return "Pass"
        else:
            return "Fail"
    
    def display(self):

        print("STUDENT ID : ",self.s_id)
        print("STUDENT NAME : ",self.s_name)
        print("STUDENT AGE : ",self.age)
        print("STUDENT PERCENTAGE : ",self.percentage)

    def __str__(self):

        return(f"STUDENT ID : {self.s_id}\n "
               f"STUDENT NAME : {self.s_name}\n"
               f"STUDENT AGE : {self.age}\n"
               f"STUDENT PERCENTAGE : {self.percentage}\n")  

class EnggStudent(Student):

    def __init__(self, stu_id, stu_name, stu_age, stu_percentage, branch, internal_mark):
        
        super().__init__(stu_id, stu_name, stu_age, stu_percentage)
        self.branch=branch
        self.internal_mark=internal_mark
    
    def accept(self):

        super().accept()
        self.branch=input("ENTER THE ENGGINER BRANCH : ")
        self.internal_mark=int(input("ENTER THE ENGGINER INTERNAL MARKS : "))
    
    def CalculateRank(self):
        
        if (self.percentage >=85 and self.internal_mark >=50):
            return "Distinction"
        elif(self.percentage >=70 and self.internal_mark >=30):
            return "Frist Class"
        elif(self.percentage >=50):
            return "Second Class"
        elif(self.percentage >=35):
            return "Pass"
        else:
            return "Fail"
    
    def display(self):
         
         super().display()
         print("BRANCH : ",self.branch)
         print("INTERNAL MARKS : ",self.internal_mark)
         print("STUDENT RANK : ",self.CalculateRank())
    
    def __str__(self):

        print("##########################################")
        return (f"STUDENT ID : {self.s_id}\n "
               f"STUDENT NAME : {self.s_name}\n"
               f"STUDENT AGE : {self.age}\n"
               f"STUDENT PERCENTAGE : {self.percentage}\n"
               f"BRANCH : {self.branch}\n"
               f"INTERNAL MARKS : {self.internal_mark}\n"
               f"RANK : {self.CalculateRank()}") 

e1 = EnggStudent(101,'Pratima',32,75,'IT/Devloper',50)
e1.display()
print(e1)    