import re

# validating regex
# https://www.debuggex.com/

# special characters
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)



# usage

# finditer retruns iterable regex match object that has match locations and matches themselves
text_to_search = "hi"

pattern = r"hi"

compiled_pattern = re.compile(pattern)
matches = compiled_pattern.finditer(text_to_search)

# getting locations and str from regex match object
for match in matches:
    print(match.start(), match.end(), match.group(0))


# useing group on matches
text_to_search = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = r"https?://(www\.)?([a-z0-9]+)(\.[A-Za-z0-9-.]+)"

compiled_pattern = re.compile(pattern)
matches = compiled_pattern.finditer(text_to_search)

for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))



# geting sub groups from matches
sub = compiled_pattern.sub(r"\2\3", text_to_search)

# retruns just the matches as string or if there are groups returns list of tuple that has matches
matches = compiled_pattern.findall(text_to_search)

# returns the first match or None (ONLY FOR BEGGING OF STRING)
match = compiled_pattern.match(text_to_search)

# returns the first match or None
match = compiled_pattern.search(text_to_search)

# ignorring case
compiled_pattern = re.compile(r"hi", re.IGNORECASE)
compiled_pattern = re.compile(r"hi", re.I)





# examples

# match only the word except (.-,)
text_to_search = " solution resolution solution. solution-a"
pattern = "\\b{0}\\b".format("solution")
 

# match phone numbers (Tr)
text_to_search = "05412222222 +905412222222"
pattern = r"0\d{3}\d{3}\d{2}\d{2}"
pattern = r"\+90\d{3}\d{3}\d{2}\d{2}"


# match emails
text_to_search = "hi_hello@gmail.edu hello123@somemail.com.tr"
pattern = r"[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


# match ip
text_to_search = "192.186.1.1"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# match date
text_to_search = "8/12/2020"
pattern = r"\d{1,2}/\d{1,2}/\d{4}"



# match urls
text_to_search = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
pattern = r"https?://(www\.)?[a-z0-9]+\.[A-Za-z0-9-.]+"


# other examples
text_to_search = "bat cat pat fat lat"
pattern = r"[^b]at"
text_to_search = """
Mr. Can 
Mr cat 
Ms  dog 
Mrs elephant
mr T
"""
pattern = r"[Mm](r|s|rs)\.?\s[A-Za-z]*"

