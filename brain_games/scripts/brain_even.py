import random
from brain_games.cli import welcome_user 

def par_impar(name):

    print('Answer "yes" if the number is even, otherwise answer "no".')
    ciclos = 3
    print("hola")

    for i in range(ciclos):
        numero = random.randint(2,10)
        print("Question: "+ str(numero))
        respuesta = input("Your answer: ").lower()
        correcta = ""

        if numero % 2 == 0:
            correcta = "yes"
        else: correcta = "no" 
       
        if respuesta == correcta:
            print("Correct!")
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