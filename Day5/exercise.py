# Declare an empty list
empty_list = []

# Declare a list with more than 5 elements
more_than_5 = [1, 2, 3, 4, 5, 6]

# Find the length of the list
length = len(more_than_5)

# Get the first, middle, and last element
first_element = more_than_5[0]
middle_element = more_than_5[length // 2]
last_element = more_than_5[-1]

# Declare a list with mixed data types
mixed_data_types = ['Your Name', your_age, your_height, 'Your Marital Status', 'Your Address']

# Declare a list of IT companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print(it_companies)

# Print the number of companies in the list
num_companies = len(it_companies)
print(num_companies)

# Print the first, second, and last company
print(it_companies[0])
print(it_companies[1])
print(it_companies[-1])

# Modify one of the companies
it_companies[3] = 'New Apple'

# Add an IT company
it_companies.append('Netflix')

# Insert an IT company in the middle
it_companies.insert(4, 'Samsung')

# Change to uppercase (excluding IBM)
it_companies = [company.upper() if company != 'IBM' else company for company in it_companies]

# Join with the string '#; '
it_companies_string = '#; '.join(it_companies)

# Check if a certain company exists
company_exists = 'Microsoft' in it_companies

# Sort the list
it_companies.sort()

# Reverse the list in descending order
it_companies.reverse()

# Slice the first 3 companies
it_companies[:3]

# Slice the last 3 companies
it_companies[-3:]

# Remove intermediate IT company(s)
it_companies.pop(4)  # Remove the company at index 4

# Remove the first IT company
it_companies.pop(0)

# Remove intermediate IT company(s)
it_companies.pop(3)  # Remove the company at index 3

# Remove the last IT company
it_companies.pop(-1)

# Remove all IT companies
it_companies.clear()

# Join lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the minimum and maximum age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Add min_age and max_age back to the list
ages.extend([min_age, max_age])

# Find the median age
median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2

# Find the average age
average_age = sum(ages) / len(ages)

# Find the age range
age_range = max_age - min_age

# Compare (min. - average) and (max. - average)
comparison1 = abs(min_age - average_age)
comparison2 = abs(max_age - average_age)

# Find the middle country(s) in the list of countries
countries = ['China', 'Russia', 'United States', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries[len(countries) // 2]

# Split the list of countries into two equal lists
if len(countries) % 2 == 0:
    half1 = countries[:len(countries) // 2]
    half2 = countries[len(countries) // 2:]
else:
    half1 = countries[:len(countries) // 2 + 1]
    half2 = countries[len(countries) // 2 + 1:]

# Unpack the first three countries and the rest as split countries
first_country, second_country, third_country, *rest = countries
