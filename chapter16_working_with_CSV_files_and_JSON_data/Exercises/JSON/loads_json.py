import json

# We have the json data
string_of_json_data = '{"name": "zophie", "is_cat": true}'

# Convert the json data to python data
python_data = json.loads(string_of_json_data)

# Print the key name
print(python_data['name'])

# Print all python data
print(python_data)