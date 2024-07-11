import tkinter as tk
from grafico import resultado, dividindo


def interface():

    def enviar():
        t1 = caixa_t1.get()
        t1 = str(t1)
        t2 = caixa_t2.get()
        t2 = int(t2)
        dividindo(t1, t2)


    def exibir():

        resultado()

    janela = tk.Tk()

    janela.title(' DADOS-GRÁFICOS ')

    label_t1 = tk.Label(janela, text=' NOME ')
    label_t1.grid(padx=10, pady=10,  row=0, column=0)

    caixa_t1 = tk.Entry(janela, text='')
    caixa_t1.grid(padx=10, pady=10, row=0, column=2)


    label_t2 = tk.Label(janela, text=' IDADE ')
    label_t2.grid(padx=10, pady=10, row=1, column=0)

    caixa_t2 = tk.Entry(janela)
    caixa_t2.grid(padx=10, pady=10, row=1, column=2)

    botao1 = tk.Button(janela, text=' ENVIAR DADOS ', bg='purple', command=enviar)
    botao1.grid(padx=10, pady=10, row=2, column=0)
    botao2 = tk.Button(janela, text=' EXIBIR GRÁFICO ', bg='blue', command=exibir)
    botao2.grid(padx=10, pady=10, row=2, column=2)

    

    janela.mainloop()