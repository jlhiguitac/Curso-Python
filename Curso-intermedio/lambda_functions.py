def palindrome(string):
    #def palindome_old(string):
    #    return string == string[::-1]
#es lo mismo, la funcion lambda es anonima, y se invoca mediante una variable y returna verdadero
#o falso, se invoca a traves de la variable palindromo un objeto tipo funcion
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        
    except ValueError as ve:
        print (ve)
        return False
    
    else:
        return print (string == string[::-1])
            



if __name__ =='__main__':
    palindrome(input("Ingresa una palabra: "))
    
    