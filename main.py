#Desarrollar un juego de trivia en Python usando programación funcional. Debe utilizar, de
#los conceptos vistos en el curso, como mínimo:
#1. recursión,
#2. generadores,
#3. listas por comprensión,
#4. decoradores,
#5. itertools.chain,
#6. mónadas,
#7. funciones lambda
#Puede agregar otros conceptos vistos en el curso o que usted haya investigado por cuenta
#propia, de programación funcional. El código debe generar documentación.

#Las preguntas de la trivia las debe importar de un archivo .csv como el que se adjunta.
#Si desea cambiar las preguntas puede hacerlo, pero debe respetar el formato del archivo
#(cada pregunta tiene 3 opciones de respuestas posibles y solo una es correcta).
#El juego debe sortear 5 preguntas al azar de las 20 posibles, mostrarle al usuario cada
#pregunta con sus opciones, y si el usuario acierta suma 10 puntos. Al finalizar, el juego le
#informa al usuario su puntaje.
#Se espera que todo el código esté tipado, que se utilice una estructura de proyecto acorde y
#que haya una cobertura de tests de al menos 85%.


import csv
import random
from typing import List, Tuple
from itertools import chain
from functools import wraps
from PyMonad import Maybe, Just, Nothing


def read_csv(file: str) -> List[Tuple[str, str, str, str]]:
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [(row[0], row[1], row[2], row[3]) for row in reader]
    
def get_questions(file: str) -> List[Tuple[str, str, str, str]]:
    return read_csv(file)[1:]

def get_random_questions(questions: List[Tuple[str, str, str, str]]) -> List[Tuple[str, str, str, str]]:
    return random.sample(questions, 5)

def ask_question(question: Tuple[str, str, str, str]) -> Maybe:
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    answer = input('Ingrese su respuesta: ')
    return Just(10) if answer == question[3] else Nothing()

def game(questions: List[Tuple[str, str, str, str]]) -> int:
    return sum([ask_question(question).value for question in questions])

def main(file: str) -> None:
    questions = get_random_questions(get_questions(file))
    score = game(questions)
    print(f'Su puntaje es: {score}')

if __name__ == '__main__':
    main('JEOPARDY_CSV.csv')

