import operator

import PySimpleGUI as sg

from Pages.pontuacao import pontuacao_page
from Pages.rodada import rodada_page
from Pages.tabela import tabela_page
from Staple import arq_staple as st


def main():
    texto = ['Nome', 'Pontos']

    try:
        tb = st.ler_arquivo('tabela_final')
    except Exception as e:
        texto = ['Ainda nao comecou', '2023']
        tb = [' ', 0]
        st.mensagem(e)

    sg.theme('DarkTeal2 ')

    layout = [
        [sg.Text("Bolao Libertadores 2023\n")],
        [sg.Table(
            values = tb,
            headings = texto,
            header_background_color = 'LightBlue1',
            auto_size_columns = True,
            hide_vertical_scroll = True,
            enable_click_events = True,
            enable_events = True,
            size = (20, 4),
            alternating_row_color = 'LightBlue4',
            key = '-TABLE-',
        )],
        [sg.Button("Palpites", size = (10, 1))],
        [sg.Button("Resultados", size = (10, 1))],
        [sg.Button("Pontuacao", size = (10, 1))],
        [sg.Button("Tabela", size = (10, 1))]
    ]
    window = sg.Window("Bolao Libertadores 2023", layout, size = (300, 500), element_justification = 'center')

    def sort_table(data, num_clicked):
        try:
            table_data = sorted(data, key = operator.itemgetter(num_clicked), reverse = True)
        except Exception as e:
            sg.popup('Error sorting table', 'Exception', e)

        return table_data

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Palpites':
            rodada_page(event)
        if event == 'Resultados':
            rodada_page(event)
        if event == 'Pontuacao':
            pontuacao_page()
        if event == 'Tabela':
            tabela_page()
            window['-TABLE-'].update(st.ler_arquivo('tabela_final'))
        if isinstance(event, tuple):
            if event[0] == '-TABLE-':
                if event[2][0] == -1 and event [2][1] != -1:
                    col_num_clicked = event[2][1]
                    new_table_data = sort_table(tb, col_num_clicked)
                    window['-TABLE-'].update(new_table_data)

    window.close()


if __name__ == '__main__':
    main()
