import matplotlib.pyplot as plt

def grafico_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_moedas, labels=l_moedas)
    plt.title('Proporção em relação ao BRL = Real Brasileiro)')
    plt.show()
    
def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

