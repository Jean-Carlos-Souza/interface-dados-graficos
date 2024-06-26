import matplotlib.pyplot as plt
import interface

x = []

y = []

def dividindo(t1, t2):

    x.append(t1)
    y.append(t2)

def resultado():
    
    plt.bar(x, y, color = 'purple')
    plt.ylabel('Idade')
    plt.xlabel('Nome')
    plt.title('IDADExNOME')
    plt.legend('Azul')
    plt.show()

