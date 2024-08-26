from questions import read_csv  # Importar explícitamente la función read_csv

import random
from typing import List, Tuple
from itertools import chain
from functools import wraps

def get_questions(file: str) -> List[Tuple[str, str, str, str]]:
    return read_csv(file)[1:]  # Lee las preguntas desde el CSV

def get_random_questions(questions: List[Tuple[str, str, str, str]]) -> List[Tuple[str, str, str, str]]:
    return random.sample(questions, 5)  # Selecciona 5 preguntas al azar

def validate_answer(func):
    @wraps(func)
    def wrapper(question):
        correct_answer = question[1]
        user_answer = func(question)
        return 10 if user_answer == correct_answer else 0  # Suma 10 puntos si es correcto
    return wrapper

@validate_answer
def ask_question(question: Tuple[str, str, str, str]) -> str:
    print(question[0])  # Muestra la pregunta
    for i, option in enumerate(question[1:], start=1):
        print(f"{i}. {option}")
    answer = input('Ingrese el número de su respuesta: ')
    return question[int(answer)]

def game(questions: List[Tuple[str, str, str, str]]) -> int:
    return sum(ask_question(question) for question in questions)  # Suma los puntajes
