import bills
import messages
import events

def valid_id_rent(mainData):
    '''
        This function checks if the ID entered is valid or not.
        If the ID is not valid, an invalid message is shown.
        Takes the dictionary as a parameter.
        Returns the valid ID.
    '''
    valid_data = False
    while valid_data == False:
        try:
            ID = int(input("Enter the ID of the costume you want to rent: "))
            if ID > 0 and ID <= len(mainData): #ID should be greater than 0 and less than or equal to the length of the dictionary
                if int(mainData[ID][3]) > 0:
                    valid_data = True
                    return ID
                else:
                    messages.out_of_stock()
            else:
                messages.invalid()
        except:
            messages.invalid()

def valid_quantity_rent(mainData, ID):
    ''' This function checks if the quantity of the costume is available or not '''
    valid_quan = False
    while valid_quan == False:
        try:
            quantity = int(input("How many pieces do you want to rent? "))
            if quantity > 0 and quantity <= int(mainData[ID][3]):
                valid_quan = True
                return quantity
            else:
                messages.range()
        except:
            messages.invalid()

def rent():
    ''' This function is the main function that rents the costume.
        A 2D list is created which holds the ID and quantity of the costume.
        The user is asked if s/he wants to rent more costumes.
        A function to print and write the bill is called.
    '''
    print("\n Let's rent a costume. \n")

    file_contents = events.read_file()
    mainData = events.dictionary(file_contents)
    
    cart = []
    events.print_costumes(file_contents, mainData)
    continueLoop = True #assigning boolean value to a variable
    while continueLoop == True: #outerloop
        
        Id = valid_id_rent(mainData)
        messages.available()
        qn = int(valid_quantity_rent(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) - qn
        cart.append([Id, qn])

        events.write_file(mainData)
        events.print_costumes(file_contents, mainData)
        
        more = True
        while more == True: #innerloop
            userInput = input("Do you want to rent more costumes?(yes/no) ")

            if userInput.lower() == "no":
                continueLoop = False #outerloop is terminated, bill details will be asked
                more = False #innerloop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True #outerloop continues, more costumes will be rented
                more = False #innerloop is terminated

            else:
                messages.invalid()
                more = True #innerloop continues
    
    print()
    bills.rent_bill(cart) #function to print and write the bill
    messages.rented()
