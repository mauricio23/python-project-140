import random
from brain_games.cli import welcome_user 

def calc(name):

    print('What is the result of the expression?"')
    ciclos = 3
    print("hola")
    simbol = ['+', '-', '*']

    for i in range(ciclos):
        number1 = random.randint(2,20)
        number2 = random.randint(2,20)
        print("Question: "+ str(number1))
        respuesta = input("Your answer: ").lower()
        correcta = ""
        if simbol == '+':
            resultado_correcto = number1 + number2
        elif simbol == '-':
            resultado_correcto = number1 - number2
        elif simbol == '*':
            resultado_correcto = number1 * number2
        else: 
            print(f"{respuesta} is wrong answer ;(. Correct answer was {correcta}.")
            print(f"Let's try again, {name}!")
            exit()

        if i == 2:
            print(f"Congratulations,{name}!")


def main():

    print("Welcome to the Brain Games!")
    name = welcome_user()
    par_impar(name)


if __name__=="__main__":
    main() 