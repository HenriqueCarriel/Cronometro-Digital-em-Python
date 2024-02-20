# Cronometro em Python
# Projeto realizado com linguagem Python
# Bibliotecas usadas: timer, tkinter
# timer = para manipular o tempo usando métodos de strings
# tkinter = para a parte gráfica (GUI) do aplicativo

from tkinter import *
import tkinter

#cores do projeto
cor1 = "#0a0a0a" # black / preta
cor2 = "#fafcff" # white / branca
cor3 = "#21c25c" # green / verde
cor4 = "#eb463b" # red / vermelha
cor5 = "#dedcdc" # gray / cinza
cor6 = "#3080f0" # blue / azul

# Tamanho da aplicação / Application size
janela = Tk()
janela.title("Cronômetro 3,2,1...")
janela.geometry("310x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

global tempo
tempo = "00:00:00"

count = -5
run = False

# função iniciar / start function
def iniciar():
    def valor():
        if run:
            global count
            global tempo

            # antes de começar / before starting
            if count <= -1:
                inicio = "começando em" + str(abs(count))
                label_time['text'] = inicio
                label_time['font'] = 'ivy 20'
            else:
                label_time['font'] = 'Times 50 bold'
                d = str(tempo)
                h,m,s = map(int,d.split(":"))
                h = int(h)
                m = int(m)
                s = int(count)

                if(s>=5):
                    count = 0
                    m+=1

                s = str(0) + str(s)
                m = str(0) + str(m)
                h = str(0) + str(h)

                d= str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
                label_time['text'] = d
                tempo = d

                s = int(count)
                m = int(m)
                h = int(h)

                label_time.after(1000, valor)
                count += 1
            valor()

# função para iniciar o cronômtro / function to start the stopwatch
def start():
    global run
    run = True
    iniciar()

# função para pausar o cronômetro / function to pause the stopwatch
def pause():
    global run
    run = False

# função para reiniciar o cronômetro / function to reset the timer
def reset():
    global count
    count = -5

# Se estiver pausado irá reiniciar do zero / If it is paused it will restart from scratch
if run == False:
    global tempo
    tempo = "00:00:00"
    label_time['text'] = tempo

# Se nao estiver pausado irá continuar onde parou antes / If it is not paused it will continue where it left off before
else:
    label_time['font'] = "ivy 20"
    label_time['font'] = "Iniciando..."

label_app = Label(janela, text='cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20,y=5)

label_time = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_time.grid(row=0, column=0, sticky=NSEW, padx=15, pady=20)

label_app.lift()

frameBaixo = Frame(janela,width=310, height=350,bg=cor1, relief="flat")
frameBaixo.grid(row=1, column=0,pady=0, padx=30, sticky=NSEW)

botao_start = Button(frameBaixo,command=start, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_start.grid(row=0, column=0, sticky=NSEW, padx=2, pady=10)

botao_stop = Button(frameBaixo,command=stop, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_stop.grid(row=0, column=1, sticky=NSEW, padx=2, pady=10)

botao_reset = Button(frameBaixo, command=reset, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_reset.grid(row=0, column=2, sticky=NSEW, padx=2, pady=10)


janela.mainloop()