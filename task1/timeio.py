import re
import sys
from pprint import pprint

from exceptions import ValidateError


def validate(string):
    ''' Validates string '''
    if not string:
        raise ValidateError("String is empty.")
    patterns = (
        r'^(\d*)([s]?)$',
        r'^(\d*|\d+\.\d+)([mhd]{1})$',
    )
    for pattern in patterns:
        result = re.match(pattern, string)
        if result:
            return result
    raise ValidateError("String '{}' is invalid.".format(string))


def to_seconds(match_result):
    ''' Returns seconds '''
    multipliers = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}
    digital_unit = match_result.group(1) or 1
    time_unit = match_result.group(2)
    if time_unit:
        return round(float(digital_unit)) * multipliers[time_unit]
    return int(digital_unit)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = """Usage: python timeio.py <timestring>
        Correct time units are:
            'd' - for days,
            'h' - for hours,
            'm' - for minutes,
            's' - for seconds(default value)

        Examples:
            python timeio.py 10m
            python timeio.py 12
            python timeio.py s
            """
        print(usage)
        sys.exit(1)
    timestring = sys.argv[1]
    print('String value: {}'.format(timestring))
    validated = validate(timestring)
    if validated:
        print('Seconds from string value: {}'.format(to_seconds(validated)))
