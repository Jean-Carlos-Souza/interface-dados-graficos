import matplotlib.pyplot as plt
import interface

x = []

y = []  

def dividindo(t1, t2):

    x.append(t1)
    y.append(t2)

def resultado():
    
    plt.bar(x, y, color = '#7fffd4', width=0.2)
    plt.ylabel('Idade', color = 'red')
    plt.xlabel('Nome', color = 'red')
    plt.title('IDADE x NOME', color = 'black')
    plt.legend('green')
    plt.show()

