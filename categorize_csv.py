import csv, requests, json, time
from post import categorize_req
from manage_files import *


def categorize():
    mensagens = csv.DictReader(inicial_csv)
    
    count = 1
    count_tt = 1
    count_ct = 0
    count_nc = 0
    count_ex = 0

    print("text,intent,acuracy")
    categorized_messages.write("text,intent,acuracy\n")
    exceptions.write(f'text,\n')
    report.write(f'####Relatórios\n\n')

    for mensagem in mensagens:
        try:
            time.sleep(1)

            url = 'https://nlp.bothub.it/parse/'
            texto = mensagem["text"]
            data = {
                'language': 'pt_br',
                'text': texto
            } 
            headers = {'Authorization': 'Bearer 99025c09-deb9-4ce8-91e8-8f5d5950c04b'}

            resposta = categorize_req(url, headers, data)
            acuracia = resposta[1]
            intent = resposta[0]

            if (acuracia > 0):
                    print(f"{count_tt}- {texto},{intent},{acuracia:.1f}%")
                    categorized_messages.write(f"{texto},{intent},{acuracia:.1f}%\n")
                    count_ct += 1
            else:
                count_nc += 1
                print(f'{count_tt}- não foi categorizado {count_nc} requests')

        except:
            count_ex += 1
            print(f'{count_tt}- cairam em exeção {count_ex} requests')
            exceptions.write(f'{texto},\n')
        
        count += 1
        count_tt += 1

        if (count >= 400):
            time.sleep(15)
            count = 0
            continue

    report.write(f'nº de frase categorizadas: {count_ct}\n')
    report.write(f'nº de frase não categorizadas: {count_nc}\n')
    report.write(f'nº de frase não tratadas: {count_ex}\n\n')
    report.write(f'Total de frase categorizadas: {count_tt}\n')
    
    categorized_messages.close()
    inicial_csv.close()
    report.close()
    exceptions.close()

