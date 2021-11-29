import requests
import json

username = '{email}token'
api = '{api key}'

# this function makes the request to the zendesk api and retrieves the ticket


def get_ticket(url, user, apikey):
    ticket = requests.get(url, auth=(user, apikey))
    if ticket.ok:
        return ticket and ticket.text  # ticket.text is used for the unit test and ticket is sent to the functions that
    else:                               # allow the user to view the tickets
        return 'Bad Response!'


# this is the function that finds all the tickets on the account. This uses a counter and uses the count to change the
# url to the ticket


def all_tickets():
    view_next_page = True
    counter = 0  # establishes a counter for the ticket id
    while view_next_page:   # loop for making allowing only 25 tickets to be displayed at once
        while True:   # loop that continues to print tickets
            try:
                counter += 1
                ticket_url = f'https://zccseankelley156.zendesk.com/api/v2/tickets/{counter}'
                ticket = get_ticket(url=ticket_url, user=username, apikey=api)
                ticket_json = json.loads(ticket)

                # The following lines finds the desired information from a ticket and saves it under a variable.
                ticket_subject = ticket_json['ticket']['subject']
                ticket_date = ticket_json['ticket']['created_at']
                ticket_requester = ticket_json['ticket']['requester_id']
                print(f'Ticket number: {counter}, Ticket subject: {ticket_subject}, Ticket date: {ticket_date}, Ticket '
                      f'requester: {ticket_requester}')
                # The above line organizes the desired info from a ticket into a print statement.
                remainder = counter / 25 # this calculates if a ticket id is divisible by 25 to see if there have been
                # 25 tickets presented.
                if remainder.is_integer():  # this uses the remainder variable to see if there has been 25 tickets shown
                    view_next_page = False
                    page_next = input('Type "Yes" to view next page of tickets. Type "View Ticket" to view a '
                                      'specific ticket. Type "Quit" to exit. : ').title()
                    if page_next == "Quit":
                        quit()      # This quits the program.
                    elif page_next == 'Yes':
                        view_next_page = True  # allows the loop to continue if the user desires.
                    elif page_next == "View Ticket":  # allows the user to view a specific ticket.
                        single_ticket()
                    else:
                        print('Invalid input')   # finds a invalid input and prompts user to choose again.
                        page_next = input('Type "Yes" to view next page of tickets. Type "View Ticket" to view a '
                                          'specific ticket. Type "Quit" to exit. : ').title()
            except requests.exceptions.ConnectionError:  # this exception is raised if there is no internet connection
                print('Connection Error... Exiting.')
                quit()
            except KeyError:  # this exception is raised if the url is not found, when there is not a ticket id for
                # for the ticket
                ticket_lookup = input('No more tickets found. Type "Yes" to view a ticket.'
                                      ' Type "Quit" to exit. : ').title()
                if ticket_lookup == 'Quit':
                    quit()          # This quits the program.
                elif ticket_lookup == 'Yes':
                    single_ticket()  # Calls the single_ticket function, which allows the user to view a specific ticket

#  This function is used to ask the user wht ticket they want to view and if they want to view the description


def single_ticket():
    while True:   # This loops continues to ask the user what ticket they want to view, until they decide to quit.
        try:
            ticket_choice = str(input('What ticket would you like to view? Type "Quit" to exit. : ')).title()
            if ticket_choice == 'Quit':
                quit()
            ticket_url = f'https://zccseankelley156.zendesk.com/api/v2/tickets/{ticket_choice}'
            ticket = get_ticket(url=ticket_url, user=username, apikey=api)
            ticket_json = json.loads(ticket)  # this converts the string that was given to json, so it can be parsed.

            # The following lines finds the desired information from a ticket and saves it under a variable.
            ticket_subject = ticket_json['ticket']['subject']
            ticket_date = ticket_json['ticket']['created_at']
            ticket_description = ticket_json['ticket']['description']
            ticket_requester = ticket_json['ticket']['requester_id']
            print(f'Ticket subject: {ticket_subject}, Ticket date: {ticket_date}, Ticket requester: {ticket_requester}')
            # The above line organizes the desired info from a ticket into a print statement.
            ticket_description_input = input('Type "Yes" to view ticket description, type "quit" to exit: ').title()
            if ticket_description_input == 'Quit':
                quit()      # This quits the program.
            elif ticket_description_input == 'Yes':  # Prints the description for a desired ticket.
                print(ticket_description)
            else:
                print('Invalid Entry')  # finds a invalid input and prompts user to choose again.
                ticket_description_input = input('Type "Yes" to view ticket description, type "quit" to exit: ').title()
        except requests.exceptions.ConnectionError:  # This is looking for a connection error.
            print('Connection Error... Exiting.')
            quit()
        except KeyError:   # If no ticket can be found, this asks wht ticket they want to view.
            print('         no ticket found')
            ticket_choice = input('What ticket would you like to view? Type "quit" to exit: ')
            if ticket_choice == 'quit':
                quit()    # This quits the program.
            print(ticket_choice)
        else:
            print('Invalid input.')   # finds a invalid input and prompts user to choose again.
            ticket_choice = input('What ticket would you like to view? Type "quit" to exit: ')
            return ticket_choice
