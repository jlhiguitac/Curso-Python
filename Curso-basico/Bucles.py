def run():
    contador = 0
    potencia = 2**contador
    LIMITE = 1000000 #definición de una constante 
    while potencia < LIMITE:
        print("Dos elevado a: {} es igual a: {}".format(str(contador), str(potencia)))
        contador += 1
        potencia = 2**contador

if __name__== '__main__':
    run()
