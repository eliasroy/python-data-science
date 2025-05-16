import numpy as np

meses=np.array(["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"])

producta = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700])
productb = np.array([180, 210,240,270,300,330,360,390,420,450,480,510])
productc = np.array([120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450])

print (f"Media de producto A: {np.mean(producta)}")
print (f"Suma de producto A: {np.sum(producta)}")
print (f"Media de producto B: {np.mean(productb)}")
print (f"Suma de producto B: {np.sum(productb)}")
print (f"Media de producto C: {np.mean(productc)}")
print (f"Suma de producto C: {np.sum(productc)}")

ventaspormes =producta+ productb+ productc

#mes con mayores ventas y mores ventas

mesconmayoresventas=meses[np.argmax(ventaspormes)]
mesconmenoresventas=meses[np.argmin(ventaspormes)]
print (f"Mes con mayores ventas: {mesconmayoresventas}")
print (f"Mes con menores ventas: {mesconmenoresventas}")
print (f"Meses: {meses}")
print (f"Ventas del mes: {ventaspormes}")


#matriz de 2d 
ventas2d = np.array([producta, productb, productc])
print (f"Ventas 2D: {ventas2d}")

#matriz de 3d
ventas3d = ventas2d.reshape(3, 4, 3)
print (f"Ventas 3D: {ventas3d}")