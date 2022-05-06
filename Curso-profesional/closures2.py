#Hola 3 -> Hola hola Hola

#Se crea una función que tiene una función adentro, lo que se hace es que
#al invocar la funcipon anterior se crea una función, la cual va a recibir a futuro
#un parametro de la función anidada para poder funcionar
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_n = make_repeater_of(int(input("Ingresa el numero de repeticiones...")))
    print(repeat_n(input("Ingresa un texto...: ")))

if __name__ == '__main__':
    run()