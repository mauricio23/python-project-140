import random
from brain_games.cli import welcome_user 


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ciclos = 3
    for i in range(ciclos):
        number1 = random.randint(2,20)
        print("Question: "+ str(number1))
        respuesta = input("Your answer: ").lower()
        resultado_correcto = "yes" if es_primo(number1) else "no"
        if respuesta == resultado_correcto:
             print("Correct!")
        else: 
            print(f"{respuesta} is wrong answer ;(. Correct answer was {str(resultado_correcto)}.")
            print(f"Let's try again, {name}!")
            exit()

        if i == 2:
            print(f"Congratulations, {name}!")


def main():

    print("Welcome to the Brain Games!")
    name = welcome_user()
    prime(name)


if __name__=="__main__":
    main()
 