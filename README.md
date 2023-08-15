# Chatbot Data Extractor

This repository contains Python scripts to extract useful data extracted from a chatbot's conversations. The scripts process JSON data to extract user content, find the most frequently asked questions, and more.

## Getting Started

To use these scripts, follow the steps below:

1. Clone the repository to your local machine:

/
  git clone https://github.com/your-username/your-repo.git

## Requirements

This Program requires you to download some files inorder to make the most frequently asked questions work. To simplify and find the most frequently asked question regardless of grammar or spelling mistakes, you can use natural language processing libraries like spaCy and the fuzzy string matching library fuzzywuzzy.

pip install spacy fuzzywuzzy

python -m spacy download en_core_web_sm

pip install python-Levenshtein

With this three you should be good to go!

## Running the machine

Simply get your chatbase chat history extracted in json format and then rename it to conversations.json
You can delete my json files they are only there for demonstration

cd python

Now you can start using the given codes in the given order"

python conversationExtractor.py

python queryExtractor.py

python dateFinder.py

python mostFrequent.py


## File Structure

ChatBot-Python-Data-Extractor/

                              │
                              
                              ├── json/
                              
                              │   ├── conversations.json
                              
                              │   ├── extracted_user_content.json
                              
                              │   └── ...other JSON files...
                              
                              │
                              
                              └── python/
                              
                                  ├── conversationExtractor.py
                                  
                                  ├── mostFrequent.py
                                  
                                  ├── dateFinder.py
                                  
                                  └── requirements.txt
