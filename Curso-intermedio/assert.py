def divisores(num):
    divisores = [x for x in range(1, num + 1 ) if num % x == 0]
    return divisores

def run():
    num = input("ingresa un numero: ")
    assert num.isnumeric() and int(num) > 0, "Ingresa solo numeros positivos"
    print(divisores(int(num)))
    print("Terminó mi programa...")
        

    

    
if __name__=="__main__":
    run()