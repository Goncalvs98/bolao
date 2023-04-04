import PySimpleGUI as sg


def ler_arquivo(arquivo):
    with open(f'{arquivo}.txt', 'r') as arq:
        return [linha.strip().split(' ') for linha in arq.readlines()]


def mensagem(texto):
    sg.theme('DarkTeal2')

    layout = [
        [sg.Text(f'{texto}', size = (50, 1), justification = 'center')],
        [sg.Button("Ok", size = (10, 1))]
    ]

    window = sg.Window("Bolao", layout, size = (300, 100), element_justification = 'center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            break

    window.close()

