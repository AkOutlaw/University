import Student
import Teacher
import Humans
import Controller

print('Here will be my course application')
teacher = Humans.Teacher('Ben', 'Jones', '12.08.1981', 8900, 'KIT', 7)
student = Humans.Student('Ben', 'Davis', '12.08.2001', 900, 'KIT', 2)
#print(teacher.surName, student.surName)
mass = Controller.Controller.readMass(r'C:\Users\Outlaw\PycharmProjects\University\input.txt')
print('')
#Controller.Controller.printBD(Controller.Controller.getListOfMunans(mass))
Controller.Controller.printBD(Controller.Controller.sortBySalaryHighToLow(Controller.Controller.getListOfMunans(mass)))


#Controller.Controller.printMass(mass)
# print(Controller.Controller.getSumByColumn(mass))
# #print(type(mass))
# Controller.printList(Controller.getSumByColumn(mass))
# #res = change(mass)
# print()
# print('Number of coulumn and max Value are:: ', Controller.maxElem(Controller.getSumByColumn(mass)))

#printMass(mass,N)
#print(getSumByRow(mass))