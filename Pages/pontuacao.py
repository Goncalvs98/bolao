import csv
from Staple import arq_staple as st


def pontuacao_page():
    palpites = st.ler_arquivo('palpites')
    resultados = st.ler_arquivo('resultados')

    # inicialização da tabela de pontos, resultados e vencedores dos usuários
    result = {palpite[0]: 0 for palpite in palpites}
    venced = {palpite[0]: 0 for palpite in palpites}
    pontos = {palpite[0]: 0 for palpite in palpites}

    # atualização da tabela de pontos dos usuários de acordo com os resultados dos jogos
    for resultado in resultados:
        time_casa, gols_casa, gols_visitante, time_visitante = resultado

        print('Jogo', time_casa, gols_casa, 'vs', gols_visitante, time_visitante)

        for palpite in palpites:
            usuario, time_casa_p, palpite_casa, palpite_visitante, time_visitante_p = palpite

            if time_casa_p == time_casa and time_visitante_p == time_visitante:

                print(usuario, palpite_casa, palpite_visitante)

                if gols_casa == palpite_casa and gols_visitante == palpite_visitante:
                    pontos[usuario] += 3
                    result[usuario] += 1

                    print(usuario, 'Acertou exato!')

                elif (gols_casa > gols_visitante and palpite_casa > palpite_visitante) \
                        or (gols_casa < gols_visitante and palpite_casa < palpite_visitante) \
                        or (gols_casa == gols_visitante and palpite_casa == palpite_visitante):
                    pontos[usuario] += 1
                    venced[usuario] += 1

                    print(usuario, 'Acertou')

    # salvando a tabela de pontos dos usuários em um arquivo .csv
    with open('pontuacao.csv', 'a', newline = '') as arquivo_pontuacao:
        writer = csv.writer(arquivo_pontuacao)
        writer.writerow(['Usuario', 'Pontos'])
        for usuario, pontos_usuario in pontos.items():
            writer.writerow([usuario, pontos_usuario])

    st.mensagem('Pontuacao Gerada')
