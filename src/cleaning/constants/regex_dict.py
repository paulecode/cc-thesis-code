import re

no_regex = re.compile(r'\s?\bno\s?(\d+)')
opus_regex = re.compile(r'\s?\bop(?:us)?\s?(\d+)')
s_regex = re.compile(r'\s?\bs\s?(\d+)')
d_regex = re.compile(r'\s?\bd\s?(\d+)')
bwv_regex = re.compile(r'\s?\bbwv\s?(\d+)')
quoted_regex = re.compile(r'"([^"]*)"(?!.*")')
key_regex = re.compile(r'\s?\b(?:in\s+)?([a-g]\s+(?:(?:flat|sharp)(?:\s+(?:minor|major))?|minor|major))\b')

regex_dict = {
    no_regex: 'no_number',
    opus_regex: 'opus_number',
    s_regex: 's_number',
    d_regex: 'd_number',
    quoted_regex: 'quoted_title',
    key_regex: 'key',
    bwv_regex: 'bwv'
}
