import json

# We have the python data
python_data = {"name": "zophie", "is_cat": True}

# We convert that data to json data
json_data = json.dumps(python_data)

# Print the json data
print(json_data)