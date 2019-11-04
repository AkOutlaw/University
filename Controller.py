import Humans

class Controller:
    def __init__(self):
        return 1

    def getListOfMunans(mass):
        listOfMunans = []
        # listOfStudents = []
        # listOfTeachers = []

        for row in mass:
            temp = []
            isStudent = 0
            #print(row[3])
            if 'salary' in row[3]:
                isStudent = 0
            else:
                isStudent = 1
            #print(isStudent)
            for elem in row:
                elem = (elem[elem.find("=") + 1 : ])
                temp.append(elem)
            if isStudent == 1:
                student = Humans.Student(*temp)
                listOfMunans.append(student)
                #listOfStudents.append(student)
            elif isStudent == 0:
                teacher = Humans.Teacher(*temp)
                listOfMunans.append(teacher)
                #listOfTeachers.append(teacher)

        return listOfMunans

    def getSalaryOrScholarship(listOfHumans):
        for obj in listOfHumans: # get class object one by one
            #print(type(obj))
            if hasattr(obj, 'scholarship'):
                return obj.scholarship
            elif hasattr(obj, 'salary'):
                return obj.salary

# Process of sorting by Salary
    def sortBySalaryHighToLow(listOfHumans):
        #listOfHumansOrdered = sorted(listOfHumans,  key=lambda x: int(x.scholarship), reverse=True)  # sorting from high to low
        listOfHumansOrdered = sorted(listOfHumans, key=lambda x: int(x.scholarship) if int(x.scholarship) else int(x.salary), reverse=True)  # sorting from high to low
        return listOfHumansOrdered

# Process of printing data using formation
    def printBD(listOfHumans):
        for obj in listOfHumans: # get class object one by one
            #print(type(obj))
            if hasattr(obj, 'courseOfStudy'):
                print('|First name - %6s;  |  Last name - %10s;  |   Date Of Birth - %10s;  |  scholarship- %5s;  |  faculty - %4s;  |  courseofstudy - %9s;|' # get fields from object
                      % (obj.firstName, obj.surName, obj.dataOfBirth, obj.scholarship, obj.faculty, obj.courseOfStudy))
            if hasattr(obj, 'experience'):
                print('|First name - %6s;  |  Last name - %10s;  |   Date Of Birth - %10s;  |  Salary - %5s;  |  faculty - %4s;  |  expirience - %9s;|' # get fields from object
                      % (obj.firstName, obj.surName, obj.dataOfBirth, obj.salary, obj.faculty, obj.experience))
# Process of reading data from file; return as massive
    def readMass(path):
        file = open(path)
        mass = []
        for line in file:
            row = line.strip().split(' ') # string concatination
            mass.append(row) # adding per row to massive
        file.close()
        return mass
