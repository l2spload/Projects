
def spin_words(sentence):
    split_sent = sentence.split(' ')
    if len(split_sent) <= 1:
        if len(sentence) >= 5:
            new_word = ''
            i = 1
            while i <= len(sentence):
                new_word += sentence[-i]
                i += 1
        else:
            return sentence
        return new_word
    else:
        new_sent = []
        for n in split_sent:
            if len(n) >= 5:
                new_word = ''
                i = 1
                while i <= len(n):
                    new_word += n[-i]
                    i += 1
                new_sent.append(new_word)
            else:
                new_sent.append(n)
        joined_sent = ' '.join(new_sent)
        return joined_sent

#----------------------------------------------#

def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#----------------------------------------------#

def is_isogram(string):
    new_str = ''
    low_str = string.lower()
    for n in low_str:
        if n not in new_str:
            new_str += n
    if low_str == new_str:
        return True
    else:
        return False

#----------------------------------------------#

def is_isogram(string):
    return len(string) == len(set(string.lower()))

#----------------------------------------------#

import math

def is_square(n):    
    if n > 0:
        if n % math.sqrt(n) == 0:
            return True
        else:
            return False
    elif n == 0:
        return True
    else:
        return False

#----------------------------------------------#

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
            return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names[2:]))

#-----------------------------------------------#

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

#-----------------------------------------------#

def narcissistic(value):
    narc_num = 0       
    for n in map(int, str(value)):
        narc_num += n ** len(str(value)) 
    if int(narc_num) == value:
        return True
    else:
        return False

#-----------------------------------------------#

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

#-----------------------------------------------#

