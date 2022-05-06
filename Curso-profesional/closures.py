def make_multiplier(x): #recibe un parametro x
    def multiplier(n): #recibe un parametro n pero recuerda un parametro x anterior
        return x * n #coge del scopus anterior el parametro x

    return multiplier #retorna la función anidada,
    #se crea una especie de instancia a la función anidada

times10 = make_multiplier(10) 
#se crea una función tipo y se le asigna el parametro x = 10
#aun no sabemos cuanto vale n
times4 = make_multiplier(4)

print(times10(3))
#estamos llamando a la función times10 que tiene como parametro x=10 y le estamos
#dando el valor de n = 3
print(times4(4))
print(times10(times4(2))) 