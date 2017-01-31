import re
import sys

from exceptions import ValidateError


def validate(string):
    ''' Validates string '''
    patterns = (
        r'^(\d*)([s]*)$',
        r'^(\d*|\d+\.\d+)([mhd]{1})$',
    )
    for pattern in patterns:
        result = re.match(pattern, string)
        if result:
            return result
    raise ValidateError("String '{}' doesn't match pattern.".format(string))


def to_seconds(match_result):
    ''' Returns seconds '''
    multipliers = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}
    if match_result.group(2):
        return round(float(match_result.group(1))) * multipliers[match_result.group(2)]
    return int(match_result.group(1))


if __name__ == '__main__':
    timestring = sys.argv[1] if len(sys.argv) > 1 else '60.5m'
    validated = validate(timestring)
    if validated:
        print(to_seconds(validated))
