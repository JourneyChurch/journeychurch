from django.test import TestCase
from pages.models import NavigationMenu
from datetime import datetime

class EntryTestCase(TestCase):
    """
    Tests for Entry Model
    """

    # Test is_published. This test is relative to the current time so these values with need to be changed if ran again
    def test_is_published(self):

        # True test case with navigation menu
        entry_date = datetime(year=2017, month=6, day=22, hour=9, minute=23, second=0)
        expiration_date = datetime(year=2017, month=7, day=22, hour=9, minute=23, second=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)

        self.assertEqual(menu.is_published(), True)

        # False test case with navigation menu
        entry_date = datetime(year=2017, month=6, day=23, hour=22, minute=23, second=0)
        expiration_date = datetime(year=2017, month=7, day=22, hour=9, minute=23, second=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)

        self.assertEqual(menu.is_published(), False)
