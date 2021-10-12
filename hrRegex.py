# Regex Template

Regex_Pattern = r""

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())



import re

pattern = re.compile(r'')

n = int(input())
for _ in range(n):
    sentence = input()
    if pattern.match(sentence):
        print(sentence)


########################################################################

#Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi.jkx , where each variable can be any single character except the newline.

regex_pattern = r"^[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}$"


#You have a test string xxXxxXxxxx. Your task is to match the pattern.  Here x denotes a digit character, and X denotes a non-digit character.

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"


#You have a test string . Your task is to match the pattern XXxXXxXX Here, x denotes whitespace characters, and X denotes non-white space characters.

Regex_Pattern = r"\S\S\s\S\S\s\S\S"


#You have a test string . Your task is to match the pattern Xxxxx. .  Here, x denotes a word character, and X denotes a digit.  S must start with a digit X and end with . symbol. S should be 6 characters long only.

Regex_Pattern = r"^\d\w\w\w\w\.$"


#You have a test string S. Your task is to match the pattern xxxXxxxxxxxxxxXxxx . Here x denotes any word character and X denotes any non-word character.

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"


#Write a RegEx to match a test string, S, under the following conditions:
#S should consist of only lowercase and uppercase letters (no numbers or symbols).
#S should end in s.

Regex_Pattern = r'^[a-zA-Z]*s$'


#You have a test String S. Your task is to write a regex which will match  with the following condition:
#S should have 3 or more consecutive repetitions of ok.2

Regex_Pattern = r'((ok){3})+'


#Given a test string, s, write a RegEx that matches s under the following conditions:
#s must start with Mr., Mrs., Ms., Dr. or Er..
#The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)*[a-zA-Z]+$'


#You have a test string S
#Your task is to write a regex that will match S with following conditions:
#S must be of length: 6
#First character: 1, 2 or 3
#Second character: 1, 2 or 0
#Third character: x, s or 0
#Fourth character: 3, 0 , A or a
#Fifth character: x, s or u
#Sixth character: . or ,

Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][\.,]$'


#You have a test string S
#Your task is to write a regex that will match S with the following conditions:
#S must be of length 6.
#First character should not be a digit (1,2,3,4,5,6,7,8,9,0).
#Second character should not be a lowercase vowel (a,e,i,o, or u ).
#Third character should not be b, c, D or F.
#Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
#Fifth character should not be a uppercase vowel (A,E,I,O or U ).
#Sixth character should not be a . or , symbol.

Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\r\n\t\f ][^AEIOU][^\.,]$'


#Write a RegEx that will match a string satisfying the following conditions:
#The string's length is -gte 5.
#The first character must be a lowercase English alphabetic character.
#The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
#The third character must not be a lowercase English alphabetic character.
#The fourth character must not be an uppercase English alphabetic character.
#The fifth character must be an uppercase English alphabetic character.

Regex_Pattern = r'^[a-z]{1}[1-9]{1}[^a-z]{1}[^A-Z]{1}[A-Z]{1}.*'


#You have a test String S
#Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).

Regex_Pattern = r"(?<![aeiouAEIOU])."


#You have a test string .
#Your task is to write a regex that will match  with the following conditions:
#S must be of length: 20
#1 character: lowercase letter.
#2 character: word character.
#3 character: whitespace character.
#4 character: non word character.
#5 character: digit.
#6 character: non digit.
#7 character: uppercase letter.
#8 character: letter (either lowercase or uppercase).
#9 character: vowel (a, e, i , o , u, A, E, I, O or U).
#10 character: non whitespace character.
#11 character: should be same as 1st character.
#12 character: should be same as 2nd character.
#13 character: should be same as 3rd character.
#14 character: should be same as 4th character.
#15 character: should be same as 5th character.
#16 character: should be same as 6th character.
#17 character: should be same as 7th character.
#18 character: should be same as 8th character.
#19 character: should be same as 9th character.
#20 character: should be same as 10th character.

Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)(\1)(\2)(\3)(\4)(\5)(\6)(\7)(\8)(\9)(\10)'


#You have a test string S
#Your task is to write a regex which will match S, with following condition(s):
#S consists of 8 digits.
#S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)

Regex_Pattern = r"^\d\d(\-?)\d\d(\-?)\d\d(\-?)\d\d(\1)(\2)(\3)(\4)$"


#You have a test string S.
#Your task is to write a regex that will match S using the following conditions:

#S must be of length equal to 45.
#The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
#The last 5 characters should consist of odd digits or whitespace characters.

Regex_Pattern = r'^[a-zA-Z20468]{40}[013579\s]{5}$'


#You have a test string S.
#Your task is to write a regex that will match S using the following conditions:
#S should begin with 1 or 2 digits.
#After that, S should have 3 or more letters (both lowercase and uppercase).
#Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'


#You have a test string S.
#Your task is to write a regex that will match S using the following conditions:
#S should begin with 2 or more digits.
#After that, S should have 0 or more lowercase letters.
#S should end with 0 or more uppercase letters

Regex_Pattern = r'^[\d]{2,}[a-z]*[A-Z]*$'


#You have a test string S.
#Your task is to write a regex that will match S using the following conditions:
#S should begin with 1 or more digits.
#After that, S should have 1 or more uppercase letters.
#S should end with 1 or more lowercase letters.

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'


#You have a test String S.
#Write a regex which can match all characters which are not immediately followed by that same character.

Regex_Pattern = r"(.)(?!(\1))"


#You have a test String S.
#Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

Regex_Pattern = r"(?<=[013579])\d"


#You have a test String .
#Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U).
#The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
#The matched word must start and end with a word boundary.

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'


#You have a test string S.
#Your task is to write a regex which will match S, with following condition(s):
#S consists of 8 digits.
#S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
#S string must have exactly one kind of separator.
#Separators must have integers on both sides.

Regex_Pattern = '^\d\d(?|(\-)|(:)|(\-\-\-)|(\.))\d\d\1\d\d\1\d\d$'


#You have a test string S.
#Your task is to write a regex which will match S, with following condition(s):
#S consists of tic or tac.
#tic should not be immediate neighbour of itself.
#The first tic must occur only when tac has appeared at least twice before.

Regex_Pattern = '^(\2tic|(tac))+$'


#You have a test string S.
#Write a regex that can match all occurrences of o followed immediately by oo in S.

Regex_Pattern = 'o(?=oo)'


#Given a sentence, s, write a RegEx to match the following criteria:
#The first character must be the letter H or h.
#The second character must be the letter I or i.
#The third character must be a single space (i.e.: \s).
#The fourth character must not be the letter D or d.
#Given n lines of sentences as input, print each sentence matching your RegEx on a new line.

Regex_Pattern = '^hi\s[^d]'


#Every submission at HackerRank has a field called language which indicates the programming language which a hacker used to code his solution.
#C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC
#Sometimes, error-prone API requests can have an invalid language field. Could you find out if a given submission has a valid language field or not?

import re
pattern = re.compile(r'^(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$')
for _ in range(int(input())):
    print('VALID' if re.match(pattern, input().split()[1]) else 'INVALID')


#We are trying to hack together a smart programming IDE. Help us build a feature which auto-detects the programming language, given the source code. There are only three languages which we are interested in "auto-detecting": Java, C and Python.
#We will provide you with links to a few short or medium size programs for Java, C and Python. In case you aren't familiar with some of these languages, these samples will help you make observations about the lexical structure and syntax of these programming languages. These sample programs are only for your manual inspection. You cannot read or access these sample-programs from the code you submit.
#After this, you will be provided with tests, where you are provided the source code for programs - or partial code snippets, but you do not know which language they are in. For each test, try to detect which language the source code is in.
#You might benefit from using regular expressions in trying to detect the lexical structure and syntax of the programs provided.

#!/usr/bin/env python3

import re
import sys

src = ''.join(sys.stdin.readlines())

if 'java' in src:
    print("Java")
elif '#include' in src:
    print("C")
else:
    print("Python")


#Print a single line containing all of the unique tag names found in the input. Your output tags should be semicolon-separated and ordered lexicographically (i.e.: alphabetically). Do not print the same tag name more than once.

#grep -oP '(?<=<)\w+' | sort -u | paste -s -d ';'


#You will be provided with N lines of what are possibly IP addresses. You need to detect if the text contained in each of the lines represents an (a)IPv4 address (b)IPv6 address or (c)None of these.

import re

V4_Pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$')

V6_Pattern = re.compile(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))')

n = int(input())
for _ in range(n):
    sentence = input()
    if re.search(V4_Pattern, sentence):
        print("IPv4")
    elif re.search(V6_Pattern, sentence):
        print("IPv6")
    else :
        print('Neither')


#In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:
#It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
#The first character must be immediately followed by one or more digits in the range 0 through 9.
#After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
#It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.
#Given n strings, determine which ones are valid alien usernames. If a string is a valid alien username, print VALID on a new line; otherwise, print INVALID.

import re

name = re.compile(r'^[_\.][0-9]+[a-zA-Z]*_?$')

n = int(input())
for _ in range(n):
    sentence = input()
    if re.search(name, sentence):
        print("VALID")
    else :
        print('INVALID')


#At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

#Starts with hackerrank
#Ends with hackerrank
#Start and ends with hackerrank

starts='^hackerrank.+'
ends='.+hackerrank$'
both='^(hackerrank).*\1?$'

import re

start = re.compile(r'^hackerrank.+')
ends = re.compile(r'.+hackerrank$')
start_and_end = re.compile(r'^(hackerrank).*\1?$')

n = int(input())
for _ in range(n):
    sentence = input()
    if re.search(start, sentence):
        print("1")
    elif re.search(ends, sentence):
        print("2")
    elif re.search(start_and_end, sentence):
        print("0")
    else :
        print("-1")