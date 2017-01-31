import unittest

from exceptions import ValidateError
from timeio import validate, to_seconds


class TestValidation(unittest.TestCase):

    def test_empty_string(self):
        string = ''
        with self.assertRaises(ValidateError):
            validate(string)

    def test_invalid_string(self):
        string = '10minutes'
        with self.assertRaises(ValidateError):
            validate(string)

    def test_invalid_string_with_float_seconds(self):
        string = '12.5s'
        with self.assertRaises(ValidateError):
            validate(string)

    def test_valid_string(self):
        string = '10.2m'
        try:
            validate(string)
        except ValidateError:
            self.fail("validate() raised ValidateError unexpectedly")


class TestConvertation(unittest.TestCase):

    def base_test(self, predicted, string):
        self.assertEqual(predicted, to_seconds(validate(string)))

    def test_days(self):
        string = '2d'
        self.base_test(172800, string)

    def test_hours(self):
        string = '4h'
        self.base_test(14400, string)

    def test_minutes(self):
        string = '26m'
        self.base_test(1560, string)

    def test_seconds(self):
        string = '10s'
        self.base_test(10, string)

    def test_seconds_without_digital_unit(self):
        string = 's'
        self.base_test(1, string)

    def test_seconds_without_time_unit(self):
        string = '12'
        self.base_test(12, string)


if __name__ == '__main__':
    unittest.main()
