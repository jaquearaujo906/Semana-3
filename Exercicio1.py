import csv
from os import path

def find_substring_credit_card(lista, parametro='322'):
    pessoa = []
    lista_nomes = []

    # p = parametro
    for p in lista:
        if len(p[2]) == 16 and parametro in p[2]:
            pessoa.append(p)
            # print(pessoa[0])
    for registro in pessoa:
        lista_nomes.append(registro)
    return lista_nomes

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
    # print(lista[1][1])
    print(find_substring_credit_card(lista))
    print(find_substring_credit_card(lista, '222'))