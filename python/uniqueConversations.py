import json

# Load the JSON data from conversations.json using the correct encoding
with open('../json/conversations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a set to store unique conversation IDs
unique_conversations = set()

# Iterate through conversations and add their IDs to the set
for conversation in data['conversations']:
    unique_conversations.add(conversation['id'])

# Count the number of unique conversations
num_unique_conversations = len(unique_conversations)

print(f"Number of unique conversations: {num_unique_conversations}")
