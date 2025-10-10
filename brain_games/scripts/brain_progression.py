import random
from brain_games.cli import welcome_user 

def generar_progresion(a1, d, n):
  return [a1 + i * d for i in range(n)]

def juego_aritmetico(name):

    print('What number is missing in the progression?"')
    ciclos = 3

    for i in range(ciclos):
        # Parámetros aleatorios
        a1 = random.randint(1, 10)     # primer término
        d = random.randint(2, 5)       # diferencia
        n = 10                         # longitud de la progresión
        progresion = generar_progresion(a1, d, n)

        # Número oculto
        pos = random.randint(0, n - 1)
        respuesta_correcta = progresion[pos]

        # Reemplazar por ".."
        progresion[pos] = ".."
        print("Question: "+ " ".join(map(str, progresion)))
        respuesta = input("Your answer: ").lower()
        
       
        if respuesta == str(respuesta_correcta):
             print("Correct!")
        else: 
            print(f"{respuesta} is wrong answer ;(. Correct answer was {str(respuesta_correcta)}.")
            print(f"Let's try again, {name}!")
            exit()

        if i == 2:
            print(f"Congratulations, {name}!")


def main():

    print("Welcome to the Brain Games!")
    name = welcome_user()
    juego_aritmetico(name)


if __name__=="__main__":
    main() 