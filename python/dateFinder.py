import json
from collections import defaultdict
import os

# Get the full path to the JSON directory (assuming it's at the same level as the script)
json_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json')

# Load the JSON data from conversations.json using the correct encoding
with open(os.path.join(json_dir, 'conversations.json'), 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a dictionary to count questions asked on each date
questions_by_date = defaultdict(int)

# Iterate through conversations and messages to count questions by date
for conversation in data['conversations']:
    for message in conversation['messages']:
        if message['role'] == 'user' and '?' in message['content']:
            # Extract the date from the conversation's created_at field
            created_at = conversation.get('created_at', '')
            if created_at:
                date = created_at[:10]
                questions_by_date[date] += 1

# Convert the dictionary to a list of dictionaries for JSON format
result = [{'date': date, 'question_count': count} for date, count in questions_by_date.items()]

# Write the result to a new JSON file
output_file = os.path.join(json_dir, 'questions_by_date.json')
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)

print(f"Questions asked by date have been saved to '{output_file}'")
