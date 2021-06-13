import csv

def find_start_substring_credit_card(lista, parametro='303'):
    pessoas = []
    for p in lista:
        if p['credit_card'].startwith(parametro):
            pessoas.append(p)
    return pessoas

def find_substring_credit_card(lista, parametro='322'):
    pessoas = []
    for p in lista:
        if parametro in p['credit_card']:
            pessoas.append(p)
    return pessoas


def carregar_arquivo(path):

    local_list = []
    with open(path, "r") as csvfile:
        csv_reader =  csv.DictReader(csvfile)
        for line in csv_reader:
            local_list.append(line)
    return local_list

if __name__ == "__main__":
    path  = 'C:\Users\jacky\OneDrive\Área de Trabalho\NappAcademy\Semana 3\usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_start_substring_credit_card(lista))
    print(find_substring_credit_card(lista))