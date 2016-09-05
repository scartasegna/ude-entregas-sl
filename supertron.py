#!/usr/bin/python3
# coding: utf-8

"Programa para probar y evaluar a numentron" 

import subprocess
import select
import fcntl
import os

# lanzar un proceso secundario (vía pipas, -u sin buffer)
proceso = subprocess.Popen(
    ['python3', "-u", "numetron.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True)

for fd in proceso.stdout.fileno(), proceso.stderr.fileno():
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

#Se inician las diferentes variables a utilizar en el codigo
error = mensaje = ''
x = '50'
inicio = 1
fin = 100
pasada = 0
antF = fin
antI = inicio

#Mientras se reciban mensajes, seguiremos ejecutando codigo
while True:
    print("Pasada {}".format(pasada))
    disp = select.select([proceso.stderr], [], [], 1)[0]
    print("disp {}".format(disp))
    if proceso.stderr in disp:
        error = proceso.stderr.read()
        if error != "":
            print("ERROR: *%s*" % error)
            break

#Se recibe el mensaje hasta que se detecta en caracter de fin de linea
    while True:
        char = proceso.stdout.read(1)
        if not char or char == "\n":
            break
        mensaje += char.lower()
    
    print("mensaje recibido " + mensaje)

    if mensaje.startswith('adivi'):
        print ("ADIVINAMOS!")
        break
    elif mensaje.startswith('inicio') and mensaje.strip().endswith(":"):
        print('mandando inicio rango {}'.format(inicio))
        print ("me Comunico A")
        proceso.stdin.write((str(inicio) + "\n"))
        proceso.stdin.flush()                 
        mensaje = ''
    elif mensaje.startswith('fin') and mensaje.strip().endswith(":"):
        print('mandando fin rango {}'.format(fin))
        print ("me Comunico B")
        proceso.stdin.write((str(fin) + "\n"))
        proceso.stdin.flush()         
        #proceso.stdin.write(x)
        mensaje = ''        
    elif mensaje.startswith('menor'):
        #Si es mayor es (elec +1 + fin) /2
        print("{} + 1 + {}) // 2".format(x,antF))
        prom = (int(x) + 1 + antF) // 2
        antI = int(x)
        x = str(prom)
        print ("CALCULO MENOR y da {}".format(x))        
    elif mensaje.startswith('mayor'):
        #Si es mayor es (elec +1 + fin) /2
        print("{} + 1 + {}) // 2".format(x,antI))
        prom = (int(x) + antI) // 2
        antF = int(x)        
        x = str(prom)
        print ("CALCULO MAYOR y da {}".format(x))
    elif mensaje.startswith('elija'):
        #Mandamos x
        print ("me Comunico y mando {}".format(x))
        proceso.stdin.write((str(x) + "\n"))
        proceso.stdin.flush()
    elif mensaje:
        print('mensaje desconocido:', mensaje)
        mensaje = ''
    pasada +=1
    mensaje = ''
print("MENSAJE: *%s*" % mensaje)
print("ERROR: *%s*" % error)
