import bills
import messages
import events

def valid_id_return(mainData):
    '''
        This function checks if the ID entered is valid or not.
        If the ID is not valid, an invalid message is shown.
        Takes the dictionary as a parameter.
        Returns the valid ID.
    '''
    valid_id = False
    while valid_id == False:
        try:
            ID = int(input("Enter the ID of the costume you want to return: "))
            if ID > 0 and ID <= len(mainData):
                valid_id = True
                return ID
            else:
                messages.invalid()
        except ValueError:
            messages.invalid()

def valid_quantity_return(mainData, ID):
    '''
        This function checks if the quantity entered is valid or not i.e. quantity is more than 0.
        Returns Quantity of the costumes to be returned
    '''
    valid_quan = False
    while valid_quan == False:
        try:
            quantity = int(input("How many pieces do you want to return? "))
            if quantity > 0:
                valid_quan = True
                return quantity
            else:
                messages.invalid()
        except ValueError:
            messages.invalid()

def Return():
    ''' This function is the main function that returns the costume.
        A list is created which holds the ID and quantity of the costume.
        The user is asked if s/he wants to return more costumes.
        A function to print and write the bill of the returned is called.
    '''
    print("\n Let's return a costume. \n")

    file_contents = events.read_file()
    mainData = events.dictionary(file_contents)

    cart = []
    continueLoop = True
    while continueLoop == True: #outerloop
        events.print_costumes(file_contents, mainData) #list of costumes is printed
        Id = valid_id_return(mainData)
        qn = int(valid_quantity_return(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) + qn
        cart.append([Id, qn])

        events.write_file(mainData)
        events.print_costumes(file_contents, mainData)

        more = True
        while more == True: #innerloop
            userInput = input("Do you want to return more costumes?(yes/no) ")
            if userInput.lower() == "no":
                continueLoop = False #outerloop is terminated, bill details will be asked
                more = False #innerloop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True #outerloop continues, more costumes will be returned
                more = False #innerloop is terminated

            else:
                messages.invalid() 
                more = True #innerloop continues
    
    print()
    bills.return_bill(cart) #function to print and write the bill
    messages.returned()

