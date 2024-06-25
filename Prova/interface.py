import tkinter as tk

def interface():

    def enviar():
        janela.update()


    def exibir():
        janela.update()

    janela = tk.Tk()

    janela.title('DADOS-GRÁFICOS')
    #janela.geometry('500x300')

    label_t1 = tk.Label(janela, text='NOME')
    label_t1.grid(padx=10, pady=10,  row=0, column=0)

    caixa_t1 = tk.Entry(janela)
    caixa_t1.grid(padx=10, pady=10, row=0, column=1)


    label_t2 = tk.Label(janela, text='IDADE')
    label_t2.grid(padx=10, pady=10, row=1, column=0)

    caixa_t2 = tk.Entry(janela)
    caixa_t2.grid(padx=10, pady=10, row=1, column=1)

    botao1 = tk.Button(janela, text='ENVIAR DADOS', bg='purple', command=enviar())
    botao1.grid(padx=10, pady=10, row=2, column=0)
    botao2 = tk.Button(janela, text='EXIBIR GRÁFICO', bg='blue', command=exibir())
    botao2.grid(padx=10, pady=10, row=2, column=1)


    janela.mainloop()