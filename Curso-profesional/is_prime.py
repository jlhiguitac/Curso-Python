def signed_code(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Developer by Jorge Higuita :)")
    return wrapper


def is_prime(num: int) -> bool:
    iterador: int = 1
    while iterador <= num:
        if num % iterador == 0:
            if num == iterador:
                return True
            else:
                if iterador != 1:
                    return False
        iterador += 1

@signed_code
def run():
    num_Input: int = int(input("Input any number: "))
    print("Is " + str(num_Input) + " a prime number?...") 
    print(is_prime(num_Input))

if __name__ == '__main__':
    run()
