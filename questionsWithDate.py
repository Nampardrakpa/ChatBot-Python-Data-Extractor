import json
import matplotlib.pyplot as plt
import os

# Load the JSON data from questions_by_date.json using the correct encoding
with open('../json/questions_by_date.json', 'r', encoding='utf-8') as file:
    top_questions_data = json.load(file)

# Extract dates and question counts from the data
dates = [entry['date'] for entry in top_questions_data]
question_counts = [entry['question_count'] for entry in top_questions_data]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(dates, question_counts, color='blue')
plt.xlabel('Date')
plt.ylabel('Number of Questions Asked')
plt.title('Number of Questions Asked by Date')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as a PNG file
output_path = '../Output/questions_by_date_plot.png'
plt.savefig(output_path)

print(f"Questions by date plot saved to '{output_path}'")
