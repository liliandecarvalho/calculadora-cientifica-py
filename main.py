# Importando tkinter
from tkinter import *
from tkinter import ttk

# Importando a biblioteca math
import math

# Cores:
cor1 = '#363434'  # preta
cor2 = '#ffab40'  # branca
cor3 = '#37474F'  # cinza

# Criando a janela principal
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x289')
janela.config(bg=cor1)

# Criando os frames
frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

frame_quadros = Frame(janela, width=300, height=340)
frame_quadros.grid(row=2, column=0)

# Funcoes
global todos_valores
todos_valores = ''
texto = StringVar()

# Funcao entrar valores na tela


def entrar_valores(evento):
    global todos_valores

    todos_valores = todos_valores + str(evento)
    texto.set(todos_valores)

# Funcao calcular


def calcular():
    global todos_valores

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log',
               'math.log10', 'math.e', 'math.pow', 'math.pi', 'math.radian']

    for i in modulos:
        if i == 'math.tan':
            todos_valores = todos_valores.replace('tan', i)

        if i == 'math.sin':
            todos_valores = todos_valores.replace('sin', i)

        if i == 'math.cos':
            todos_valores = todos_valores.replace('cos', i)

        if i == 'math.sqrt':
            todos_valores = todos_valores.replace('\u221a', i)

    # ---------------------------------------

        if i == 'math.log':
            todos_valores = todos_valores.replace('log', i)

        if i == 'math.log10':
            todos_valores = todos_valores.replace('log10', i)

        if i == 'math.e':
            todos_valores = todos_valores.replace('e', i)

        if i == 'math.pow':
            todos_valores = todos_valores.replace('^', i)

    # ---------------------------------------

        if i == 'math.pi':
            todos_valores = todos_valores.replace('TT', i)

    resultado = str(eval(todos_valores))
    texto.set(resultado)

    todos_valores = ''

# Funcao limpar tela


def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set('')


# Configurando o frame tela
label_tela = Label(frame_tela, textvariable=texto, width=16, height=2, padx=7,
                   anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# Configurando o frame cientifica
b_tan = Button(frame_cientifica, command=lambda: entrar_valores('tan'), text="tan", width=6, height=1, bg=cor1, fg=cor2, font=(
    'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_tan.place(x=0, y=1)
b_sin = Button(frame_cientifica, command=lambda: entrar_valores('sin'), text="sin", width=6, height=1, bg=cor1,
               fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_sin.place(x=59, y=1)
b_cos = Button(frame_cientifica, command=lambda: entrar_valores('cos'), text="cos", width=6, height=1, bg=cor1,
               fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_cos.place(x=118, y=1)
b_sqrt = Button(frame_cientifica, command=lambda: entrar_valores('\u221a'), text="\u221a", width=6, height=1, bg=cor1,
                fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_sqrt.place(x=177, y=1)


b_log = Button(frame_cientifica, command=lambda: entrar_valores('log'), text="log", width=6, height=1, bg=cor1,
               fg=cor2, font=(
                   'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_log.place(x=0, y=29)
b_log10 = Button(frame_cientifica, command=lambda: entrar_valores('log10'), text="log10", width=6, height=1, bg=cor1,
                 fg=cor2, font=(
                     'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_log10.place(x=59, y=29)
b_euler = Button(frame_cientifica, command=lambda: entrar_valores('e'), text="e", width=6, height=1, bg=cor1,
                 fg=cor2, font=(
                     'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_euler.place(x=118, y=29)
b_pow = Button(frame_cientifica, command=lambda: entrar_valores('\u005E'), text="\u005E", width=6, height=1, bg=cor1,
               fg=cor2, font=(
                   'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_pow.place(x=177, y=29)


b_pi = Button(frame_cientifica, command=lambda: entrar_valores('TT'), text="TT", width=6, height=1, bg=cor1,
              fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_pi.place(x=0, y=58)
b_virgula = Button(frame_cientifica, command=lambda: entrar_valores(','), text=",", width=6, height=1, bg=cor1,
                   fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_virgula.place(x=59, y=58)
b_abre_chave = Button(frame_cientifica, command=lambda: entrar_valores('('), text="(", width=6, height=1, bg=cor1,
                      fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_abre_chave.place(x=118, y=58)
b_fecha_chave = Button(frame_cientifica, command=lambda: entrar_valores(')'), text=")", width=6, height=1, bg=cor1,
                       fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_fecha_chave.place(x=177, y=58)


b_c = Button(frame_quadros, command=lambda: limpar_tela(), text="C", width=14, height=1, bg=cor1,
             fg=cor2, font=(
                 'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, )
b_c.place(x=0, y=0)
b_percentual = Button(frame_quadros, command=lambda: entrar_valores('%'), text="%", width=6, height=1, bg=cor1,
                      fg=cor2, font=(
                          'Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, )
b_percentual.place(x=118, y=0)
b_divisao = Button(frame_quadros, command=lambda: entrar_valores('/'), text="/", width=6, height=1, bg=cor1,
                   fg=cor2, font=('Ivy 10 bold'),
                   relief=RAISED, overrelief=RIDGE, )
b_divisao.place(x=177, y=0)


b_7 = Button(frame_quadros, command=lambda: entrar_valores(7), text="7", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=29)
b_8 = Button(frame_quadros, command=lambda: entrar_valores(8), text="8", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=29)
b_9 = Button(frame_quadros, command=lambda: entrar_valores(9), text="9", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=29)
b_multiplicacao = Button(frame_quadros, command=lambda: entrar_valores('*'), text="*", width=6, height=1, bg=cor1,
                         fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_multiplicacao.place(x=177, y=29)


b_4 = Button(frame_quadros, command=lambda: entrar_valores(4), text="4", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=58)
b_5 = Button(frame_quadros, command=lambda: entrar_valores(5), text="5", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=58)
b_6 = Button(frame_quadros, command=lambda: entrar_valores(6), text="6", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=58)
b_subtracao = Button(frame_quadros, command=lambda: entrar_valores('-'), text="-", width=6, height=1, bg=cor1,
                     fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_subtracao.place(x=177, y=58)


b_1 = Button(frame_quadros, command=lambda: entrar_valores(1), text="1", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=87)
b_2 = Button(frame_quadros, command=lambda: entrar_valores(2), text="2", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=87)
b_3 = Button(frame_quadros, command=lambda: entrar_valores(3), text="3", width=6, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=87)
b_adicao = Button(frame_quadros, command=lambda: entrar_valores('+'), text="+", width=6, height=1, bg=cor1,
                  fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_adicao.place(x=177, y=87)


b_0 = Button(frame_quadros, command=lambda: entrar_valores(0), text="0", width=14, height=1, bg=cor1,
             fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=116)
b_ponto = Button(frame_quadros, command=lambda: entrar_valores('.'), text=".", width=6, height=1, bg=cor1,
                 fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=116)
b_igual = Button(frame_quadros, command=lambda: calcular(), text="=", width=6, height=1, bg=cor1,
                 fg=cor2, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=116)


janela.mainloop()
