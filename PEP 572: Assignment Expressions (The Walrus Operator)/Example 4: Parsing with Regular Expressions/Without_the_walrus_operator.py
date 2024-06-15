import re

pattern = re.compile(r'(\d+)')
match = pattern.search('The answer is 42')
if match:
    value = match.group(1)
    print(f'Found number: {value}')