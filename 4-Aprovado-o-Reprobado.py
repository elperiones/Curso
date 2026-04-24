# 4 PROGRAMA PARA VERIFICAR RESULTADO APROBADA O REPROBADA

calificacion = input("Ingrese su calificacion(0-100):")

nota = float(calificacion)

if nota >= 60 and nota <= 100:
    print("Aprobado")
elif nota >= 0 and nota <=59:
    print("Reprobado")
else:
    print("La nota esta fuera de rango, Ingresa una calificaion entre 0 y 100")