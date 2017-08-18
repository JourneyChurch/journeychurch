from django.test import TestCase
from datetime import datetime
from utils.dates.format import format_two_dates

class FormatTestCase(TestCase):
    """
    Test format date functions
    """

    def test_format_two_dates(self):

        # Same month and year
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 1, 12)

        self.assertEqual(format_two_dates(start_date, end_date), "January 2002")

        # Different month, same year
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 2, 12)

        self.assertEqual(format_two_dates(start_date, end_date), "January - February 2002")

        # Different year, same month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2003, 1, 12)

        self.assertEqual(format_two_dates(start_date, end_date), "January 2002 - January 2003")

        # Different year, different month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2003, 2, 12)

        self.assertEqual(format_two_dates(start_date, end_date), "January 2002 - February 2003")
