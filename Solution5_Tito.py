#!/usr/bin/python3

import re

joke_pattern = re.compile(r"Why did the (.*?)\? Because (.*)")

joke = input(
    "For example: Why did the chicken cross the road? Because chickens aren't allowed on a pedestrian bridge duh.")

match = joke_pattern.match(joke)

if match:
    print("First part:", match.group(1))
    print("Second part:", match.group(2))
else:
    print("Not a valid joke.")


"""
The 'match' function of the 're' module is used to match the regular expression 
against the input string (in this case, the joke). If a match is found, the 
groups are accessed using the group method of the match object, with the group 
number (1 or 2) passed as the argument.
"""
