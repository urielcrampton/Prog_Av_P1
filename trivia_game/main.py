from typing import List, Dict
from .questions import load_questions, get_random_questions, shuffle_options, get_random_options
from .utils import calculate_score, evaluate_answer
from .decorators import timeit
import itertools

@timeit
def play_game(questions: List[Dict[str, str]], num_questions: int) -> int:
    selected_questions = get_random_questions(questions, num_questions)
    correct_answers = sum([ask_question(q, questions) for q in selected_questions])
    return calculate_score(correct_answers)

def ask_question(question: Dict[str, str], all_questions: List[Dict[str, str]]) -> int:
    options = get_random_options(all_questions, question['Answer'])
    shuffled_options = shuffle_options(options)
    
    print(f"Category: {question['Category']}")
    print(f"Question: {question['Question']}")
    
    for i, option in enumerate(shuffled_options):
        print(f"{i + 1}. {option}")
    
    user_answer = input("Your answer (1/2/3): ")
    
    correct = evaluate_answer(shuffled_options[int(user_answer) - 1], question['Answer'])
    return 1 if correct else 0

if __name__ == "__main__":
    questions = load_questions(r'data\JEOPARDY_CSV.csv')
    score = play_game(questions, 5)
    print(f"Your final score is: {score}")
