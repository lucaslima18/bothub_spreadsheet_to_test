import csv, json

#open csv files
inicial_csv = open('csv/mensagens_susana.csv')
categorized_messages = open('csv/susana.csv', 'w')
exceptions = open('csv/exceptions.csv', 'w')
report = open('csv/relatorios.md', 'w')

#open json files
with open('json/intents.json') as j:
    intents_json = json.load(j)
