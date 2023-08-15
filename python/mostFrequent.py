import json
import os
from collections import Counter
import spacy
from fuzzywuzzy import fuzz

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Specify the path to the extracted_user_content.json file
json_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json')
json_file_path = os.path.join(json_dir, 'extracted_user_content.json')

# Load the extracted_user_content.json file
with open(json_file_path, 'r', encoding='utf-8') as file:
    user_contents = json.load(file)['user_contents']

# Preprocess and simplify questions
def preprocess_question(question):
    doc = nlp(question.lower())
    simplified = ' '.join([token.lemma_ for token in doc if token.is_alpha])
    return simplified

simplified_questions = [preprocess_question(question) for question in user_contents]

# Find the most frequently asked questions
most_common_questions = Counter(simplified_questions).most_common(10)

# Specify the path to the output file in the json directory
output_file = os.path.join(json_dir, 'top_questions.json')

# Convert the results to a JSON-friendly format
top_questions_json = [{"question": question, "count": count} for question, count in most_common_questions]

# Save the top questions and counts in a JSON file in the json directory
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(top_questions_json, outfile, ensure_ascii=False, indent=4)

print("Top 10 most asked questions saved to 'top_questions.json' in the json directory.")
