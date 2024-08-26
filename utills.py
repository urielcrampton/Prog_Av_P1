from questions import *

import random
from typing import List, Tuple
from itertools import chain
from functools import wraps


def get_questions(file: str) -> List[Tuple[str, str, str, str]]:
    return read_csv(file)[1:]

def get_random_questions(questions: List[Tuple[str, str, str, str]]) -> List[Tuple[str, str, str, str]]:
    return random.sample(questions, 5)

def ask_question(question: Tuple[str, str, str, str]):
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    answer = input('Ingrese su respuesta: ')
    return True

def game(questions: List[Tuple[str, str, str, str]]) -> int:
    return sum([ask_question(question).value for question in questions])