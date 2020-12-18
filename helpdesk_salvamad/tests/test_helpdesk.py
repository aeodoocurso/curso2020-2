from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestHelpdesk(TransactionCase):

    def setUp(self):
        super(TestHelpdesk, self).setUp()

        self.ticket = self.env.ref('helpdesk_salvamad.helpdesk_ticket_demo_01')
        self.tag = self.env.ref('helpdesk_salvamad.helpdesk_ticket_tag_demo_01')
        self.ticket.tag_ids = self.tag.ids

    def test_10_tag_assign(self):
        self.assertEqual(self.ticket.tag_ids, self.tag)

    def test_20_raise_exception(self):
        self.ticket.dedicated_time = 2
        self.assertEqual(self.ticket.dedicated_time, 2)
        with self.assertRaises(ValidationError):
            self.ticket.dedicated_time = -2




 