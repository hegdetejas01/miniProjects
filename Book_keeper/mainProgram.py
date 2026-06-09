# This implements the main program

import customerClass as c
import productClass as p
import keeperClass as k
import printStatement as p
import productClass as pr


# login as employee - done only for the first time
employee = k.Keeper()

print(p.employee_login_message)
loggedIn = employee.loginEmployee()

if loggedIn:
    print(p.login_successfull_keeper)

    inputValue = employee.createMainMenu(employee.getData("name"))
    if inputValue == 1:
        k.makeBill()


    elif inputValue == 2:
        pass
    elif inputValue == 3:
        del employee
        exit()




