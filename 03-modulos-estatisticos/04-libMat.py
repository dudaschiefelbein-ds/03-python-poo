import matplotlib.pyplot as plt 

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTi = [60, 52, 76, 89, 108, 95]
qtdRh = [40, 72, 17, 28, 87, 56]


plt.plot(meses, qtdTi, label="TI", color="blue", linestyle="-", marker=".")
plt. plot(meses, qtdRh, label="RH", color="red", linestyle="-", marker="o")
plt. title('Chamados abertos' )
plt.xlabel ('Meses')
plt.ylabel ('Quantidade')
plt. legend()
plt. show()

