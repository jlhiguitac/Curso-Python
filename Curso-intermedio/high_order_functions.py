from functools import reduce


def run():
    
#filter
    my_list = [i for i in range (1, 11)] 
    #funcion Filter filtra los valores de la lista de acuerdo a la condición, devuelve true o false
    #el output de la función filter puede ser menor al arreglo entregado
    odd = list(filter(lambda x: x % 2 != 0, my_list))

    print("Funcion filter")
    print(my_list)
    print(odd)

#map
    my_list2 = [i for i in range(1, 6)]
    #función MAP realiza la operación que uno quiera recorriendo una lista, devuelve el valor de la lista 
    #el output de la función map es igual, no elimina elementos, solo los itera y aplica la condición
    squares = list(map(lambda x: x**2, my_list2))
    print("Funcion map")
    print(my_list2)
    print(squares)

#reduce
    my_list3 = [2, 2, 2, 2, 2]
    #la funcion REDUCE recibe 2 parametros, inicialmente los parametros 1 y 2 de la lista, luego los itera y avanza un parametro mas
    #donde el primer parametro(a) ahora es el resultado de la iteración anterior y el segundo es el nuevo parametro de la lista.
    all_multiplied = reduce(lambda a, b: a * b, my_list3)
    print("Funcion reduce")
    print(my_list3)
    print(all_multiplied)




if __name__=='__main__':
    run()