import csv
from os import path

def find_born_in(lista, birth_year='1992'):

    lista_nomes = list()
    for pessoa in lista:
        if len(pessoa[4]) == 10 and pessoa[4].startwith(birth_year):
            lista_nomes.append(pessoa)
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
    print(find_born_in(lista))
    print(find_born_in(lista, '1998'))