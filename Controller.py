import Humans

class Controller:
    def __init__(self):
        return 1

    def getListOfMunans(mass):
        listOfMunans = []
        # listOfStudents = []
        # listOfTeachers = []
        teacherIdentidier = 'salary'

        for row in mass:
            temp = []
            isStudent = 0
            if teacherIdentidier in row[3]: # is row contains 'salary' then Teacher
                isStudent = 0
            else:
                isStudent = 1
            for elem in row:
                elem = elem.split('=') # split row to get value for field of the object
                elem = elem[1]  # get values
                temp.append(elem)
            if isStudent == 1:
                student = Humans.Student(*temp) # Create class object Student
                listOfMunans.append(student) #add Student to list
                #listOfStudents.append(student)
            elif isStudent == 0:
                teacher = Humans.Teacher(*temp)
                listOfMunans.append(teacher)
                #listOfTeachers.append(teacher)

        return listOfMunans

# Process of sorting by Salary
    def sortBySalaryHighToLow(listOfHumans):
        listOfHumansOrdered = sorted(listOfHumans,  key=lambda x: int(x.getSizeOfMoney()), reverse=True)  # sorting from high to low
        return listOfHumansOrdered

# Process of printing data using formation
    def printBD(listOfHumans):
        for obj in listOfHumans: # get class object one by one
            #print(type(obj))
            if hasattr(obj, 'courseOfStudy'):
                print('|First name - %6s;  |  Last name - %10s;  |   Date Of Birth - %10s;  |  scholarship- %5s;  |  faculty - %4s;  |  courseofstudy - %9s;|' # get fields from object
                      % (obj.firstName, obj.surName, obj.dataOfBirth, obj.scholarship, obj.faculty, obj.courseOfStudy))
            if hasattr(obj, 'experience'):
                print('|First name - %6s;  |  Last name - %10s;  |   Date Of Birth - %10s;  |  Salary - %9s;  |  faculty - %4s;  |  expirience - %12s;|' # get fields from object
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
