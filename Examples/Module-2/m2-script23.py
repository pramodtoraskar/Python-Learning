
# Define Tuple
# ----------------
dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual'}

# Accessing Values
# ----------------
print("dict_obj['Training']: ", dict_obj['Training'])
print("dict_obj['Mode']: ", dict_obj['Mode'])

# Updating Tuple
# ----------------
dict_obj['Attendees'] = 45
dict_obj['Location'] = 'Pune'

print("dict_obj['Attendees']: ", dict_obj['Attendees'])
print("dict_obj['Location']: ", dict_obj['Location'])

print(dict_obj)

# Delete
# ----------------
dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual', 'Location': 'Pune'}

# remove entry with key 'Location'
del dict_obj['Location']

# remove all entries in dict
dict_obj.clear()

# delete entire dictionary
del dict_obj
print("dict['Location']: ", dict_obj['Location'])

# More than one entry per key not allowed
dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Training': 'Basic Python Learning'}
print("dict_obj['Training']: ", dict_obj['Training'])

# Keys must be immutable
dict_obj = {['Training']: 'Python Learning', 'Attendees': 25, 'Mode': 'virtual'}
print("dict_obj['Training']: ", dict_obj['Name'])


# Length
# ----------------
print(len({'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual', 'Location': 'Pune'}))

# Printable representation
# ----------------
print(str({'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual', 'Location': 'Pune'}))

# Repetition
# ----------------
print(dict_obj.has("Attendees"))
