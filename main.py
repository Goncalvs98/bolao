import PySimpleGUI as sg
from achar_nome import achar_nome


def ler_arquivo(arquivo):
    with open(f'{arquivo}.txt', 'r') as arq:
        return [linha.strip().split(' ') for linha in arq.readlines()]


def mensagem(texto):
    sg.theme('Reddit')

    layout = [
        [sg.Text(f'{texto}', size = (30, 1), justification = 'center')],
        [sg.Button("Ok", size = (10, 1))]
    ]

    window = sg.Window("Bolao", layout, size = (200, 100), element_justification = 'center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            break

    window.close()


def jogo_page(user, timeCasa, timeFora):
    sg.theme('Reddit')

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
            texto = f'{user[0]} {timeCasa} {values["golCasa"]} {values["golFora"]} {timeFora}\n'

            with open('palpites.txt', 'a') as arq:
                arq.write(texto)
            mensagem('Palpite Cadastrado com Sucesso')
            break


def palpites_page(rodada):
    sg.theme('Reddit')

    usuarios = ler_arquivo('usuarios')
    jogos = {
        'Rodada 1': ler_arquivo('Rodadas\\rodada1'),
        'Rodada 2': ler_arquivo('Rodadas\\rodada2'),
        'Rodada 3': ler_arquivo('Rodadas\\rodada3'),
        'Rodada 4': ler_arquivo('Rodadas\\rodada4'),
        'Rodada 5': ler_arquivo('Rodadas\\rodada5'),
        'Rodada 6': ler_arquivo('Rodadas\\rodada6'),
        'Oitavas': ler_arquivo('Rodadas\\Oitavas'),
        'Quartas': ler_arquivo('Rodadas\\Quartas'),
        'Semi': ler_arquivo('Rodadas\\Semi'),
        'Final': ler_arquivo('Rodadas\\Final')
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
            palpites = ler_arquivo('palpites_feitos')
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
                mensagem('Jogo ja cadastrado')

    window.close()


def rodada_page():
    sg.theme('Reddit')
    rodadas = ['Rodada 1', 'Rodada 2', 'Rodada 3', 'Rodada 4', 'Rodada 5', 'Rodada 6', 'Oitavas', 'Quartas', 'Semi',
               'Final']

    layout = [
        [sg.Text('Rodada: '), sg.Combo(rodadas, key = 'rod')],
        [sg.Button("Confirmar", size = (10, 1))]
    ]

    window = sg.Window("Rodada", layout, size = (300, 100), element_justification = 'center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Confirmar':
            palpites_page(values['rod'])
            break

    window.close()


def main():
    texto = ''

    try:
        tb = ler_arquivo('tabela_final')
        for dado in tb:
            nome, pontos = dado
            texto += f'{nome}       | {pontos}\n'

    except:
        texto += 'Ainda nao comecou'

    sg.theme('Reddit')

    layout = [
        [sg.Text("Bolao Libertadores 2023\n")],
        [sg.Text(texto)],
        [sg.Button("Palpites", size = (10, 1))],
        [sg.Button("Resultados", size = (10, 1))],
        [sg.Button("Pontuacao", size = (10, 1))],
        [sg.Button("Tabela", size = (10, 1))]
    ]
    window = sg.Window("Bolao", layout, size = (300, 500), element_justification = 'center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Palpites':
            rodada_page()
        if event == 'Resultados':
            print('Resultados')
        if event == 'Pontuacao':
            print('Pontuacao')
        if event == 'Tabela':
            print('Tabela')

    window.close()


if __name__ == '__main__':
    main()
