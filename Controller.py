import Humans

class Controller:
    def __init__(self):
        return 1

    def getListOfMunans(mass):
        listOfMunans = []
        listOfStudents = []
        listOfTeachers = []

        for row in mass:
            temp = []
            for elem in row:
                #print(elem)
                elem = (elem[elem.find("=") + 1 : ])
                temp.append(elem)
            #print(temp)
            student = Humans.Student(*temp)
            listOfMunans.append(student)
        return listOfMunans

    def sortBySalaryHighToLow(listOfHumans):
        listOfHumansOrdered = sorted(listOfHumans, key=lambda x: int(x.scholarship), reverse=True)
        return listOfHumansOrdered


    def printBD(listOfHumans):
        for obj in listOfHumans:
            print('|First name - %6s;  |  Last name - %10s;  |   Date Of Birth - %10s;  |  scholarship - %5s;  |  faculty - %4s;  |  courseofstudy - %9s;|'
                  % (obj.firstName, obj.surName, obj.dataOfBirth, obj.scholarship, obj.faculty, obj.courseOfStudy))


    def readMass(path):
        file = open(path)
        mass = []
        for line in file:
            row = line.strip().split(' ')
            mass.append(row)

        file.close()
        return mass