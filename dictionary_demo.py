# Create a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Add a new key-value pair
my_dict['email'] = 'alice@example.com'

# Update an existing value
my_dict['age'] = 26

# Access a value using a key
print(my_dict['name'])  # Output: Alice

# Remove a key-value pair
del my_dict['city']

# Iterate over dictionary keys and values
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Check if a key exists in the dictionary
if 'email' in my_dict:
    print('Email key exists')

# Get the length of the dictionary
print(len(my_dict))  # Output: 3

# Use dictionary methods
print(my_dict.get('name'))  # Output: Alice
print(my_dict.keys())       # Output: dict_keys(['name', 'age', 'email'])
print(my_dict.values())     # Output: dict_values(['Alice', 26, 'alice@example.com'])
print(my_dict.items())      # Output: dict_items([('name', 'Alice'), ('age', 26), ('email', 'alice@example.com')])

# Pop a key-value pair
email = my_dict.pop('email')
print(email)  # Output: alice@example.com

# Clear the dictionary
my_dict.clear()
print(my_dict)  # Output: {}