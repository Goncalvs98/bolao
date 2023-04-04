import PySimpleGUI as sg

from Pages.palpite import palpites_page
from Pages.resultado import resultado_page


def rodada_page(page):
    sg.theme('DarkTeal2')
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
            try:
                if page == 'Palpites':
                    palpites_page(values['rod'])
                if page == 'Resultados':
                    resultado_page(values['rod'])
            except Exception as e:
                sg.popup(e)
            break

    window.close()