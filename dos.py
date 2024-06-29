import matplotlib
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig('test.png')  # En lugar de plt.show()
print("Gráfico guardado como 'test.png'")