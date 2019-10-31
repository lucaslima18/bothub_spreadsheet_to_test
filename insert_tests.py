import csv
from post import create_test
from manage_files import right_sentences, wrong_sentences


def test():
    print("responda as perguntas com sim ou nao!")
    categorized = open('csv/categorized_messages.csv')
    mensagens = csv.DictReader(categorized)
    right_sentences.write("text,intent,\n")
    wrong_sentences.write("text,intent,\n")

    for mensagem in mensagens:
        text = mensagem['text']
        intent = mensagem['intent']

        try:
            test_question = input(f"A frase \"{text}\" faz parte da intenção \"{intent}\"?\n")
            
            if(test_question == 'sim'):
                create_test(text, intent)
                right_sentences.write(f"{text},{intent},%\n")
            else:
                intent = input("digite o nome da intenção:")
                create_test(text, intent)
                wrong_sentences.write(f"{text},{intent},%\n")
        except:
            print(f'caiu em exeção')

