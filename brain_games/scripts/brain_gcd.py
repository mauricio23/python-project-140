import random
import math
from brain_games.cli import welcome_user 


def mcd(name):

    print('Find the greatest common divisor of given numbers')
    ciclos = 3
 
    for i in range(ciclos):
        number1 = random.randint(2, 20)
        number2 = random.randint(2, 20)
        print("Question: " + str(number1) + " " + str(number2))
        respuesta = input("Your answer: ").lower()
        resultado_correcto = math.gcd(number1, number2)
        
        if respuesta == str(resultado_correcto):
             print("Correct!")
        else: 
            print((
            f"'{respuesta}' is wrong answer ;(. "
            f"Correct answer was '{resultado_correcto}'."
            ))
            print(f"Let's try again, {name}!")
            exit()

        if i == 2:
            print(f"Congratulations, {name}!")


def main():

    name = welcome_user()
    mcd(name)


if __name__ == "__main__":
    main()
 