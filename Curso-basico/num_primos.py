# def es_primo(numero):
#     contador = 0
#     for i in range (1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return  True
#     else:
#         return False


def run():
    # numero = int(input("Escribe un número: "))
    # if es_primo(numero):
    #     print("Es primo")
    # else:
    #     print("No es primo")
    numero = int(input("Ingresa un numero: "))
    iterador = 1
    while iterador <= numero:
        if numero % iterador == 0:
            if (numero == iterador):
                print("el número {} es número primo".format(str(numero)))
                break
            else:
                if iterador != 1:
                    print("el número {} no es número primo".format(str(numero)))
                    break
        iterador += 1


if __name__=="__main__":
    run()