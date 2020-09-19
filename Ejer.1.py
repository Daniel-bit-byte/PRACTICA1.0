print("verifica si tu tarea se puede procesar con un tiempo dado")
x = int(input("ingrese el tiempo dado en segundos:"))
print("introducir el tiempo a demorar la tarea en horas,minutos,segundos")
z= int(input("ingrese el tiempo en horas:"))
z1 = int(input("ingrese el tiempo en minutos:"))
z2 = int(input("ingrese el tiempo en segundos:"))
h = z*60*60
m = z1*60
s = z2
t = h + m + s
if x > t:
 print("la tarea se puede completar")
else:
 print("el timepo es isuficiente")
 
 
