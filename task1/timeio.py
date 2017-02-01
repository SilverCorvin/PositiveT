"""
This script converts timestring to seconds

Examples:
    $ python timeio.py 10m
    $ python timeio.py 12
    $ python timeio.py s
"""

import re
import sys

from exceptions import ValidateError

__author__ = 'Ivan Povalyaev'
__version__ = 0.1


def get_validated_timedict(string):
    """
    Validates string

    Args:
        string (str): Timestring like parameter

    Returns:
        dict:
            {
                'digital_unit': a digital part of string or 1
                'time_unit': a time part of string, e.g. 'd', 'h', 'm', 's'
            }
    Raises:
        ValidateError: If string is empty or is invalid
    """
    if not string:
        raise ValidateError("String is empty.")
    patterns = (
        r'^(\d*)([s]?)$',
        r'^(\d*|\d+\.\d+)([mhd]{1})$',
    )
    for pattern in patterns:
        result = re.match(pattern, string)
        if result:
            digital_unit = result.group(1) or None
            time_unit = result.group(2) or None
            return {'digital_unit': digital_unit, 'time_unit': time_unit}
    raise ValidateError("String '{}' is invalid.".format(string))


def to_seconds(**kwargs):
    """
    Converts dict to seconds

    Args:
        kwargs (dict):
            {
                'digital_unit': a digital part of string or 1
                'time_unit': a time part of string, e.g. 'd', 'h', 'm', 's'
            }
    Returns:
        int: Value in seconds
    """
    multipliers = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}
    digital_unit = kwargs.get('digital_unit') or 1
    time_unit = kwargs.get('time_unit')
    if time_unit:
        return round(float(digital_unit)) * multipliers[time_unit]
    return int(digital_unit)


def _main():
    """
    Main script function
    """
    if len(sys.argv) != 2:
        print(sys.modules[__name__].__doc__)
        sys.exit(1)
    timestring = sys.argv[1]
    print('String value: {}'.format(timestring))
    validated = get_validated_timedict(timestring)
    if validated:
        print('Seconds from string value: {}'.format(to_seconds(**validated)))


if __name__ == '__main__':
    _main()
