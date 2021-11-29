import TicketManager

# this menu allows the user to pick if they want to view all tickets or a certain ticket. It calls the function for
# the users desired input.


def menu():
    print('         Select View Options:')
    print('         -Press 1 to view all tickets')
    print('         -Press 2 to view a ticket')
    print("         -Type 'Quit' to exit the program")
    menu_input = input('         Enter your selection: ').title()
    while True:
        if menu_input == 'Quit':   # quits the program.
            quit()
        elif menu_input == '1':
            TicketManager.all_tickets()    # calls the all_tickets function to view all the tickets on an account
        elif menu_input == '2':
            TicketManager.single_ticket()    # calls the single_ticket function which allows the user to pick a ticket
        else:
            print('         Invalid Input')     # finds a invalid input and prompts user to choose again.
            menu_input = input('         Enter your selection: ')
