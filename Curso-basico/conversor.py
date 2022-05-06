def conversion_pesos(tipo_pesos,valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de pesos a dolares bien perron papá 💸💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos


Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    conversion_pesos("colombianos", 3875)
elif opcion == 2:
    conversion_pesos("argentinos", 100.07)
elif opcion == 3:
    conversion_pesos("mexicanos", 20.32)
else:
    print("Pinche bato cabrón escogiste una opción inválida")


