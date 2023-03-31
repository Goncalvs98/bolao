from gerar_palpites import ler_arquivo, ler_palpite


def resultados():
    texto = ''
    planejados = ler_arquivo('planejados')

    for jogo in planejados:
        time_casa, time_visitante = jogo

        palp_c, palp_v = ler_palpite()

        texto += f'{time_casa} {palp_c} {palp_v} {time_visitante}\n'

    with open('resultados.txt', 'w') as arquivo_resultados:
        arquivo_resultados.write(texto)


resultados()
