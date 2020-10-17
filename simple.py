import random

e = 7
e1 = 1
e2 = 2
e3 = 3
e4 = 4

um = 0
um1 = 1
um2 = 2
um3 = 3
um4 = 4

def calculo(x1, x2, d):

    #Inicializar los pesos p1 y p2 (Valores aleatorios entre -1 y 1)
    p1 = random.uniform(-1.0, 1.0)
    p2 = random.uniform(-1.0, 1.0)

    #Calcular umbral (Valor aleatorio entre -1 y 1)
    u = random.uniform(-1.0, 1.0)

    #Calcular valor entre 0 y 1 (n)
    n = random.uniform(0, 1.0)

    #Calcular coeficiente de aprendizaje (y)
    y = ( p1 * x1) + (p2 * x2) - u

    #Calcular f
    f = 0
    if y >= 0:
        f = 1
    elif y < 0:
        f = 0
    else:
        print("Hay un problema al calcular el coeficiente de aprendizaje (y)")

    #Calcular valor de error
    e = 0
        
    e = d - f

    #Calcular variación para los pesos
    v1 = n * e * x1
    v2 = n * e * x2

    #Calcular nuevo valor de peso
    pe1 = p1 + v1 
    pe2 = p2 + v2

    #Calcular nuevo umbral
    um = u - (n * e)

    print("\n", 
        "################################","\n", 
        "Iteración 1","\n", 
        "################################","\n",
        "x1:",x1,"\n", 
        "x2:",x2,"\n",
        "p1:",p1,"\n",
        "p2:",p2,"\n",
        "n:",n,"\n",
        "y:",y,"\n",
        "f:",f,"\n",
        "d:",d,"\n",
        "u:",u,"\n",
        "e:",e,"\n",
        "v1:",v1,"\n",
        "v2:",v2,"\n",
        "pe1:",pe1,"\n",
        "pe2:",pe2,"\n",
        "um:",um,"\n",
        "um2:",um2,"\n",
        "um3:",um3,"\n",
        "um4:",um4,"\n",
        )
    
    e1 = e
    um1 = um



while e1 != 0 or e2 != 0 or e3 != 0 or e4 != 0:
    while um1 != um or um2 != um or um3 != um or um4 != um:
        if e != 0:
            # Definir x1 y x2, segun la compuerta AND 
            x1 = 1
            x2 = 0
            
            #Calcular valor esperado segun compuerta AND
            d = 0
            if x1== 0 and x2==0:
                d = 0
            elif x1== 0 and x2==1:
                d = 0
            elif x1== 1 and x2==0:
                d = 0
            elif x1== 1 and x2==1:
                d = 1
            else:
                print("Error en los pesos, valores deben ser 1 o 0")
            calculo(x1, x2, d)
        else:
            print("fin del programa")
            

    