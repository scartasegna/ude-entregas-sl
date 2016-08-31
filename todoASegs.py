# Hacer un programa que pida el ingreso de hora,minutos,segundos
# dos veces  y luego las sume

def pasarASegundos(h,m,s):
   return(h*60*60 + m*60 + s)

def pasarAHMS(segundos):
    horas = segundos / 3600
    minutos = (segundos % 3600) / 60
    segundos = (segundos % 3600) % 60
    return (horas, minutos, segundos)

horas = int(input("Ingrese la 1er cantidad de horas: "))

mins = int(input("Ingrese la 1er cantidad de minutos: "))

segs = int(input("Ingrese la 1er cantidad de segundos: "))

todoSegs = pasarASegundos(horas,mins,segs)

horas2 = int(input("Ingrese la 1er cantidad de horas: "))

mins2 = int(input("Ingrese la 1er cantidad de minutos: "))

segs2 = int(input("Ingrese la 1er cantidad de segundos: "))

todoSegs2 = pasarASegundos(horas2,mins2,segs2)

totalSegs = todoSegs + todoSegs2

(h,m,s) = pasarAHMS(totalSegs)

strh1 = str(horas) +":"+str(mins)+":"+str(segs)
strh2 = str(horas2) +":"+str(mins2)+":"+str(segs2)

print( "La suma de " +strh1 +" y " + strh2 + " es " \
      + str(h) + " horas " + str(m) + " minutos " + str(s) + " segundos")
#print(str(horas) + " horas " + str(mins) + " minutos " \
#      + str(segs) + " segundos son " + str(todoSegs) + " segundos")


#segs = int(input("Ingrese la cantidad de segundos a convertir: "))


#(h,m,s) = pasarAHMS(segs)

#print(str(segs) + " segundos son un total de " + str(h) + " horas "  \
#      + str(m) + " minutos " + str(s) + " segundos")
