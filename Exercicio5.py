import csv
from os import path

def find_born_in_month_and_gender(lista, paramether='03', gender='F'):

    pessoas = []
    for pessoa in lista:
        try:
            if paramether in pessoa[4].split("-")[1] and pessoa[5] == gender:
               pessoas.append(pessoa)
        except:
            continue
    return pessoas

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
    print(find_born_in_month_and_gender(lista))
    print(find_born_in_month_and_gender(lista, '01'))
    print(find_born_in_month_and_gender(lista, '01', 'M'))