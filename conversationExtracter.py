import json
import os

# Define the paths for input JSON and output JSON files
input_json_path = os.path.join('..', 'json', 'conversations.json')
output_json_path = os.path.join('..', 'json', 'extracted_content.json')

# Load the JSON data from input JSON file using the correct encoding
with open(input_json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "content" field from each message
contents = []
for conversation in data['conversations']:
    for message in conversation['messages']:
        contents.append(message['content'])

# Create a dictionary to store the extracted content
result = {
    'extracted_content': contents
}

# Write the extracted content to a new JSON file
with open(output_json_path, 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)

print("Extracted content has been saved to 'extracted_content.json'")
