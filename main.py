#!/usr/bin/python3
import csv
from categorize_csv import categorize
from insert_tests import test

print("##### BOTHUB: CONVERSOR DE PLANILHAS PARA TESTE #####\n")

categorize_question = input("Suas planilha de frases já foi categorizada?(responda com sim ou nao)\n")

if(categorize_question == 'sim'):
    print('\n\n!NESTE CASO, VAMOS AO PRÓXIMO PASSO...\n')
else: 
    print('##### CATEGORIZANDO FRASES #####\n')
    print('!ISSO PODE DEMORAR UM POUCO, QUE TAL TOMAR UMA XÍCARA DE CAFÉ? ;)\n\n')
    categorize()
    print('\n\n!A CATEGORIZAÇÃO ACABOU, AGORA VAMOS AO PRÓXIMO PASSO...\n')

print('##### INSERINDO TESTES #####')
test()



