# JUEGO DE HISTORIA CON DECICIONES

print("\n" + "="*50)
print(" SENDA DE REDENCION")
print("="*50 + "\n")
print(" Eres Sylas 'El Zurdo', un forajido buscado por la ley. Acabas de escapar del asalto al banco de Valentine.")
print(" El sol de mediodia quema y los cazarrecompensas te pisan los talones.")
print(" En tus fundas llevas tu REVOLVER Cattleman y en la montura unos BINOCULARES. \n")

decision1 = input("¿Qué desenfundas primero? ¿El REVOLVER  o los BINOCULARES ? > ").lower()

if decision1 == "binoculares":    

        print("\n Observas el horizonte. A lo lejos, ves dos rutas para cruzar la frontera.")
        print(" El DESFILADERO del Diablo, estrecho y con salientes para esconderse.")
        print(" El VADO del río San Luis, donde el agua es baja pero estás a campo abierto.\n")
        decision2 = input("¿Por dónde intentas cruzar? ¿DESFILADERO  o VADO ? > ").lower()

        if decision2 == "desfiladero":

            print("\n Te adentras en el cañon. De repente, escuchas el llanto de una mujer. ")
            print(" Hay una diligencia volcada. Una mujer pide ayuda, pero parece una emboscada de la banda de los O'Driscoll.\n")
            
            decision3 = input("¿Qué haces? ¿AYUDAR , IGNORAR  o USAR DE CEBO a la mujer ? > ").lower()

            if decision3 == "ayudar":
                print("\n Era una trampa, ¡pero tu rapidez te salva! Desarmas a los bandidos y la mujer resulta ser una aliada.")
                print(" Ella te muestra un atajo secreto hacia el campamento de tu banda.\n")
                decision4 = input("¿Decides IR al campamento o REPARTIR el botin con ella ? > ").lower()
                
                if decision4 == "campamento":
                    print("\n Llegas al campamento. Tu lider te recibe como a un heroe. Tienen un plan para el gran golpe final. ")
                    print(" Hay un tren cargado de oro pasando a medianoche.\n")
                    decision5 = input("¿Qué posición tomas? ¿MAQUINISTA , DINAMITERO  o FRANCOTIRADOR ? > ").lower()
                    
                    if decision5 == "dinamitero":
                        print("\n BOOM! Las vias saltan por los aires y el tren se detiene. Te llevas una fortuna. ")
                        print(" GANASTE! Te retiras a una granja en el sur y dejas la vida criminal. \n")
                    elif decision5 == "maquinista":
                        print("\ El maquinista estaba armado y te dispara antes de que puedas tomar el control. ")
                        print(" Game Over. La ley te atrapo en los railes. \n")
                    else:
                        print("\n Un rifle te falla en el momento critico. Los guardias del tren te rodean. ")
                        print(" Game Over. Tu punteria no fue suficiente hoy. \n")
                
                elif decision4 == "repartir":
                    print("\n Ella te traiciona al ver el oro. Te dispara por la espalda mientras contabas las monedas. ")
                    print(" Game Over. No hay honor entre ladrones. \n")
                else:
                    print(" Te quedas pensando y los cazarrecompensas te alcanzan. Game Over. \n")

            elif decision3 == "ignorar":
                print("\n Sigues de largo. El remordimiento te persigue, pero logras salir del cañon solo para caer en un nido de pumas. ")
                print(" Game Over. La naturaleza es más cruel que la ley. \n")
            elif decision3 == "usar":
                print("\n Intentas usarla de cebo, pero el Sheriff te estaba observando desde arriba. ")
                print(" Game Over. Vas directo a la horca por tu falta de honor. \n")
            else:
                print(" Respuesta no valida: Tu caballo se asusta y te tira por un barranco. Game Over. \n")

        elif decision2 == "vado":
            print("\n El agua esta fria. A mitad del rio, tu caballo se queda atrapado en el lodo. ")
            decision3 = input("¿Qué haces? ¿ABANDONAR al caballo  o INTENTAR salvarlo ? > ").lower()
            
            if decision3 == "salvarlo":
                print("\n Con un esfuerzo sobrehumano, sacas a tu fiel compañero. El caballo te lo agradece galopando contigo hasta México.")
                print(" Ganaste! La lealtad a tu caballo te salvo la vida. \n")
            elif decision3 == "abandonar":
                print("\n Corres hacia la orilla, pero sin caballo eres presa facil para los lobos que acechan. ")
                print(" Game Over. Un jinete sin caballo no es nada en el Oeste. \n")
            else:
                print(" Respuesta no valida. Te ahogas en la corriente. Game Over. \n")

elif decision1 == "revolver":
        print("\n Prefieres el hierro. Entras en el salón del pueblo más cercano buscando suministros. ")
        print(" Un extraño te reta a un duelo en mitad de la calle. ")
        decision2 = input("¿Aceptas el DUELO  o intentas CALMAR los animos ? > ").lower()
        
        if decision2 == "duelo":

            print("\n Diez pasos. Te giras... ¡BANG! Eres más rapido, pero el extraño era el hijo del Gobernador. ")
            decision3 = input("¿Que haces? ¿HUIR hacia las montañas  o ENTREGARTE a la justicia ? > ").lower()
            
            if decision3 == "huir":
                print("\n Encuentras una mina abandonada llena de dinamita y suministros. ")
                print(" Ganaste! Te conviertes en el forajido más temido del Viejo Oeste. \n")
            elif decision3 == "entregarte":
                print("\n Crees en la justicia, pero el juez es corrupto. Te condenan sin juicio. ")
                print(" Game Over. La ley siempre gana en este siglo. \n")
            else:
                print(" Respuesta no valida. Te disparan mientras lo piensas. Game Over. \n")

        elif decision2 == "calmar":
            print("\n El hombre no escucha razones. Te dispara mientras intentas hablar. ")
            print(" Game Over. Trajiste palabras a una pelea de pistolas. \n")
        else:
            print(" Respuesta no valida. Te quedas congelado y te arrestan. Game Over. \n")
            
else:
        print(" Respuesta no valida. Los cazarrecompensas te encuentran perdiendo el tiempo y te entregan al Sheriff. Game Over. \n")

