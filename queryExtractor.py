import json
import os

# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the conversations.json file in the json directory
conversations_file_path = os.path.join(current_dir, '..', 'json', 'conversations.json')

# Load the JSON data from conversations.json using the correct encoding
with open(conversations_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "content" field from messages where role is "user"
user_contents = []
for conversation in data['conversations']:
    for message in conversation['messages']:
        if message['role'] == 'user':
            user_contents.append(message['content'])

# Create a dictionary to store the extracted user content
result = {
    'user_contents': user_contents
}

# Specify the path to the extracted_user_content.json file in the json directory
output_file_path = os.path.join(current_dir, '..', 'json', 'extracted_user_content.json')

# Write the extracted user content to a new JSON file in the json directory
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)

print("Extracted user content has been saved to 'extracted_user_content.json'")
