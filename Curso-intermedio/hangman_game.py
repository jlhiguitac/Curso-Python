import random
import os
import sys
from xmlrpc.client import boolean

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def read(route: str):#función para leer archivos 
    words = [] #lista de palabras para consultar
    #aca debajo abro el archivo data para sacar una palabra, y creo una lista llamada words
    with open(route, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line)
    return words

def write(dict): #funcion para escribir archivos txt
    with open("./archivos/marcador.txt", "w", encoding="utf-8") as f:
        for key, value in dict.items():
            f.write(key + ":" + value)
            f.write("\n")

def win_board(name, points):# funcion para manejar almacenar los marcadores
    dict_users = {}
    sorted_dict = {}
    word = read("./archivos/marcador.txt")
    for values in word:
        #list_users = values[0:values.find(":")] 
        #list_points = values[values.find(":"): values.find("\n")]
        dict_users [values[0:values.find(":")]] = values[values.find(":") + 1 : values.find("\n")]
    dict_users[name] = str(points)
    sorted_dict = sorted(dict_users.items(), key = lambda x: x[1], reverse = True)
    #print(sorted_dict)
    write(dict_users)
    print("Récord de puntaje: ")
    for key, value in sorted_dict:
        if key == name:
            print(key.upper() + ": " + value + "%")
        else:
            print(key + ": " + value + "%")
    
def word_process():# Función para seleccionar cada palabra
    char_list = [] #lista de letras de la palabra a buscar
    empty_list = [] #lista de vacíos para mostrar en pantalla
    key_word: str = ""
    sec_word: str = ""
    words = read("./archivos/data.txt")
    #saco una palabra aleatoriamente de la lista words
    key_word = words[random.randint(0,170)]
    #le quito el salto de linea
    sec_word = key_word[0: int(len(sec_word))-1]
    #le quito las tildes
    sec_word = normalize(sec_word)
    #creo dos listas, una con los caracteres de la palabra y la otra con los espacios en blanco
    for index in range (len(sec_word)):
        char_list.append(sec_word[index])
        empty_list.append("_")
    return char_list, empty_list, key_word
   
def show_end_message(condition, sec_word, name, trying, attempts):
    os.system("cls")
    points: float = 0.0
    if (condition):
        print("¡Ganaste! la palabra era "+ sec_word.upper())
        print("Lo hiciste en: " + str(trying) +" intentos \n")
        if trying <= attempts:
            points = (trying/attempts)*100
        else:
            points = int(100 - (trying/(attempts + 4))*100)
        print("Obtuviste: " + str(points) + "% de asertividad \n")
        win_board(name, points)
    else:
        print("Perdiste, la palabra era "+ sec_word.upper())
    print("""
    Quieres seguir jugando? presiona "y" y luego ENTER
    Sí no, presiona cualquier tecla seguido de ENTER...
    """)

def console(name, char_list, empty_list, sec_word):#función con la logica del juego
    exit_condition: boolean = False
    word_empty_list = ""
    trying: int = 0
    attempts: int = len(sec_word) - 1
    for i in empty_list:
        word_empty_list = word_empty_list + i
    print("Bienvenido: " + name)
    print("¡ADIVINA LA PALABRA!")
    print(word_empty_list)
    while True:
        try:
            iterable_char = normalize(input("Ingresa una letra: ").lower())
            if len(iterable_char)>1:
                raise ValueError
            os.system("cls")
            print("Bienvenido: " + name)
            print("¡ADIVINA LA PALABRA!")
            for i, char in enumerate(char_list):
                if iterable_char == char:
                    empty_list[i] = iterable_char 
                    word_empty_list = ""
                    for i in empty_list:
                        word_empty_list = word_empty_list + i
            trying += 1       
            print(word_empty_list)
            if(trying == (attempts + 4)):
                show_end_message(False, sec_word, name, trying, attempts)
                exit_condition = True
            if empty_list == char_list:
                show_end_message(True, sec_word, name, trying, attempts)
                exit_condition = True
            if exit_condition:
                reInit = input("Quieres seguir jugando?: ")
                if (reInit == "y"):
                    os.system("cls")
                    char_list, empty_list, sec_word = word_process()
                    exit_condition = False
                    word_empty_list = ""
                    trying = 0
                    attempts = len(sec_word)
                    for i in empty_list:
                        word_empty_list = word_empty_list + i
                    print("Bienvenido: " + name)
                    print("¡ADIVINA LA PALABRA!")
                    print(word_empty_list)
                else:
                    sys.exit("GAME OVER!!!")       
        except ValueError:
            print("Debes ingresar solo una letra")
        
def init_users():
    os.system("cls")
    print ("""Bienvenido al HangMan Game by Negrito

Los usuarios repetidos se sobreescriben.

Rompe el record y diviértete!!! \n""")
    name: str = input("Escribe tu nombre: ")
    return name

def run():
    name: str = init_users()
    os.system("cls")
    char_list, empty_list, key_word = word_process()
    console(name,char_list, empty_list, key_word)

if __name__=="__main__":
    run()