def achar_nome(nome):
    with open(f'nomes.txt', 'r') as arq:
        nomes = [linha.strip().split(',') for linha in arq.readlines()]

    for time in nomes:
        sigla, nome_time = time
        if nome == sigla:
            return nome_time
    return 'Erro'


def todos_nome():
    with open(f'nomes.txt', 'r') as arq:
        nomes = [linha.strip().split(',') for linha in arq.readlines()]

    for time in nomes:
        sigla, nome_time = time
        print(achar_nome(sigla))