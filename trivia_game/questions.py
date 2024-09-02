import csv
import itertools
import random
from typing import List, Tuple, Dict
from itertools import chain

def load_questions(file_path: str) -> List[Dict[str, str]]:
    """Load questions from a CSV file."""
    with open(file_path, mode='r', newline='', encoding='latin1') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def get_random_options(questions: List[Dict[str, str]], correct_answer: str) -> List[str]:
    """Get random options including the correct one."""
    incorrect_answers = [q['Answer'] for q in questions if q['Answer'] != correct_answer]
    random.shuffle(incorrect_answers)
    return list(itertools.chain(random.sample(incorrect_answers, 2), [correct_answer]))


def shuffle_options(options: List[str]) -> List[str]:
    """Shuffle the order of options."""
    random.shuffle(options)
    return options

def get_random_questions_gen(questions: List[Dict[str, str]], n: int):
    """Generator to yield n random questions from the question pool."""
    selected = random.sample(questions, n)
    for q in selected:
        yield q

