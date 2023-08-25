import numpy as np


l=[1,2,3,4,5] , [6,7,8,9,10]
n1= np.array(l)
print(n1)
print(type(n1))



#principales atributos
print(n1.ndim) #muestra las dimensiones
print(n1.shape) #muestra las tuplas, contiene el numero de tamano
print(n1.size)#muestra cantidad de elementos TOTAL
print(n1.dtype)#muestra que tipo de dato estamos usando


##Acceso a los elementos
#Para acceder al numero deseado primero deberemos ingresar el renglo y despues la columna




         #print(n1(1,2)) ## PRIMER NUMERO, es el renglon y SEGUNDO NUMERO es la columna

print(n1*2/2)
print(np.linalg.norm(n1))
print(n1[0,:].mean())  #MEAN SIRVE PARA SACAR PROMEDIOS, Y los dos puntos irve para indicar que quieres tomar todos los valores de la columna o renglon segun sea el caso


