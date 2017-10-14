import datetime
import imp
import unittest


clock = imp.load_source('clock', './clock')


class TestDateParse(unittest.TestCase):
    def test_month_day(self):
        expect = datetime.date(datetime.date.today().year, 10, 31)
        result = clock.date_parse("10-31")
        self.assertEqual(result, expect)
    def test_year_month_day(self):
        expect = datetime.date(2016, 10, 31)
        result = clock.date_parse("2016-10-31")
        self.assertEqual(result, expect)


class TestTimeParse(unittest.TestCase):
    def test_hour_minute(self):
        now = datetime.date.today()
        expect = datetime.datetime(now.year, now.month, now.day, 5, 35)
        result = clock.time_parse("5:35")
        self.assertEqual(result, expect)
    def test_hour_minute_m(self):
        now = datetime.date.today()
        expect = datetime.datetime(now.year, now.month, now.day, 5, 35)
        result = clock.time_parse("5:35m")
        self.assertEqual(result, expect)
    def test_hour_minute_second(self):
        now = datetime.date.today()
        expect = datetime.datetime(now.year, now.month, now.day, 5, 35, 12)
        result = clock.time_parse("5:35:12")
        self.assertEqual(result, expect)
    def test_hour_minute_second(self):
        now = datetime.date.today()
        expect = datetime.datetime(now.year, now.month, now.day, 5, 35, 12)
        result = clock.time_parse("5:35:12s")
        self.assertEqual(result, expect)
    def test_near_iso(self):
        expect = datetime.datetime(2015, 12, 7, 9, 8, 7)
        result = clock.time_parse("2015-12-07T09:08:07")
        self.assertEqual(result, expect)
    def test_2digit_hour(self):
        now = datetime.date.today()
        expect = datetime.datetime(now.year, now.month, now.day, 5, 35)
        result = clock.time_parse("05:35")
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
