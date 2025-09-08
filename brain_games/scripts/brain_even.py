import random
from brain_games.cli import welcome_user 

def par_impar():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    ciclos = 3
    for i in range(ciclos):
        numero = random.randint(1,10)
        print("Question: "+ str(numero))
        respuesta = input("Your answer: ").lower()
        correcta = ""
        if numero % 2 == 0:
            correcta = "yes"
        else: correcta = "no" 
        
        if respuesta == correcta:
            print("Correct!")


def main():

    print("Welcome to the Brain Games!")
    welcome_user()
    par_impar()


if __name__=="__main__":
    main() 