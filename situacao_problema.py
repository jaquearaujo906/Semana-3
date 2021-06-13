import csv
path = 'usernames2.csv'


def buscar_cartao_expira_2030_v1(path):
    """
    Função abre o arquivo .csv, realiza a leitura via DictReader e
    retorna uma lista com os registros em que o cartão expira em 2030.

    Args:
        path (String): String com o nome do arquivo

    Returns:
        List: Lista de dicionários
    """
    lista_local = []
    lista_com_itens = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lista_local.append(line)
    for item in lista_local:
        try:
            if item.get('credit_card_expire').split('/')[1] == '30':
                lista_com_itens.append(item)
        except KeyError:
            pass
    return lista_com_itens


def buscar_cartao_expira_2030_v2(path):
    """
    Função abre o arquivo .csv, realiza a leitura via Reader e
    retorna uma lista com os registros em que o cartão expira em 2030.

     Args:
        path (String): String com o nome do arquivo

    Returns:
        List: Lista de listas
    """
    lista_local = []
    lista_com_itens = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            lista_local.append(line)
    for item in lista_local:
        try:
            if item[3].split('/')[1] == '30':
                lista_com_itens.append(item)
        except IndexError:
            pass
    return lista_com_itens


if __name__ == "__main__":
    lista1 = buscar_cartao_expira_2030_v1(path)
    lista2 = buscar_cartao_expira_2030_v2(path)


