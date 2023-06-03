import PySimpleGUI as sg

# Janela1
def janela_TelaInicial():
    sg.theme('DarkBlue')

    srcImage = sg.Image('imgs/Logo with text for GitHub Top.png')
    # menu =  sg.Menu()

    layout = [
        [srcImage],
        [sg.Menu([['Pessoa', ['Cadastrar-se', 'Editar']], ['Ajuda', ['Sobre']]])]
    ]
    janela = sg.Window("Tela Inicial", layout, finalize=True)

    return janela

#Janela2
def cadastrar():
    layout = [
        [sg.Text("CADASTRO DE PESSOAS", justification='right')],

        [sg.Text('CPF:'), sg.Input(key='-cpf-'), sg.Text('Nome:'), sg.Input(key='-nome-')],
        [sg.Text('Endereço:'), sg.Input(key='-endereco-')],

        [sg.Text('Cidade:'), sg.Input(key='-cidade-'), sg.Text('Estado:'),
         sg.Combo(['SP', 'RJ', 'MG', 'ES'], key='-estado-')],

        [sg.Frame('Sexo', [[sg.Radio('Masculino', group_id='sexo', key='-masculino-'),
                            sg.Radio('Feminino', group_id='sexo', key='-feminino-')]], )],

        [sg.Text('E-mail:'), sg.Input(key='-email-'), sg.Text('Data de Nascimento:'), sg.Input(key='-dntNascimento-')],

        [sg.Text('Observações: '), sg.Multiline(size=(50, 5), background_color='white',key='-obs-')],

        [sg.Column([
            [sg.Button('Cadastrar', button_color=('white', '#0079d3'), size=(10, 2))]
        ], justification='center', key='-minha_coluna-')]
    ]

    janelaCadastro = sg.Window('Cadastro de Pessoas', layout)
    return janelaCadastro

#Janela3
def editar():
    # para teste
    dados = [
        ['333.656.665-33', 'Rogério Colpani', 'Rua das Dores', 'Mococa', 'Ceará', 'Masculino', 'rogerio@gmail.com',
         '10/10/1980', 'só observo você']]
    cabecalho = ['CPF', 'NOME', 'ENDEREÇO', 'CIDADE', 'ESTADO', 'SEXO', 'E-MAIL', 'DATA-DE-NASCIMENTO',
                 'OBSERVAÇÕES']

    layout = [
        [sg.Column([
            [sg.Text('PESSOAS CADASTRADAS')]
        ], justification='center')],

        [sg.Column([
            [sg.Table(values=dados, headings=cabecalho, justification='center',
                      enable_click_events=True, key='-tabela-', display_row_numbers=True, auto_size_columns=True)],
        ], justification='center')],

        [sg.Column([
            [sg.Button('Remover')],
        ], justification='center')]
    ]
    janela = sg.Window('Editando', layout=layout, finalize=True, )
    return janela

#Janela4
def sobre():

    layout = [
        [sg.Listbox(values=['Nome: Thiago Carretero dos Santos, \n\nRafael Almeida Vasconcelos, \n\nRaphael Baruque Souza, \n\nGuilherme Dias Gregorio.',
                            'Formação:',
                            'Cargo:',
                            'Local de trabalho:',
                            'Area de atuação:'],size=(100,10))]
    ]

    janela = sg.Window('Informações sobre os Autores',layout=layout)
    return janela


janela1, janela2, janela3, janela4 = janela_TelaInicial(), None, None, None

while True:
    # window, evento, valores = sg.read_all_windows()
    evento, valores = janela1.read()

    if (evento == sg.WINDOW_CLOSED):
        break

    if evento == 'Cadastrar-se':
        janela1.hide()
        janela2 = cadastrar()
        e, v = janela2.read()

        if (e == 'Cadastrar'):

            cpf = v['-cpf-']
            nome = v['-nome-']
            endereco = v['-endereco-']
            cidade = v['-cidade-']
            estado = v['-estado-']
            sexo = v['-masculino-']
            email = v['-email-']
            dataNascimento = v['-dntNascimento-']
            observacoes = v['-obs-']

            dado = [cpf, nome, endereco, cidade, estado, sexo, email, dataNascimento, observacoes]

            # Adiciona os novos dados à tabela
            janela3 = editar()
            tabela = janela3['-tabela-']

            tabelaValores = tabela.Get()# Obtém os valores atuais da tabela
            tabelaValores.append(dado)# Adiciona uma nova linha aos valores
            tabela.update(values=tabelaValores)

    if (e == 'Remover'):
        tabela = janela3['-tabela-']
        index = tabela.SelectedRows[0]
        dado.Values
        dado.pop(index)

        tabela.update(values=dado)
        janela3['-tabela-'].update(select_rows=[-1])
        print(index)

            # result = sg.popup('Cadastro realizado com Sucesso!!!', button_color='#0079d3')




    if evento == 'Editar':
        janela1.hide()
        janela3 = editar()
        e, v = janela3.read()


    if evento == 'Sobre':
        janela1.hide()
        janela4 = sobre()
        e, v = janela4.read()

janela1.close()
