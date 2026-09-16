import matplotlib.pyplot as plt 

navegadores= ["Chrome","Firefox","Edge"]
qtd= [1200, 600, 200]
cores= ["red", "orange", "blue"]
plt.pie(qtd, labels=navegadores,colors=cores)

plt.show()
