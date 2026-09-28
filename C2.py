week = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#Dentro de un for iterar para saber en cual posicion estan los fines de semana. Respuesta esperada: [5,6]

out = []
for i, day in enumerate(week):
    if day == "Domingo" or day == "Sabado":
        #out = [i]
        out.append(i)

print(out)
        