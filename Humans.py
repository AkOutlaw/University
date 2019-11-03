class Student:
    def __init__(self, firstname, lastname, dateofbirth, scholarship, faculty, courseofstudy):
        self.firstName = firstname
        self.surName = lastname
        self.dataOfBirth = dateofbirth
        self.scholarship = scholarship
        self.faculty = faculty
        self.courseOfStudy = courseofstudy

class Teacher:
    def __init__(self, firstname, lastname, dateofbirth, salary, faculty, experience):
        self.firstName = firstname
        self.surName = lastname
        self.dataOfBirth = dateofbirth
        self.salary = salary
        self.faculty = faculty
        self.experience = experience
