import re

pattern = re.compile(r'(\d+)')
if match := pattern.search('The answer is 42'):
    print(f'Found number: {match.group(1)}')
