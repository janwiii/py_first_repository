import rent
import Return
import messages
import events

def rent_bill(cart):
    '''
        This function prints and writes the bill of the costumes that have been rented.
        Takes the list 'cart' as a parameter.
    '''

    file_contents = events.read_file()
    mainData = events.dictionary(file_contents)

    alpha = False
    while alpha == False:
        name = input("Please enter your name: ")
        if name.isalpha():
            alpha = True
        else:
            messages.invalid()        

    int_contact = False
    while int_contact == False:
        try:
            contact = int(input("Please enter your contact number: ")) #here the string value of the contact is changed into integer datatype
            int_contact = True #loop is terminated
        except:
            messages.invalid() #loop continues as an exception is thrown

    #printing of bill starts here    
    print()
    print("\n                         INVOICE                              \n")
    print("\n" + "Name: " + name)
    print("Phone no.: " + str(contact))
    date = events.date_time()
    print("Rent Date: " + str(date) + "\n")
        
    print("-------------------------------------------------------------")
    print("ID", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("-------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        costume_id = int(cart[index][0])
        costume_quantity = int(cart[index][1])
        costume_name = mainData[costume_id][0]
        costume_brand = mainData[costume_id][1]
        costume_price = int(mainData[costume_id][2].replace("$", "")) * costume_quantity
        total += costume_price
        
        print(str(index + 1) , "\t" , costume_name , "\t" , costume_brand , "\t" , str(costume_price) , "\t" , str(costume_quantity))
        print("\n")
        
    print("Grand Total: " + str(total))
    #bill ends here
    
    #writing the bill starts here
    file = open(name + "_" + str(events.date()) +  ".txt" , "w") #a text file with the name of the user is created
    
    file.write("\n                         INVOICE                              \n")
    file.write("\n" + "Name: " + name + "\n")
    file.write("Phone no.: " + str(contact) + "\n")
    date = events.date_time()
    file.write("Rent Date: " + str(date) + "\n\n")
        
    file.write("-------------------------------------------------------------")
    file.write("\nID\tCostume Name\tBrand\t\tPrice\tQuantity\n")
    file.write("-------------------------------------------------------------\n\n")

    total = 0
    for index in range(len(cart)):
        costume_id = int(cart[index][0])
        costume_quantity = int(cart[index][1])
        costume_name = mainData[costume_id][0]
        costume_brand = mainData[costume_id][1]
        costume_price = int(mainData[costume_id][2].replace("$", "")) * costume_quantity
        total += costume_price
        
        file.write(str(index + 1) + "\t" + costume_name + "\t" + costume_brand + "\t" + str(costume_price) + "\t" + str(costume_quantity))
        file.write("\n\n")
        
    file.write("-------------------------------------------------------------\n\n")
      
    file.write("Grand Total: " + str(total))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n        Thank you! The costumes have been rented.          \n")
    file.write("-------------------------------------------------------------")

    file.close()
    #the text file ends here

def return_bill(cart):
    '''
        This function prints and writes the bill of the costumes that have been rented.
        Takes the list 'cart' as a parameter.
    '''

    file_contents = events.read_file()
    mainData = events.dictionary(file_contents)

    alpha = False
    while alpha == False: #this loop checks whether the name is in alphabetic form or not
        name = input("Please enter your name: ")
        if name.isalpha(): #if the name is found alphabetic then the loop is terminated
            alpha = True 
        else:
            messages.invalid()        

    '''In the following two loops we checked that if the contact and days rented are in integer datatype or not.'''
    int_contact = False
    while int_contact == False:
        try:
            contact = int(input("Please enter your contact number: "))
            int_contact = True
        except:
            messages.invalid()

    int_days = False
    while int_days == False:
        try:
            days_rented = int(input("How many days has it been since you rented the costume? "))
            int_days = True

        except ValueError:
            messages.invalid()

    ''' A fine of $5 is charged if the renting days exceeds 5 days
        The charge is applied per day per costume. '''  
    extra_days = 0
    fine = 0
    if days_rented > 5:
        extra_days = days_rented - 5

    if extra_days > 0:
        fine = 5 * extra_days       

    #bill printing starts here   
    print()
    print("\n                         INVOICE                              ")
    print("\n" + "Name: " + name)
    print("Phone no.: " + str(contact))
    date = events.date_time()
    print("Return Date: " + str(date))
    print("No of days rented: " + str(days_rented) + "\n")
        
    print("-------------------------------------------------------------")
    print("ID", "\t", "Costume Name", "\t", "Brand", "\t\t", "Quantity", "\t", "Fine")
    print("-------------------------------------------------------------\n")

    total_quantity = 0
    for index in range(len(cart)):
        costume_id = int(cart[index][0])
        costume_quantity = int(cart[index][1])
        costume_name = mainData[costume_id][0]
        costume_brand = mainData[costume_id][1]
        costume_price = int(mainData[costume_id][2].replace("$", "")) * costume_quantity

        total_quantity += costume_quantity
        total_fine = fine * total_quantity
        
        print(str(index + 1) , "\t" , costume_name , "\t" , costume_brand , "\t" , str(costume_quantity) , "\t\t" , str(costume_quantity * 5 * extra_days))
        print("\n")

    print("Total Fine = " + str(total_fine) + "\n")
    #bill printing ends here
    
    #bill generation(writing bill) starts here
    file = open(name + "_" + str(events.date()) +  ".txt" , "w")# a text file with the name of the user is created
    
    file.write("\n                         INVOICE                              \n")
    file.write("\n" + "Name: " + name + "\n")
    file.write("Phone no.: " + str(contact) + "\n")
    date = events.date_time()
    file.write("Return Date: " + str(date) + "\n\n")
        
    file.write("-------------------------------------------------------------")
    file.write("\nID\tCostume Name\tBrand\t\tQuantity\tFine\n")
    file.write("-------------------------------------------------------------\n\n")

    total_quantity = 0
    for index in range(len(cart)):
        costume_id = int(cart[index][0])
        costume_quantity = int(cart[index][1])
        costume_name = mainData[costume_id][0]
        costume_brand = mainData[costume_id][1]
        costume_price = int(mainData[costume_id][2].replace("$", "")) * costume_quantity
        total_quantity += costume_quantity
        total_fine = fine * total_quantity
        
        file.write(str(index + 1) + "\t" + costume_name + "\t" + costume_brand + "\t" + str(costume_quantity) + "\t\t" + str(costume_quantity * 5 * extra_days))
        file.write("\n\n")
        
    file.write("-------------------------------------------------------------\n\n")
      
    file.write("Total Fine: " + str(total_fine))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n        Thank you! The costumes have been returned.          \n")
    file.write("-------------------------------------------------------------")

    file.close()
    #bill generation ends here
