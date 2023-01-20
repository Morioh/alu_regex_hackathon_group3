#!/usr/bin/python3

import re

# The song lyrics should match the pattern "[Verse X] some lyrics", where X is a number, and "some lyrics" can be any string of characters.
song_lyrics_pattern = re.compile(r"\[Verse [0-9]\] [ \w]+")

# Function to find movie titles in a string:


def find_lyrics(string):
    lyrics = song_lyrics_pattern.findall(string)
    if lyrics:
        return 'Lyric(s) found: ' + ', '.join(lyrics)
    else:
        return 'No lyric found.'


# Test the function:
print(find_lyrics('"[Verse 1] Never forget you"'))
print(find_lyrics("Beyonce's \"[Verse 3] Be with you\" is a thoughful."))
