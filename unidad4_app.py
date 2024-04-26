# Simulando datos
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## De distribuciones uniformes a distribuciones normales
# Distribucion uniforme
a = np.random.uniform(0, 10, 10000)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
unifo = sns.histplot(a)
plt.title('Uniform Distribution')


# Distribución tipo normal
for i in range(0,10000):
    b = np.random.uniform(0, 10, 10000)
    b = b + np.random.uniform(0, 10, 10000)

plt.subplot(1, 2, 2)
norm = sns.histplot(b)
plt.title('Normal distribution')

