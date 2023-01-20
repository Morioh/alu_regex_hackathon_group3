#!/usr/bin/python3

import re

# The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.
movie_titles_pattern = re.compile(r"[A-Z0-9][a-za-z0-9 ]+ \([0-9]{4}\)")

# Function to find movie titles in a string:


def find_titles(str):
    titles = movie_titles_pattern.findall(str)
    if titles:
        return 'Title(s) found: ' + ', '.join(titles)
    else:
        return 'No title found.'


# Test the function:
print(find_titles("I watched Avengers (2022) in 2023"))
print(find_titles("Regal was a bummer!"))
