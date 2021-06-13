import csv
import json

def converter_url(url):
    url = url.replace("'","")
    url = url.replace("[","")
    url = url.replace("]","")
    url = url.replace(" ","")
    url = url.replace(",")
    return url

def carregar_dicionario_websites(path):

    local_list = {}
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            if line[0] == 'name':
                continue
            local_list[line[0]]=converter_url(line[4])
    return local_list

if __name__ == "__main__":
    path  = 'C:\Users\jacky\OneDrive\Área de Trabalho\NappAcademy\Semana 3\names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, ident=4)
    print(json_object)


