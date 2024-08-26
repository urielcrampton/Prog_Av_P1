from utills import *

def main(file: str) -> None:
    questions = get_random_questions(get_questions(file))
    score = game(questions)
    print(f'Su puntaje es: {score}')

if __name__ == '__main__':
    main('JEOPARDY_CSV.csv')
