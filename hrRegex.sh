#Given a sentence, s, write a RegEx to match the following criteria:
#The first character must be the letter H or h.
#The second character must be the letter I or i.
#The third character must be a single space (i.e.: \s).
#The fourth character must not be the letter D or d.
#Given n lines of sentences as input, print each sentence matching your RegEx on a new line.

grep -i '^hi\s[^d]'

#####################################################################################################

#We are trying to hack together a smart programming IDE. Help us build a feature which auto-detects the programming language, given the source code. There are only three languages which we are interested in "auto-detecting": Java, C and Python.
#We will provide you with links to a few short or medium size programs for Java, C and Python. In case you aren't familiar with some of these languages, these samples will help you make observations about the lexical structure and syntax of these programming languages. These sample programs are only for your manual inspection. You cannot read or access these sample-programs from the code you submit.
#After this, you will be provided with tests, where you are provided the source code for programs - or partial code snippets, but you do not know which language they are in. For each test, try to detect which language the source code is in.
#You might benefit from using regular expressions in trying to detect the lexical structure and syntax of the programs provided.

#!/bin/bash

content=$(cat)

if [[ $content =~ <regex> ]];
then
    echo ""
elif [[ $content =~ <regex> ]]; 
then
    echo ""
else
    echo ""20
fi

######################################################################################################################

#At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

#Starts with hackerrank
#Ends with hackerrank
#Start and ends with hackerrank

#!/bin/bash

sed -E \
  -e '1d' \
  -e "s/$starts/1/" \
  -e "s/$ends/2/" \
  -e "s/$both/0/" \
  -e '/1|2|0/! c\-1'



