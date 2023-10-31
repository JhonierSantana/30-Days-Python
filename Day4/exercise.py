# concat string
string1 = 'Thirty'
string2 = 'Days'
string3 = "Of"
string4 = 'Python'
result = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(result)

string5 = 'Coding'
string6 = 'For'
string7 = "All"
result1 = string5 + ' ' + string6 + ' ' + string7
print(result1)

# Declare a varibale
company = "Coding For All"
print(company)

# length of the string
length = len(company)
print(length)

# Change uppercase
uppercase = company.upper()
print(uppercase)

# Change Lowercase
lowercase = company.lower()
print(lowercase)

# format the string
capitalized = company.capitalize()
title_case = company.title()
swap_case = company.swapcase()

print(capitalized, title_case, swap_case)

# Cut the first word
first_word = company.split()[0]

# if the check contain a word
contains_coding = 'Coding' in company

# Replace a word
replaced = company.replace('Coding', 'Python')

# Split the chain
split_result = company.split(' ')

# Divide by commas
comma_split = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')

# Character in the indexe
char_at_0 = company[0]

# Last index
last_index = len(company) - 1

# Character in index 10
char_at_10 = company[10]

# Create acronyms
acronym1 = ''.join(word[0] for word in "Python For Everyone".split())
acronym2 = ''.join(word[0] for word in "Coding For All".split())

# Find position of C and F
position_c = company.index('C')
position_f = company.index('F')

# Find position of last 'l'
last_l_index = company.rfind('l')

# Find position of 'because' in a sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_because = sentence.find('because')

# Find last 'because' position
last_because_index = sentence.rfind('because')

# Cutting the sentence 'because because because'
cut_because = sentence[position_because:position_because + 21]

# Check if it begins or ends with a substring
starts_with_coding = company.startswith('Coding')
ends_with_coding = company.endswith('coding')

# Eliminate blank spaces
trimmed = '   Coding For All      '.strip()

# Check if it is an identifier
identifier1 = '30DaysOfPython'.isidentifier()
identifier2 = 'thirty_days_of_python'.isidentifier()

# Join list with separator
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)

# Use newline escape sequence
sentences = "I am enjoying this challenge.\nI just wonder what is next."

# Use tab escape sequence
table = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"

# Format a string
radius = 10
area = 3.14 * radius ** 2
formatted_string = f"The area of a circle with radius {radius} is {area} meters square."

# Mathematical operations
addition = f"8 + 6 = {8 + 6}"
subtraction = f"8 - 6 = {8 - 6}"
multiplication = f"8 * 6 = {8 * 6}"
division = f"8 / 6 = {8 / 6:.2f}"
modulus = f"8 % 6 = {8 % 6}"
floor_division = f"8 // 6 = {8 // 6}"
exponentiation = f"8 ** 6 = {8 ** 6}"

# Print results
print(formatted_string)
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulus)
print(floor_division)
print(exponentiation)