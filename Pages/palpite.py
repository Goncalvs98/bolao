import PySimpleGUI as sg
from Staple.achar_nome import achar_nome
from Staple import arq_staple as st


def jogo_page(user, timeCasa, timeFora):
    sg.theme('DarkTeal2')

    layout = [
        [sg.Text(achar_nome(timeCasa) + ': ', size = (20, 1)), sg.Input(key = 'golCasa')],
        [sg.Text(achar_nome(timeFora) + ': ', size = (20, 1)), sg.Input(key = 'golFora')],
        [sg.Button("Confirmar", size = (10, 1))]
    ]

    window = sg.Window(f"Bolao{user}", layout, size = (500, 250))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Confirmar':
            texto = f'{user} {timeCasa} {values["golCasa"]} {values["golFora"]} {timeFora}\n'

            with open('palpites.txt', 'a') as arq:
                arq.write(texto)

            sg.popup('Palpite Cadastrado com Sucesso')
            break


def palpites_page(rodada):
    sg.theme('DarkTeal2')

    usuarios = st.ler_arquivo('usuarios')
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

    layout = [
        [sg.Text('Nome', size = (10, 1)), sg.Combo(usuarios, key = 'user', size = (10, 1))],
        [sg.Text('Jogo', size = (10, 1)), sg.Combo(jogos[rodada], key = 'jog', size = (10, 1))],
        [sg.Button("Confirmar", size = (10, 1))]
    ]

    window = sg.Window("Bolao", layout, size = (300, 200), element_justification = 'center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Confirmar':
            try:
                palpites = st.ler_arquivo('palpites_feitos')
                feito = False
                for palpite in palpites:
                    nome, tmC, tmF = palpite
                    if nome == values['user'][0] and tmC == values['jog'][0] and tmF == values['jog'][1]:
                        feito = True

                if not feito:
                    jogo_page(values['user'][0], values['jog'][0], values['jog'][1])
                    text = f'{values["user"][0]} {values["jog"][0]} {values["jog"][1]}\n'
                    with open('palpites_feitos.txt', 'a') as arq:
                        arq.write(text)
                else:
                    st.mensagem('Jogo ja cadastrado')
            except Exception as e:
                st.mensagem(e)

    window.close()
