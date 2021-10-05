#----->Cálculo del tiempo de reacción con la fórmula<------
"""     		------------
        		¦x[cm]¦t[s]¦
				¦-----¦----¦
				¦-----¦----¦
				------------			"""

n=int(input("Cantidad de medidas: "))
datos=[[0 for x in range(2)] for y in range(n)] #->Arreglo de Datos


def mostrarDatos(arreglo):
	print("\nx[m]	t[s]")
	for f in range(len(arreglo)):
		for c in range(2):
			print(arreglo[f][c],end="	")
		print()
	print("\n")

def mostrarTiempos(Array):
	print("\nt[s]")
	for i in range(len(datos)):
		print(Array[i])

def media(arreglo):
	sumax=0; promediox=0
	sumat=0; promediot=0
	for f in range(len(arreglo)):
		sumax=sumax+arreglo[f][0]
		sumat=sumat+arreglo[f][1]

	promediox=round(sumax/(len(arreglo)),2)
	promediot=round(sumat/(len(arreglo)),2)
	
	return promediox, promediot

def tiempoReaccion(arreglo):
	for i in range(len(arreglo)):
		x=float(input("int. distancia en cm: "))
		x=x/100 #-> centímetros a metros
		#tiempo de reacción redondeado a 2 decimales
		t=round(((2*x)/(9.775))**(1/2),2) 
		arreglo[i][0]=x #-->Agregando distancia al arreglo
		arreglo[i][1]=t #-->Agregando tiempo de reaccion al arreglo



tiempoReaccion(datos)
mostrarDatos(datos)
(medx,medt)=media(datos)

print("Media x: ",medx,"[m]")
print("Media t: ",medt,"[s]")


#---->Generación de Histograma<------

tiempos=[0]*n

for i in range(len(datos)):
	tiempos[i]=datos[i][1]
tiempos.sort()

mostrarTiempos(tiempos)


import matplotlib.pyplot as plt
div=[0.14,0.16,0.18,0.20,0.22,0.24]
plt.hist(tiempos, div,ec="black")
plt.title("Histograma tiempos de reacción")
plt.xlabel("Tiempo [s]")
plt.ylabel("Número de medidas")
plt.ylim(1,30)
plt.grid()
plt.show()
