
"""editador por: Williams Bobadilla
   extraido de: https://www.monografias.com/trabajos-pdf5/vpython-aplicaciones-fisica-educativa/vpython-aplicaciones-fisica-educativa.shtml
   fecha: 13-11-2018
   descripcion: modelo del atomo de hidrogeno, con giro del spin 
   """





import vpython as visual
import time


#creamos ejes para mejor ubicacion
ejex=visual.cylinder(radius=0.01, lenght=3000,axis=visual.vector(1,0,0),color=visual.color.red)  #eje x
ejey=visual.cylinder(radius=0.01, lenght=3000,axis=visual.vector(0,1,0),color=visual.color.green) #eje y
ejez=visual.cylinder(radius=0.01, lenght=3000,axis=visual.vector(0,0,1),color=visual.color.blue) #eje z

color=visual.color

n1= visual.sphere(pos=visual.vector(1,0,0), radius=1, color=color.green)
n2=visual.sphere(pos=visual.vector(2,1,0), radius=1, color=color.green)
p1=visual.sphere(pos=visual.vector(2,0,0), radius=1, color=color.red)
p2=visual.sphere(pos=visual.vector(1,1,0), radius=1, color=color.red)



e1=visual.sphere(pos=visual.vector(15,0,0), radius=0.5, color=color.blue)
e2=visual.sphere(pos=visual.vector(0,15,0), radius=0.5, color=color.red)

dt=0.1
curva1=visual.curve()
curva2=visual.curve()


while True:
	visual.rate(20)
	dt=0.1
	e1.rotate(angle=-dt, origin=visual.vector(0,0,0), axis=visual.vector(0,0.3,0))
	e2.rotate(angle=-dt, origin=visual.vector(0,0,0), axis=visual.vector(0.3,0,0))
	curva1.append(pos=e1.pos)
	curva2.append(pos=e2.pos)


