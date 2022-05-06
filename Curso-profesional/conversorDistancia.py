import numpy as np

# Variables globales


#Lista y diccionario global
abreviaturas_list = ["km", "mi", "UA", "al"]
super_dict_conversiones = {
        "km": [1, 0.621, 0.000000006684, 0.00000000000010569],
        "mi": [1.609, 1, 0.00000001075, 0.0000000000017],
        "UA": [149597870, 92900277, 1, 63242],
        "al": [9461000000000, 587528100000, 0.000015812, 1]
    }

def decConv(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        convertList = super_dict_conversiones.get(uniIn)
        factor = convertList[uniFdx]
        valueConvertion = round(n*factor, 1)
        if uniIndx > 1 or uniFdx > 1:
            print( str(n) + " " + abreviaturas_list[uniIndx] + " de Longitud equivalen a " + np.format_float_scientific(valueConvertion, precision = 2, exp_digits=3) + " " + abreviaturas_list[uniFdx])
        else:
            print( str(n) + " " + abreviaturas_list[uniIndx] + " de Longitud equivalen a " + str(valueConvertion) + " " + abreviaturas_list[uniFdx])
        print("Developed by Jorge Higuita :)")
    return wrapper

@decConv
def convertion(uniIndx, uniFdx):
    valueIn: float = float(input("Ingresa la longitud..."))
    assert type(valueIn) == float, "Debes escribir solo el valor númerico"
    return (valueIn)

def checkAbrev(uniIn):
    try:
        ndx = abreviaturas_list.index(uniIn)
    except:
        ndx = -1
    return ndx

if __name__=='__main__':
    uniIndx = -1
    uniFdx = -1
    print('''CONVERSOR DE GRANDES DISTANCIAS 
    Unidades de referencia: 
    km = kilometro, mi = milla, UA = unidad astronómica, al = año luz  ''')
    while (uniIndx < 0):
        uniIn: str = input("Ingresa la unidad de tu medida (abreviada)...")
        assert type(uniIn) == str, "Escribe la sigla abreviada"
        uniIndx = checkAbrev(uniIn)
        if uniIndx < 0:
            print("Debe ingresar una unidad valida...")
    while (uniFdx < 0):
        uniF: str = input("Ingresa la unidad a la cual quieres tu longitud (abreviada)...")
        assert type(uniF) == str, "Escribe la sigla abreviada"
        uniFdx = checkAbrev(uniF)
        if uniFdx < 0:
            print("Debe ingresar una unidad valida...")
    convertion(uniIndx, uniFdx)
    