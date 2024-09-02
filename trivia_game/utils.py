from typing import List

def calculate_score(correct_answers: int, points_per_question: int = 10) -> int:
    """Calculate the score based on correct answers."""
    return correct_answers * points_per_question

