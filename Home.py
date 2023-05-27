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

# def cadastrar():
#
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
    window, evento, valores = sg.read_all_windows() #ou window.read()

    if(window == janela1 and evento == sg.WINDOW_CLOSED):
        break

    if window == janela1 and evento == 'Editar':
        janela3 = editar()
        janela1.hide()

    if(window == janela3 and evento == 'Remover'):
        janela1 = janela_TelaInicial()
        janela3.un_hide()

window.close()