import re
import sys

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
    digital_unit = round(float(match_result.group(1)))
    time_unit = match_result.group(2)
    if time_unit:
        return digital_unit * multipliers[time_unit]
    return digital_unit


if __name__ == '__main__':
    timestring = sys.argv[1] if len(sys.argv) > 1 else ''
    validated = validate(timestring)
    if validated:
        print(to_seconds(validated))
