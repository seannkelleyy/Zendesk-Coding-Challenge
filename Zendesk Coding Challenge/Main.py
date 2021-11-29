import DisplayManager

# this file is the main menu that allows the user to input what they want to do. The .title() allows the user to input
# the their response with no capital letters or all capital letters.

print('Welcome to the ticket viewer')
print()
option_input_1 = input("Enter 'Menu' to view options or enter 'Quit' to exit: ").title()

while True:
    if option_input_1 == 'Quit':  # quits program
        quit()
    elif option_input_1 == 'Menu':   # calls the menu function from DisplayManager.py
        DisplayManager.menu()
    else:
        print("Invalid Input")   # finds a invalid input and prompts user to choose again.
        option_input_1 = input("Enter 'Menu' to view options or enter 'Quit' to exit: ").title()
