#! utf-8
from intranet3 import memcache
import datetime
import unittest
import base64

from intranet3 import helpers
from intranet3 import memcache

class HELPERSTest(unittest.TestCase):

    def test_next_month(self):

        date = datetime.date(2013, 5, 1)
        result = helpers.next_month(date)
        self.assertEqual(
            result, datetime.date(2013, 6, 1)
        )

    def test_previous_month(self):

        date = datetime.date(2013, 5, 1)
        result = helpers.previous_month(date)
        self.assertEqual(
            result, datetime.date(2013, 4, 1)
        )

    def test_day_offset(self):

        n = 6
        date = datetime.date(2013, 5, 1)
        result = helpers.day_offset(date, n)
        self.assertEqual(
            result, datetime.date(2013, 5, 7)
         )

    def test_start_end_month(self):

        date = datetime.date(2013, 5, 1)
        result = helpers.start_end_month(date)
        self.assertEqual(
            result, (datetime.date(2013, 5, 1), datetime.date(2013, 5, 31))
        )

    def test_previous_day(self):

        date = datetime.date(2013, 5, 1)
        result = helpers.previous_day(date)
        self.assertEqual(
            result, datetime.date(2013, 4, 30)
        )

    def test_next_day(self):

        date = datetime.date(2013, 5, 1)
        result = helpers.next_day(date)
        self.assertEqual(
            result, datetime.date(2013, 5, 2)
        )

    def test_decoded_dict(self):

        dic = {'one':'2', 'two':'2'}
        result = helpers.decoded_dict(dic)
        self.assertEqual(
            result, {'two': '2', 'one': '2'}
        )

    def test_format_time(self):

        value = 4.50
        result = helpers.format_time(value)
        self.assertEqual(
            result, '4:30'
        )

    def test_image_resize(self):

        RESULT_HASH = 895427805
        IMAGE_AS_BASE64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QUWC' \
                          'wA3aw5ojAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAMSURBVAjXY/j//z8ABf4C/tzMWec' \
                          'AAAAASUVORK5CYII='
        result = helpers.image_resize(base64.b64decode(IMAGE_AS_BASE64), type=True)
        result = hash(result)

        self.assertEqual(
            result, RESULT_HASH
        )

    def test_get_mem_usage(self):

        result = helpers.get_mem_usage()
        self.assertTrue(isinstance(result, int))

