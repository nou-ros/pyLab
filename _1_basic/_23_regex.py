'''
Regular Expressions
Regular expressions (REs, or regexes, or regex patterns) are a powerful language for matching text patterns. Possible pattern examples for searches are, e.g., E-mail addresses or domain names. This article gives a basic introduction to regular expressions and shows how regular expressions work in Python. It will cover all the necessary concepts:

1) Methods to search for matches
2) Methods on a match object
3) Meta characters
4) More special sequences
5) Sets
6) Quantifier
7) Conditions
8) Grouping
9) Examples
10) Modification
11) Compilation flags

Regular expressions inside Python are made available through the re module:'''

import re

'''
Using regexes, you specify the rules for the set of possible strings that you want to match. Typically we first define our pattern that we want to search for, and use re.compile() on it. By default, our pattern is case sensitive.'''

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

# Note: It is recommended to use raw strings for the search:
## Use raw strings for the search pattern
a = '\tHello'
b = r'\tHello'
print(a)
print(b)

'''
Performing matches with compiled objects
Once we have our pattern, we can search for this pattern in the text / string that we want to look up.

match(): Determine if the RE matches at the beginning of the string.
search(): Scan through a string, looking for any location where this RE matches.
findall(): Find all substrings where the RE matches, and returns them as a list.
finditer(): Find all substrings where the RE matches, and returns them as an iterator.


Modification methods
We will cover these methods later:

split(): Returns a list where the string has been split at each match
sub(): Replaces one or many matches with a string'''

# finditer()
my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group()) # returns the string

print()
# findall()
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)

print()
# match
match = pattern.match(my_string)
print(match)
pattern = re.compile(r'abc')
match = pattern.match(my_string)
print(match)

print()
# search
match = pattern.search(my_string)
print(match)

'''
Note: Methods can also be used directly on the re module. It does not make that much of a difference, but some people prefer explicitely precompiling and binding the pattern to a reusable variable. (See https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile)'''

matches = re.finditer(r'abc', test_string)
for match in matches:
    print(match)

'''
Methods on a Match object
group(): Return the string matched by the RE
start(): Return the starting position of the match
end(): Return the ending position of the match
span(): Return a tuple containing the (start, end) positions of the match'''

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group()) # returns the substring that was matched by the RE

'''
Meta characters
Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with ) if we actually want to search for the char.

. Any character (except newline character) "he..o"
^ Starts with "^hello"
\$ Ends with "world\$"
* Zero or more occurrences "aix*"
+ One or more occurrences "aix+"
{ } Exactly the specified number of occurrences "al{2}"
[] A set of characters "[a-m]"
\ Signals a special sequence (can also be used to escape special characters) "\d"
| Either or "falls|stays"
( ) Capture and group
'''
test_string = 'python-engineer.com'
pattern = re.compile(r'\.')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

'''
More Metacharacters / Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\d :Matches any decimal digit; this is equivalent to the class [0-9].
\D : Matches any non-digit character; this is equivalent to the class [^0-9].
\s : Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S : Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
\W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
\b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
\A Returns a match if the specified characters are at the beginning of the string "\AThe"
\Z Returns a match if the specified characters are at the end of the string "Spain\Z"
'''

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\d')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\s')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    
print()
pattern = re.compile(r'\w')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    
print()
pattern = re.compile(r'\bhey')
matches = pattern.finditer('heyho hohey') # ho-hey, ho\nhey are matches!
for match in matches:
    print(match)
    
print()
pattern = re.compile(r'\Ahello')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    
print()
pattern = re.compile(r'123_\Z')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

'''
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning. Append multiple conditions back-to back, e.g. [aA-Z].
A ^ (caret) inside a set negates the expression.
A - (dash) in a set specifies a range if it is in between, otherwise the dash itself.

Examples:

[arn] Returns a match where one of the specified characters (a, r, or n) are present
[a-n] Returns a match for any lower case character, alphabetically between a and n
[^arn] Returns a match for any character EXCEPT a, r, and n
[0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9] Returns a match for any digit between 0 and 9
[0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case
'''
test_string = 'hello 123_'
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

print('all dates with a character in between')
pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between')
pattern = re.compile(r'\d\d\d\d[-.]\d\d[-.]\d\d') #  no escape for the . here in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)

print()
print('only dates with - or . in between in May or June')
pattern = re.compile(r'\d\d\d\d[-.]0[56][-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
    
# a dash in a character set specifies a range if it is in between, otherwise the dash itself
print()
print('only dates with - or . in between in May, June, July')
pattern = re.compile(r'\d\d\d\d[-.]0[5-7][-.]\d\d') #  no escape for the . here in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)

'''
Quantifier
* : 0 or more
+ : 1 or more
? : 0 or 1, used when a character can be optional
{4} : exact number
{4,6} : range numbers (min, max)'''

my_string = 'hello_123'
pattern = re.compile(r'\d*')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\d+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    
print()
my_string = 'hello_1_2-3'
pattern = re.compile(r'_?\d')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    
print()
my_string = '2020-04-01'
pattern = re.compile(r'\d{4}') # or if you need a range r'\d{3,5}'
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''
pattern = re.compile(r'\d{4}.\d{2}.\d{2}')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\d+.\d+.\d+')
matches = pattern.finditer(dates)
for match in matches:
    print(match)

'''Conditions
Use the | for either or condition.'''

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""
pattern = re.compile(r'Mr\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

'''
Grouping
( ) is used to group substrings in the matches.'''

emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.[a-zA-Z]+')
pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.(com|de)')
pattern = re.compile('([a-zA-Z1-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

'''
Modifying strings
split(): Split the string into a list, splitting it wherever the RE matches
sub(): Find all substrings where the RE matches, and replace them with a different string'''

my_string = 'abc123ABCDEF123abc'
pattern = re.compile(r'123') #  no escape for the . here in the set
matches = pattern.split(my_string)
print(matches)

my_string = "hello world, you are the best world"
pattern = re.compile(r'world')
subbed_string = pattern.sub(r'planet', my_string)
print(subbed_string)


urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    #print(match)
    print(match.group()) # 0
    #print(match.group(1))
    #print(match.group(2))
    print(match.group(3))
    
# substitute using back references to replace url + domain name
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

'''
Compilation Flags
ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S : Make . match any character, including newlines.
IGNORECASE, I : Do case-insensitive matches.
LOCALE, L : Do a locale-aware match.
MULTILINE, M : Multi-line matching, affecting ^ and $.
VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.'''

my_string = "Hello World"
pattern = re.compile(r'world', re.IGNORECASE) # No match without I flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

my_string = '''
hello
cool
Hello
'''
# line starts with ...
pattern = re.compile(r'^[a-z]', re.MULTILINE) # No match without M flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

'''
Further readings
https://docs.python.org/3/howto/regex.html
https://docs.python.org/3/library/re.html
https://developers.google.com/edu/python/regular-expressions'''
