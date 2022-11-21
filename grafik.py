from matplotlib import pyplot as plt
import numpy as np

boylistesi = []
kilolistesi = []
for i in range(10):
    boy = input("Boyunuzu giriniz")
    kilo = input("Kilonuzu giriniz")
    boylistesi.append(boy)
    kilolistesi.append(kilo)
numpyboy = np.array(boylistesi)
numpykilo = np.array(kilolistesi)
plt.bar(numpyboy, numpykilo)
plt.legend()
plt.xlabel('Boy')
plt.ylabel('Kilo')
plt.title('Boy ve Kilo Grafiği')
plt.show()
