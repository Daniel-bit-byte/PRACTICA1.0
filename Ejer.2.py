print("ingrse coeficientes ")
a = int(input("ingrese el coficiente a:"))
b = int(input("ingrese el coficiente b:"))
c = int(input("ingrese el coficiente c:"))
D = (b)**2 - 4*a*c
if D > 0:
     print("las raices serán reales y diferentes")
elif D < 0:
     print("las raices serán complejas")
else:
     print("las raices serán reales e iguales")

    