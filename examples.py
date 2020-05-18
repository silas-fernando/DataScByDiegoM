# Boxplot - diagrama de caixa
import matplotlib.pyplot as plt
import random

vetor = []

for i in range(20):
	numero_aleatorio = random.randint(0,10)
	vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()