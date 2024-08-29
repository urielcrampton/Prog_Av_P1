from typing import List

def calculate_score(correct_answers: int, points_per_question: int = 10) -> int:
    """Calculate the score based on correct answers."""
    return correct_answers * points_per_question

def evaluate_answer(user_answer: str, correct_answer: str) -> bool:
    """Check if the user's answer is correct."""
    return user_answer.lower() == correct_answer.lower()
