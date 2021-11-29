from unittest.mock import patch
import unittest
from TicketManager import get_ticket

# This file tests the function that makes the request for the ticket. Fill in your credentials


username = '{email}/token'
api = '{apikey}'
ticket_url = 'https://{subdomain}.zendesk.com/api/v2/tickets/1'


class TestTicketManager(unittest.TestCase):

    def test_monthly_schedule(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            ticket = get_ticket(url=ticket_url, user=username, apikey=api)
            mocked_get.assert_called_with(ticket_url, auth=(username, api))
            self.assertEqual(ticket, 'Success')

            mocked_get.return_value.ok = False

            schedule = get_ticket(url=ticket_url, user=username, apikey=api)
            mocked_get.assert_called_with(ticket_url, auth=(username, api))
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
