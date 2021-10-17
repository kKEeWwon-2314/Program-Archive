"""
Two strategies to test whether or not a given sentence is
a palindrome. Demonstrates use of strings and operations on
str data types.
"""

def remove_spaces_punctuation(sentence):
    """
    This function accepts a str parameter (sentence) and creates
    a new str object containing only the alphabetic characters
    from the original. The "sanitized", space- and punctuation-free
    string is returned.
    """
    # a. create an empty string
    sanitized = ''
    # b. for each character in the sentence...
    for character in sentence:
        # add to new string if it's alphabetic
        if character.isalpha():
            sanitized += character

    return sanitized


def reverse_string(s):
    """
    This function accepts a str parameter (s) and creates a copy
    of the string written backwards. The reversed copy is returned
    as an str object.
    NOTE: Python has fancier ways to accomplish this if you're
          willing to brave some cryptic syntax.
    """
    # a. create an empty string
    backwards = ''
    # b. go through characters from back to front
    for i in range(len(s)-1, -1, -1):
        # add each character to my new string
        backwards += s[i]

    return backwards


def is_palindrome1(sentence):
    """
    Tests if the given str object (sentence) is a palindrome.
    Returns True if it is, False otherwise.
    """
    print('original:', sentence)

    # 1. take out all the punctuation and spaces
    sanitized_sentence = remove_spaces_punctuation(sentence)
    print('sanitized:', sanitized_sentence)
    
    # 2. de-capitalize the string
    lower_cased = sanitized_sentence.lower()
    print('de-capitalized:', lower_cased)
    
    # 3. reverse the sanitized string
    backwards = reverse_string(lower_cased)
    print('reversed:', backwards)
    
    # 4. read it, checking that the reversed one is same as original
    return lower_cased == backwards


def is_palindrome2(sentence):
    """
    Alternative strategy to test whether or not a given sentence
    is a palindrome.
    NOTE: Code implementation left as exercise for you!
    """
    pass    # placeholder; delete when implementation is finished!


test = 'A man, a plan, a canal, Panama!'
result = is_palindrome1(test)
print()
print(test)
if result:
    print('  is a palindrome.')
else:
    print('  is not a plaindrome.')
print()


test = 'Rats live on no evil star.'
result = is_palindrome1(test)
print()
print(test)
if result:
    print('  is a palindrome.')
else:
    print('  is not a plaindrome.')
print()

test = 'This sentence is not a palindrome.'
result = is_palindrome1(test)
print()
print(test)
if result:
    print('  is a palindrome.')
else:
    print('  is not a palindrome.')