from Staple import arq_staple as st


def tabela_page():

    with open(f'pontuacao.csv', 'r') as arq:
        pontuacao = [linha.strip().split(',') for linha in arq.readlines()]

    usuarios = st.ler_arquivo('usuarios')
    texto = ''

    for usuario in usuarios:
        nome_user = usuario[0]
        sum = 0

        for pontos in pontuacao:
            nome, ponto = pontos

            if nome == nome_user:
                sum += int(ponto)

        texto += f'{nome_user} {sum}\n'

    with open('tabela_final.txt', 'w') as tabela_final:
        tabela_final.write(texto)
