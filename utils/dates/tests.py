from django.test import TestCase
from datetime import datetime
from utils.dates.format import format_date_month_year, format_date_month_day

class FormatTestCase(TestCase):
    """
    Test format date functions
    """

    def test_format_date_month_year(self):

        # Both dates are empty
        start_date = None
        end_date = None

        self.assertEqual(format_date_month_year(start_date, end_date), None)

        # No start date
        start_date = None
        end_date = datetime(2002, 1, 12)

        self.assertEqual(format_date_month_year(start_date, end_date), None)

        # No end date
        start_date = datetime(2002, 1, 11)
        end_date = None

        self.assertEqual(format_date_month_year(start_date, end_date), "January 2002")

        # Same month and year
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 1, 12)

        self.assertEqual(format_date_month_year(start_date, end_date), "January 2002")

        # Different month, same year
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 2, 12)

        self.assertEqual(format_date_month_year(start_date, end_date), "January - February 2002")

        # Different year, same month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2003, 1, 12)

        self.assertEqual(format_date_month_year(start_date, end_date), "January 2002 - January 2003")

        # Different year, different month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2003, 2, 12)

        self.assertEqual(format_date_month_year(start_date, end_date), "January 2002 - February 2003")


    def test_format_date_month_day(self):

        # Both dates are empty
        start_date = None
        end_date = None

        self.assertEqual(format_date_month_day(start_date, end_date), None)

        # No start date
        start_date = None
        end_date = datetime(2002, 1, 12)

        self.assertEqual(format_date_month_day(start_date, end_date), None)

        # No end date
        start_date = datetime(2002, 1, 11)
        end_date = None

        self.assertEqual(format_date_month_day(start_date, end_date), "January 11")

        # Same month and day
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 1, 11)

        self.assertEqual(format_date_month_day(start_date, end_date), "January 11")

        # Different month, same day
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 2, 11)

        self.assertEqual(format_date_month_day(start_date, end_date), "January 11 - February 11")

        # Different day, same month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 1, 12)

        self.assertEqual(format_date_month_day(start_date, end_date), "January 11 - 12")

        # Different day, different month
        start_date = datetime(2002, 1, 11)
        end_date = datetime(2002, 2, 12)

        self.assertEqual(format_date_month_day(start_date, end_date), "January 11 - February 12")
