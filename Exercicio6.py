import csv
from os import path

def find_start_substring_credit_card(lista, *paramether):

    pessoas = []
    for p in lista:
        for parametro in paramether:
            if parametro in p[2]:
                pessoas.append(p)
    return
            

def carregar_arquivo(path):

    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list

if __name__ == "__main__":
    path  = 'C:\Users\jacky\OneDrive\Área de Trabalho\NappAcademy\Semana 3\usernames.csv'
    lista = []
    list  = carregar_arquivo(path)
    print(find_start_substring_credit_card(lista))
    print(find_start_substring_credit_card(lista, '222', '223'))
    print(find_start_substring_credit_card(lista, '222', '223', '224'))
