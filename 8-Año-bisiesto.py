# 8 PROGRAMA PARA VERIFICAR QUE AÑO ES O NO ES BISIESTO

año = int(input("Introduce un año para verificar: "))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f"El año {año} si es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")