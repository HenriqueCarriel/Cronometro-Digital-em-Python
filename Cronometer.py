import time
from tkinter import *
import tkinter

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#definindo o tamanho da aplicação
janela = Tk()
janela.title("Cronômetro em Python")
janela.geometry('310x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

# variaveis do projeto
global tempo
tempo = '00:00:00'
count = -5
run = False

# Funcao iniciar
def iniciar():
    def valor():
        if run:
            global count
            global tempo

            # condição antes de iniciar
            if count <= -1:
                inicio = "Começando em " + str(abs(count))
                label_time['text'] = inicio
                label_time['font'] = 'ivy 20 '
            else:
                label_time['font'] = 'Times 50 bold'
                d = str(tempo)
                h, m, s = map(int, d.split(":"))
                h = int(h)
                m = int(m)
                s = int(count)

                if (s >= 59):
                    count = 0
                    m += 1

                # incrementando os valores na variavel 'tempo'
                s = str(0) + str(s)
                m = str(0) + str(m)
                h = str(0) + str(h)

                # atualizando os valores atuais
                d = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
                label_time['text'] = d
                tempo = d
                s = int(count)
                m = int(m)
                h = int(h)

                # definindo o tempo dos segundos
            label_time.after(1000, valor)
            count += 1
    valor()

# iniciando o contador
def start():
    global run
    run = True
    iniciar()

# pausando o contador
def stop():
    global run
    run = False

# reiniciando o contador
def reset():
    global count
    count = -5

    # reiniciando o tempo
    if run == False:
        global tempo
        tempo = '00:00:00'
        label_time['text'] = tempo

    # reinicia com o cronometro funcionando
    else:
        label_time['font'] = 'ivy 20 '
        label_time['text'] = 'Iniciando...'
        time.sleep(1)

# criando as labels
label_app = Label(janela, text='Cronômetro Digital - Desenvolvido em Python', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_time = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor4)
label_time.grid(row=0, column=0, sticky=NSEW, padx=15, pady=20)

label_app.lift()

frameBaixo = Frame(janela, width=310, height=350, bg=cor1, relief="flat")
frameBaixo.grid(row=1, column=0, pady=0, padx=30, sticky=NSEW)

# criando os botoes
botao_start = Button(frameBaixo, command=start, text="Iniciar", width=11, height=2, bg=cor1, fg=cor2,
                     font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_start.grid(row=0, column=0, sticky=NSEW, padx=2, pady=12)

botao_stop = Button(frameBaixo, command=stop, text="Pausar", width=11, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'),
                    relief=RAISED, overrelief=RIDGE)
botao_stop.grid(row=0, column=1, sticky=NSEW, padx=2, pady=12)

botao_reset = Button(frameBaixo, command=reset, text="Reiniciar", width=11, height=2, bg=cor1, fg=cor2,
                     font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_reset.grid(row=0, column=2, sticky=NSEW, padx=2, pady=12)

janela.mainloop()