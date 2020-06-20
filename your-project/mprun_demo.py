import re

def permutation(input_text):

    #remove spaces and lowercase
    input_text = re.sub(' ', '', input_text).lower()

    #find unique characters
    unique_characters = set([letter for letter in input_text])

    #odd characters 
    odd_characters = [input_text.count(character) % 2 != 0 for character in unique_characters]


    #is palindrome 
    is_palindrome_permutation = sum(odd_characters) <=1

    print(f"unique characters are: {unique_characters}")
    print(f"characters that appear an odd number of times: {odd_characters}")
    print(f"Palindrome Permutation (if max one character appears an odd number of times): {is_palindrome_permutation}")
