import time

def Fibo_gen(max):
    a = True
    n1 = 0
    n2 = 1
    counter = 0

    while a == True:
        if counter == 0:
            counter += 1
            yield n1

        elif counter == 1:
            counter += 1
            yield n2
        else:
            if counter < max:
                aux = n1 + n2
                n1, n2 = n2 , aux
                counter += 1
                yield aux
            else:
                return StopIteration
        
    
if __name__=='__main__':
    max = int(input("Ingresa el el número máximo de elementos de la serie que quieres..."))
    assert  type(max) == int, "debes ingresar un número entero"
    fibonacci = Fibo_gen(max)
    for element in fibonacci:
        print (element)
        time.sleep(0.5)