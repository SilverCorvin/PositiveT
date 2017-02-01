import unittest

from exceptions import ValidateError
from timeio import get_validated_timedict, to_seconds


class TestValidation(unittest.TestCase):

    def test_empty_string(self):
        string = ''
        with self.assertRaises(ValidateError):
            get_validated_timedict(string)

    def test_invalid_string(self):
        string = '10minutes'
        with self.assertRaises(ValidateError):
            get_validated_timedict(string)

    def test_invalid_string_with_float_seconds(self):
        string = '12.5s'
        with self.assertRaises(ValidateError):
            get_validated_timedict(string)

    def test_valid_string(self):
        string = '10.2m'
        try:
            get_validated_timedict(string)
        except ValidateError:
            self.fail(
                "get_validated_timedict() raised ValidateError unexpectedly")


class TestConvertation(unittest.TestCase):

    def test_days(self):
        timedict = {'digital_unit': '2', 'time_unit': 'd'}
        self.assertEqual(172800, to_seconds(**timedict))

    def test_hours(self):
        timedict = {'digital_unit': '4', 'time_unit': 'h'}
        self.assertEqual(14400, to_seconds(**timedict))

    def test_minutes(self):
        timedict = {'digital_unit': '26', 'time_unit': 'm'}
        self.assertEqual(1560, to_seconds(**timedict))

    def test_seconds(self):
        timedict = {'digital_unit': '10', 'time_unit': 's'}
        self.assertEqual(10, to_seconds(**timedict))

    def test_seconds_without_digital_unit(self):
        timedict = {'digital_unit': None, 'time_unit': 's'}
        self.assertEqual(1, to_seconds(**timedict))

    def test_seconds_without_time_unit(self):
        timedict = {'digital_unit': '12', 'time_unit': None}
        self.assertEqual(12, to_seconds(**timedict))


if __name__ == '__main__':
    unittest.main()
