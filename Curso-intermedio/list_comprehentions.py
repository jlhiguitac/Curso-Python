def run():
        #squares = []
    #for i in range(1,101):
    #    if (i % 3) != 0:
    #        squares.append(i**2)
    #squares = [i**2 for i in range(1, 101) if i % 3 != 0] #para cada i en range se va guardar i**2 solo si cumple la condición
    #print(squares)
    reto = [i for i in range (1, 10009) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0] 
    odd = list(filter(lambda x: x % 2 == 0, reto))

    print(reto)
    print(odd)

def impNumeros():

    numero = 100
    iterador = 1
    while iterador <= numero:
        cuadrado = iterador * iterador
        ##print("el número {} es número primo".format(str(numero)))
        print("Numero: ", iterador, "-", " Cuadrado: " , cuadrado)
        iterador += 1




if __name__=='__main__':
    run()