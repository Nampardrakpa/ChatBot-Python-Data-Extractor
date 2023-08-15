import json
import matplotlib.pyplot as plt

# Load the top_questions.json file
with open('../json/top_questions.json', 'r', encoding='utf-8') as file:
    top_questions_data = json.load(file)

# Extract questions and counts from the data
questions = [item['question'] for item in top_questions_data]
counts = [item['count'] for item in top_questions_data]

# Create a bar plot
plt.barh(questions, counts)
plt.xlabel('Number of Occurrences')
plt.ylabel('Questions')
plt.title('Top 10 Most Frequently Asked Questions')
plt.tight_layout()

# Save the plot as an image file
output_path = '../Output/top_questions_plot.png'
plt.savefig(output_path)

print(f"Plot saved as {output_path}")
