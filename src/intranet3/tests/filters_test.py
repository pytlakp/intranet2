import unittest
import markdown
from intranet3.utils import filters
from datetime import datetime, time, date, timedelta


class FILTERSTest(unittest.TestCase):

    def test_slugify(self):

        text = 'text1 text2'
        result = filters.slugify(text)
        self.assertEqual(
            result, 'text1-text2'
        )

    def test_parse_user_email(self):

        email= 'example.user@exampledomain.com'
        result = filters.parse_user_email(email)
        self.assertEqual(
            result, 'example.user'
        )

    def test_parse_datetime_to_milisecond(self):

        import datetime
        times= datetime.datetime(2012, 1, 1)
        result = filters.parse_datetime_to_miliseconds(times)
        self.assertEqual(
            result, 1325372400000L
        )

    def test_timedelta_to_minutes(self):

        times= timedelta(days=1)
        result = filters.timedelta_to_minutes(times)
        self.assertEqual(
            result, 1440
        )

    def test_comma_number(self):

        number = 666.666
        result = filters.comma_number(number)
        self.assertEqual(
            result, '666,67'
        )

    def test_first_words(self):

        word = '@Lo@##$#$##rem Ipsum is simply dummy text of the printing and typesetting industry.'
        result = filters.first_words(word, characters=5)
        self.assertEqual(
            result, 'Lo re ...'
        )

    def test_is_true(self):

        val = (True, 1, 1.0, '1', 'True', 'true', 't')
        for a in val:
            result = filters.is_true(a)
            self.assertEqual(
                result, True
            )

    def test_false(self):

        val = (True, 1, 1.0, '1', 'True', 'true', 't')
        for a in val:
            result = filters.is_false(a)
            self.assertEqual(
                result, False
            )

    def test_int_or_float_int(self):

        val = 22
        result = filters.int_or_float(val)
        self.assertEqual(
            result, '22'
        )

    def test_int_or_float_float(self):
        val= 1.1
        result = filters.int_or_float(val)
        self.assertEqual(
            result, '1.1'
        )

    def test_initials_name(self):

        word = 'Andrzej Kowalski'
        result = filters.initials(word)
        self.assertEqual(
            result, 'A.K'
        )

    def test_initials_email(self):

        word = 'andrzej.kowalski@gmail.com'
        result = filters.initials(word)
        self.assertEqual(
            result, 'A.K'
        )

    def test_tojson(self):

        data = [
            (1, 'name', 'last_name')
        ]

        result = filters.tojson(data)
        self.assertEqual(
            result, '[[1, "name", "last_name"]]'
        )

    def test_markdown_filter(self):

        val = "**example**"
        result = filters.markdown_filter(val)
        self.assertEqual(
            result, '<p><strong>example</strong></p>'
        )

    def test_do_dictsort(self):

        data = {"name": "Andrzej",
                "last_name": "Plusk",
                "password": "P@$sW0rd",
                "bank_account": "PKO" ,
                "key_id": 666,
                }

        result = filters.do_dictsort(data)
        self.assertEqual(
            result, [('bank_account', 'PKO'), ('key_id', 666), ('last_name', 'Plusk'), ('name', 'Andrzej'), ('password',
                                                                                                            'P@$sW0rd')]
        )


