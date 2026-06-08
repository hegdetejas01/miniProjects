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

        productList = []
        isProductPresent = True
        name = input(p.get_customer_name)
        number = input(p.get_customer_number)
        customer = c.Customer(name,number)
        
        while isProductPresent:
            productName = input(p.get_product_name)
            productList.append(productName)
            isProductPresent = int(input("Press 1 to add new product"))

        print(productList)

    elif inputValue == 2:
        pass
    elif inputValue == 3:
        del employee
        exit()




