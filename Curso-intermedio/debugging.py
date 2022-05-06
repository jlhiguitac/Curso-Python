def divisores(num):
    divisores = [x for x in range(1, num + 1 ) if num % x == 0]
    return divisores

def run():
    while True:
        try:
            num = int(input("ingresa un numero: "))
            if num <= 0:
                raise ValueError
            print(divisores(num))
            print("Terminó mi programa...")
            break
        except ValueError:
            print("Debes ingresar un número entero")

    

    
if __name__=="__main__":
    run()

