import csv, json

#open csv files
inicial_csv = open('csv/inicial_csv.csv')
categorized_messages = open('csv/categorized_messages.csv', 'w')
exceptions = open('csv/exceptions.csv', 'w')
report = open('csv/report.md', 'w')
right_sentences = open('csv/right_sentences.csv', 'w')
wrong_sentences = open('csv/wrong_sentences.csv', 'w')


#open json files
with open('json/intents.json') as j:
    intents_json = json.load(j)
