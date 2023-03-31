def read_file():
    ''' This function fetches data from the file '''
    file = open("costumes.txt", "r")
    data = file.readlines()
    file.close()
    return data

def dictionary(file_contents):
    '''
        Function converts file's content into dictionary
        Takes content of a txt file as parameter.
        Returns a dictionary with integer keys starting from 1.
    '''
    data = {}
    for index in range(len(file_contents)):
        data[index + 1] = file_contents[index].replace("\n", "").split(",")
    return data

def print_costumes(file_contents, mainData):
    '''
        This fucntion shows the list of the costumes by reading the file
        Takes contents of the text file and the dictionary created as a parameter
    '''
    print("-------------------------------------------------------------")
    print("ID", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("-------------------------------------------------------------\n")
    for key,value in mainData.items():  # Iterates over keys and values of mainData dictionary
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])

    print("\n-------------------------------------------------------------\n")

def write_file(mainData):
    '''
        This function writes in the selected text file.
        The quantity of the costumes is reduced if it is called in the rent file
        and it is increased ifit is called in the return method in the text file.
    '''
    file = open("costumes.txt", "w")
    for value in mainData.values():
        write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
        file.write(write_data)
    file.close()

def date_time():
    ''' This function is for updating date and time in the bill '''
    import datetime

    year    = (datetime.datetime.now().year)
    month   = (datetime.datetime.now().month)
    day     = (datetime.datetime.now().day)
    hour    = (datetime.datetime.now().hour)
    minute  = (datetime.datetime.now().minute)
    
    date = (str(year) + "-" + str(month) + "-" + str(day)+ " " + str(hour) + ":" + str(minute))
    return date

def date():
    import datetime
    
    year    = (datetime.datetime.now().year)
    month   = (datetime.datetime.now().month)
    day     = (datetime.datetime.now().day)

    date_ = (str(year) + "-" + str(month) + "-" + str(day))
    return date_
