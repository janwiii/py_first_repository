import messages
import rent
import Return
import events

messages.welcome()
loop = True

while loop == True:
    messages.select_option()

    select_option = False
    while select_option == False:
        try:
            select = int(input("Enter an option: "))
            select_option = True
        except:
            messages.invalid()
            messages.select_option()

    if select == 1:
        rent.rent()

    elif select == 2:
        Return.Return()

    elif select == 3:
        messages.thanks()
        loop = False

    else:
        messages.invalid()
