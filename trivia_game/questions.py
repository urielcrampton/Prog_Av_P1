import csv
from functools import lru_cache
import itertools
import random
from typing import List, Tuple, Dict
from itertools import chain

@lru_cache(maxsize=1)
def load_questions(file_path: str) -> List[Dict[str, str]]:
    """
    Carga las preguntas desde un archivo CSV.

    Args:
        file_path (str): Ruta al archivo CSV que contiene las preguntas.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios, cada uno representando una pregunta y sus opciones.
    """
    with open(file_path, mode='r', newline='', encoding='latin1') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def get_random_options(questions: List[Dict[str, str]], correct_answer: str) -> List[str]:
    """
    Obtiene opciones aleatorias, incluyendo la respuesta correcta.

    Args:
        questions (List[Dict[str, str]]): Lista de diccionarios que contienen las preguntas y respuestas.
        correct_answer (str): Respuesta correcta que debe ser incluida en las opciones.

    Returns:
        List[str]: Lista de opciones aleatorias, incluyendo la respuesta correcta.
    """
    incorrect_answers = [q['Answer'] for q in questions if q['Answer'] != correct_answer]
    if len(incorrect_answers) < 2:
        # Si hay menos de 2 respuestas incorrectas, toma todas y añade el correcto
        return incorrect_answers + [correct_answer]
    random.shuffle(incorrect_answers)
    return list(itertools.chain(random.sample(incorrect_answers, min(2, len(incorrect_answers))), [correct_answer]))

def shuffle_options(options: List[str]) -> List[str]:
    """
    Mezcla el orden de las opciones.

    Args:
        options (List[str]): Lista de opciones a mezclar.

    Returns:
        List[str]: Lista de opciones con el orden mezclado.
    """
    random.shuffle(options)
    return options

def get_random_questions_gen(questions: List[Dict[str, str]], n: int):
    """
    Generador que devuelve n preguntas aleatorias del conjunto de preguntas.

    Args:
        questions (List[Dict[str, str]]): Lista de diccionarios que contienen las preguntas disponibles.
        n (int): Número de preguntas aleatorias a seleccionar.

    Yields:
        Dict[str, str]: Una pregunta aleatoria del conjunto de preguntas.
    """
    selected = random.sample(questions, n)
    for q in selected:
        yield q
