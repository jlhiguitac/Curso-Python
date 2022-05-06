def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Jorge", "Pépe", "Miguel"]
    # con "w" se sobreescribe, con "a" no se sobrescribe
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__=="__main__":
    run()
