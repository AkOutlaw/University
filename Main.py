import Controller

print('Here will be my course application!!!')
mass = Controller.Controller.readMass(r'C:\Users\Outlaw\PycharmProjects\University\input.txt')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Here is the data from the file:')
Controller.Controller.printBD(Controller.Controller.getListOfMunans(mass))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Here is the sorted data from the file:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
Controller.Controller.printBD(Controller.Controller.sortBySalaryHighToLow(Controller.Controller.getListOfMunans(mass)))
