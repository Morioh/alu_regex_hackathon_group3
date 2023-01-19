#!/usr/bin/python3

import re
from termcolor import colored


hex_color_pattern = re.compile(r"#\w{6,6}")


# code to ask the user to enter the episode titles
hex_color = input(f'''
    Enter a hex color that matchs the pattern "#XXXXXX" where X is any letter or digit: ''')

# checking to see a match 
hex_color_match = hex_color_pattern.match(hex_color)

if hex_color_match:
    text = colored(f"""\n
    Your hex code {hex_color} matches the pattern '#XXXXXX' provided
    \n""","green", attrs=["bold"])
    print(text)
else:
    test = colored('\nYour hex code doesnt match the pattern provided \n', "red",attrs=["blink","bold"])
    print(test)

