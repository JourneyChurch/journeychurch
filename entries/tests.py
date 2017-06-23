from django.test import TestCase
from pages.models import NavigationMenu
from datetime import datetime

class EntryTestCase(TestCase):
    """
    Tests for Entry Model
    """

    # Test is_published with NavigationMenu
    def test_is_published(self):

        # Test date
        date = datetime(year=2017, month=6, day=22, hour=9, minute=23, second=0, microsecond=0)


        # True, dates are not specified
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=None, expiration_date=None)
        self.assertEqual(menu.is_published(date=date), True)


        # Entry Date not specified
        # True, date <= expiration date
        expiration_date = datetime(year=2017, month=7, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=None, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), True)

        # False, date > expiration date
        expiration_date = datetime(year=2017, month=5, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=None, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), False)


        # Expiration Date not specified
        # True, date >= entry date
        entry_date = datetime(year=2017, month=5, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=None)
        self.assertEqual(menu.is_published(date=date), True)

        # False, date < entry date
        entry_date = datetime(year=2017, month=7, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=None)
        self.assertEqual(menu.is_published(date=date), False)


        # True, entry_date == date
        entry_date = datetime(year=2017, month=6, day=22, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=7, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), True)


        # True, expiration_date == date
        entry_date = datetime(year=2017, month=5, day=22, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=6, day=22, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), True)


        # True, entry_date < date < expiration_date
        entry_date = datetime(year=2017, month=6, day=21, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=6, day=24, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), True)


        # False, date > expiration_date
        entry_date = datetime(year=2017, month=6, day=20, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=6, day=21, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), False)


        # False, date < entry_date
        entry_date = datetime(year=2017, month=7, day=20, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=7, day=21, hour=9, minute=23, second=0, microsecond=0)
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date)
        self.assertEqual(menu.is_published(date=date), False)


    # Test is_visible()
    def test_is_public(self):

        # Test dates that make is_published() true
        date = datetime(year=2017, month=6, day=22, hour=9, minute=23, second=0, microsecond=0)
        entry_date = datetime(year=2017, month=6, day=21, hour=9, minute=23, second=0, microsecond=0)
        expiration_date = datetime(year=2017, month=6, day=24, hour=9, minute=23, second=0, microsecond=0)


        # True because status is open
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date, status='open')
        self.assertEqual(menu.is_public(date=date), True)


        # False because status is closed
        menu = NavigationMenu(title="Menu", slug="menu", created_date=datetime.now(), updated_date=datetime.now(), entry_date=entry_date, expiration_date=expiration_date, status='closed')
        self.assertEqual(menu.is_public(date=date), False)
