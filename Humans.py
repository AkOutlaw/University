import Controller

class People:
    def __init__(self, firstname, lastname, dateofbirth,sourceofincome , faculty, courseexperience):
        self.firstName = firstname
        self.surName = lastname
        self.dataOfBirth = dateofbirth
        self.sourceOfIncome = sourceofincome
        self.faculty = faculty
        self.courseExperience = courseexperience

    def getSizeOfMoney(people):
         raise NotImplementedError("Subclass must implement abstract method")

class Student(People): #parent class Student with init constructor
    def __init__(self, firstname, lastname, dateofbirth, scholarship, faculty, courseofstudy):
        self.firstName = firstname
        self.surName = lastname
        self.dataOfBirth = dateofbirth
        self.scholarship = scholarship
        self.faculty = faculty
        self.courseOfStudy = courseofstudy

    def getSizeOfMoney(self):
        return self.scholarship

class Teacher(People): #parent class Teacher with init constructor
    def __init__(self, firstname, lastname, dateofbirth, salary, faculty, experience):
        self.firstName = firstname
        self.surName = lastname
        self.dataOfBirth = dateofbirth
        self.salary = salary
        self.faculty = faculty
        self.experience = experience

    def getSizeOfMoney(self):
        return self.salary
