def pergunta(tipo):
    res = input(f'Time {tipo}: ')
    if res >= 0:
        return res
    return pergunta(tipo)


def ler_palpite():
    a = pergunta('da Casa')
    b = pergunta('Visitante')
    return a, b


def ler_arquivo(arquivo):
    with open(f'{arquivo}.txt', 'r') as arq:
        return [linha.strip().split(' ') for linha in arq.readlines()]


def palpites():
    planejados = ler_arquivo('planejados')

    usuarios = ler_arquivo('usuarios')

    for jogo in planejados:
        time_casa, time_visitante = jogo

        for usuario in usuarios:
            nome = usuario[0]
            print(f'\n{nome} seu palpite para {time_casa} vs {time_visitante}')
            palp_c, palp_v = ler_palpite()
            texto = f'{nome} {time_casa} {palp_c} {palp_v} {time_visitante}\n'
            with open('palpites.txt', 'a') as arquivo_palpites:
                arquivo_palpites.write(texto)
