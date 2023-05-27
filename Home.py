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

#def cadastrar():



def editar():
    layout =[
        [sg.Text('Editando')],
        [sg.Button('Remover')]
    ]
    janela = sg.Window('Editando',layout=layout, finalize=True)
    return janela

# def sobre():
#     return

janela1, janela2, janela3, janela4 = janela_TelaInicial(), None, None, None

while True:
    #window, evento, valores = sg.read_all_windows()
    evento, valores = janela1.read()

    if(evento == sg.WINDOW_CLOSED):
        break

    if evento == 'Editar':
        janela1.hide()
        janela3 = editar()
        e, v = janela3.read()

        if(e == 'Remover'):
            janela1.un_hide() #volta para a janela 1

janela1.close()