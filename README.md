# alu_regex_hackathon_group3

Regex Hackathon Questions and Solutions.

1. The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.

[A-Za-z0-9 ]+ \([0-9]{4}\)

2. The song lyrics should match the pattern "[Verse X] some lyrics", where X is a number, and "some lyrics" can be any string of characters.

\[Verse [0-9]\] [ \w]+

3. The twitter handles should match the pattern "@username", where "username" can be any string of letters and digits.

@\w+

4. The ISBN numbers should match the pattern "ISBN xxx-x-xxx-xxxxx-x", where x is a digit.

ISBN \d{3}.\d.\d{3}.\d{5}.\d

5. The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, and the second part can be any string of characters.

Why did the (._?)\? Because (._)

6. The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.

\w+\s+\w*\s*S\d{2,2}E\d{2,2}:\s(\w+\s+)\*

7. The dates should match the pattern dd-MMM-yyyy, where dd is a two-digit day, MMM is a three-letter month abbreviation, and yyyy is a four-digit year.

[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}

8. The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.

#\w{6,6}

9. The IP addresses should match the pattern "xxx.xxx.xxx.xxx" where x is a digit between 0 and 255.

^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$

## In order to use the file on solution 6 and solution 8. you must install `python virtual env` and then install the `terminal color package`

in order to install the virtual env
just type
`python3 -m venv env`

and afterwards, ,activate it using
`source env/bin/activate` for those using linux

but in case you are windows, activate it using
`source env/scripts/activate`

and lastly, install the terminal colorizer,by running the command
`pip install termcolor`

after that you are good to go and you can run the file normally
