import csv
from post import create_test


def test():
    print("responda as perguntas com sim ou nao!")
    categorized = open('csv/susana.csv')
    mensagens = csv.DictReader(categorized)
    for mensagem in mensagens:
        text = mensagem['text']
        intent = mensagem['intent']
        objeto = mensagem

        test_question = input(f"A frase \"{text}\" faz parte da intenção \"{intent}\"?\n")
        
        if(test_question == 'sim'):
            create_test(text, intent)
        else:
            intent = input("digite o nome da intenção:")
            create_test(text, intent)

