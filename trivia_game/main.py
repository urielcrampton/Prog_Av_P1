from typing import List, Dict
from .questions import load_questions, get_random_questions_gen, shuffle_options, get_random_options
from .utils import calculate_score
from .decorators import timeit
import itertools

def ask_question_recursively(question: Dict[str, str], shuffled_options: List[str]) -> int:
    """Function to ask a question and handle user input with recursion."""
    
    print(f"Category: {question['Category']}")
    print(f"Question: {question['Question']}")
    
    for i, option in enumerate(shuffled_options):
        print(f"{i + 1}. {option}")
    
    user_answer = input("Your answer (1/2/3): ")
    
    if user_answer not in {'1', '2', '3'}:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return ask_question_recursively(question, shuffled_options)  # Recurence
    
    correct = lambda answer: answer.lower() == question['Answer'].lower()

    if correct(shuffled_options[int(user_answer) - 1]):
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer was: {question['Answer']}\n")
        return 0


@timeit
def play_game(questions: List[Dict[str, str]], num_questions: int) -> int:
    """Function to play the game by asking a series of random questions."""
    selected_questions = get_random_questions_gen(questions, num_questions)
    correct_answers = sum([ask_question_recursively(q, shuffle_options(get_random_options(questions, q['Answer']))) for q in selected_questions])
    return calculate_score(correct_answers)




if __name__ == "__main__":
    questions = load_questions(r'data\JEOPARDY_CSV.csv')
    score = play_game(questions, 5)
    print(f"Your final score is: {score}")
