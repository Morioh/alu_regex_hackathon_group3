# alu_regex_hackathon_group3

Regex Hackathon Questions and Solutions.

1. The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.

([A-Z0-9][a-za-z0-9 ]+) \(([0-9]{4})\) or \w+ \(\d{4}\)

2. The song lyrics should match the pattern "[Verse X] some lyrics", where X is a number, and "some lyrics" can be any string of characters.



3. The twitter handles should match the pattern "@username", where "username" can be any string of letters and digits.

@\w+

4. The ISBN numbers should match the pattern "ISBN xxx-x-xxx-xxxxx-x", where x is a digit.



5. The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, and the second part can be any string of characters.



6. The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.



7. The dates should match the pattern dd-MMM-yyyy, where dd is a two-digit day, MMM is a three-letter month abbreviation, and yyyy is a four-digit year.



8. The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.



9. The IP addresses should match the pattern "xxx.xxx.xxx.xxx" where x is a digit between 0 and 255.


