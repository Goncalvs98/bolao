import PySimpleGUI as sg
from Staple import arq_staple as st
from Staple.achar_nome import achar_nome


def resultado_page(rodada):
    sg.theme('DarkTeal2')
    layout = [[sg.Text(rodada)]]

    jogos = {
        'Rodada 1': st.ler_arquivo('Rodadas\\rodada1'),
        'Rodada 2': st.ler_arquivo('Rodadas\\rodada2'),
        'Rodada 3': st.ler_arquivo('Rodadas\\rodada3'),
        'Rodada 4': st.ler_arquivo('Rodadas\\rodada4'),
        'Rodada 5': st.ler_arquivo('Rodadas\\rodada5'),
        'Rodada 6': st.ler_arquivo('Rodadas\\rodada6'),
        'Oitavas': st.ler_arquivo('Rodadas\\Oitavas'),
        'Quartas': st.ler_arquivo('Rodadas\\Quartas'),
        'Semi': st.ler_arquivo('Rodadas\\Semi'),
        'Final': st.ler_arquivo('Rodadas\\Final')
    }
    jogos_rodada = jogos[rodada]

    for jogo in jogos_rodada:
        timeC, timeF = jogo
        layout.append([
            sg.Text(achar_nome(timeC), size = (20, 1), justification = 'right'),
            sg.Input(key = f'gol{timeC}', size = (10,1)),
            sg.Text('x'),
            sg.Input(key = f'gol{timeF}', size = (10,1)),
            sg.Text(achar_nome(timeF), size = (20, 1))
        ])

    layout.append([sg.Button("Confirmar", size = (10, 1))])

    window = sg.Window("Rodada", layout, size = (600, 500), element_justification = 'center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Confirmar':
            texto = ''
            for jogo in jogos_rodada:
                timeC, timeF = jogo

                golstimeC = f'gol{timeC}'
                golstimeF = f'gol{timeF}'

                texto += f'{timeC} {values[golstimeC]} {values[golstimeF]} {timeF}\n'

            with open('resultados.txt', 'w') as arq:
                arq.write(texto)
            st.mensagem('Resultados Cadastrados com Sucesso')
            break

    window.close()