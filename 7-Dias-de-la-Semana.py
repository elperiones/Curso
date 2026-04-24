# 7 PROGRAMA PARA VER LOS DIAS DE LA SEMANA

semana = int(input("Introduzca un numero del 1 al 7:"))

if semana == 1 and semana <= 7:
    print("Es el dia Lunes")
elif semana == 2:
    print("Es el dia Martes")
elif semana == 3:
    print("Es el dia Miercoles")
elif semana == 4:
    print("Es el dia Jueves")
elif semana == 5:
    print("Es el dia Viernes")
elif semana == 6:
    print("Es el dia Sabado")
elif semana == 7:
    print("Es el dia Domingo")
else:
    print("Error, Debe ingresar un numero entre el 1 al 7")