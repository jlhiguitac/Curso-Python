def imc_grade(func):
    def wrapper(*args, **kwargs):
        n= func(*args, **kwargs)
        match n:
            case x if n > 15 and n < 16.1:
                print("IMC= " + str(x) +  " Delgadez Severa. Debe alimentarse mejor")
            case n if n > 16 and n < 18.6 :
                print("IMC= " + str(x) +  " Delgado. Revise su Alimentación y haga ejercicios")
            case n if n > 18.5 and n < 25.1 :
                print("IMC= " + str(x) +  " Ud. está saludable. Siga asi, cuide su alimentacion y haga ejercicios")
            case n if n > 25 and n < 30:
                print("IMC= " + str(x) +  " Ud. tiene sobrepeso. Comience a hacer ejercicios")
            case n if n > 29.9 and n < 35:
                print("IMC= " + str(x) +  " Ud. tiene obesidad moderada. Debe hacer ejercicios y revisar sus hábitos alimenticios")
            case n if n > 34.9 and n < 40:
                print("IMC= " + str(x) +  " Ud. tiene obesidad severa. Debe hacer ejercicios, cambiar sus hábitos alimenticios y buscar ayuda")
            case n if n > 39.9:
                print("IMC= " + str(x) +  " La obesidad no es buena. Busque ayuda de inmediato. Está a  tiempo de mejorar")
            
    return wrapper

@imc_grade
def calc_imc() -> float:
    peso: float = float(input("Inserte su peso en Kg: "))
    assert type(peso) == float, "Sólo puedes usar números"
    estatura: float = float(input("Inserte su estatura en metros: "))
    assert type(estatura) == float, "Sólo puedes usar números"    
    return round(peso/estatura**2,1)


calc_imc()