def read(route: str):#función para leer archivos 
    words = [] #lista de palabras para consultar
    #aca debajo abro el archivo data para sacar una palabra, y creo una lista llamada words
    with open(route, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line)
    return words

def write(dict): #funcipon para escribir archivos txt
    with open("./archivos/marcador.txt", "w", encoding="utf-8") as f:
        for key, value in dict.items():
            f.write(key + ": " + value)
            f.write("\n")


def run():
    dict_users = {}
    word = read("./archivos/marcador.txt")
    name: str = input("nombre: ")
    points: str = "25"
    #list_users = list(filter(lambda values: values[0:values.find(":")], word))
    print(word)
    for values in word:
        #list_users = values[0:values.find(":")] 
        #list_points = values[values.find(":"): values.find("\n")]
        dict_users[values[0:values.find(":")] ] = values[values.find(":") + 1 : values.find("\n")]
        print(dict_users.items())
    dict_users[name] = str(points)
    print(sorted(dict_users.items(), key=lambda x: x[1]))
     
if __name__=="__main__":
    run()