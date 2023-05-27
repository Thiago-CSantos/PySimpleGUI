import PySimpleGUI as sg


def janela_TelaInicial():
    sg.theme('DarkBlue')

    srcImage = sg.Image('imgs/Logo with text for GitHub Top.png')
    # menu =  sg.Menu()

    layout = [
        [srcImage],
        [sg.Menu([['Pessoa', ['Cadastrar', 'Editar']], ['Ajuda', ['Sobre']]])]
    ]
    janela = sg.Window("Tela Inicial", layout, finalize=True)

    return janela


def cadastrar():
    layout = [
        [sg.Text("CADASTRO DE PESSOAS", justification='right')],

        [sg.Text('CPF:'), sg.Input(key='cpf'), sg.Text('Nome:'), sg.Input(key='nome')],
        [sg.Text('Endereço:'), sg.Input(key='endereco')],

        [sg.Text('Cidade:'), sg.Input(key='cidade'), sg.Text('Estado:'),
         sg.Combo(['SP', 'RJ', 'MG', 'ES'], key='estado')],

        [sg.Frame('Sexo', [[sg.Radio('Masculino', group_id='sexo', key='masculino'),
                            sg.Radio('Feminino', group_id='sexo', key='feminino')]],)],

        [sg.Text('E-mail:'), sg.Input(key='email'), sg.Text('Data de Nascimento:'), sg.Input(key='dntNascimento')],

        [sg.Text('Observações: '),sg.Multiline(size=(50,5), background_color='white')],

        [sg.Column([
            [sg.Button('Cadastrar', button_color=('white', '#0079d3'), size=(10,2))]
        ],justification='center', key='minha_coluna')]
    ]

    janelaCadastro = sg.Window('Cadastro de Pessoas', layout)
    return janelaCadastro


def editar():
    layout = [
        [sg.Text('PESSOAS CADASTRADAS', justification='center')],
        [sg.Button('Remover')]
    ]
    janela = sg.Window('Editando', layout=layout, finalize=True)
    return janela


# def sobre():


janela1, janela2, janela3, janela4 = janela_TelaInicial(), None, None, None

while True:
    # window, evento, valores = sg.read_all_windows()
    evento, valores = janela1.read()

    if (evento == sg.WINDOW_CLOSED):
        break

    if evento == 'Cadastrar':
        janela1.hide()
        janela2 = cadastrar()
        e, v = janela2.read()

        if (e == 'Cadastrar'):
            result = sg.popup('Cadastro realizado com Sucesso!!!', button_color='#0079d3')

        if(result == 'OK'):
            janela1.un_hide()
            janela2.close()
            print(result)


    if evento == 'Editar':
        janela1.hide()
        janela3 = editar()
        e, v = janela3.read()

        if (e == 'Remover'):
            janela1.un_hide()  # volta para a janela 1

janela1.close()
