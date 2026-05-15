import numpy as np

a = np.array([1,2,3,4,5])
a = a + 2
suma = np.suma(a)
promedio = np.mean(a)


#b = np.zeros([5])
#c = np.ones([3])
 
#print(np.__version__ )
print(a)
print(suma)
print(promedio)
#print(b)
#print(c)

matriz = np.ones([3,3])
matriz = matriz + 4
sumMatriz = np.sum(matriz)

print(matriz)  
print(sumMatriz)