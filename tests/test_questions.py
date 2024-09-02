import unittest
import csv
from trivia_game.questions import load_questions, get_random_options, shuffle_options, get_random_questions_gen
from typing import List, Dict
import os

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_data.csv'
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Show_Number', 'Air_Date', 'Round', 'Category', 'Value', 'Question', 'Answer'])
            writer.writeheader()
            writer.writerow({
                'Show_Number': '4680',
                'Air_Date': '12/31/04',
                'Round': 'Jeopardy!',
                'Category': 'HISTORY',
                'Value': '$200',
                'Question': 'For the last 8 years of his life, Galileo was under house arrest for espousing this man\'s theory',
                'Answer': 'Copernicus'
            })
            writer.writerow({
                'Show_Number': '4681',
                'Air_Date': '01/01/05',
                'Round': 'Double Jeopardy!',
                'Category': 'SCIENCE',
                'Value': '$400',
                'Question': 'The chemical symbol for gold',
                'Answer': 'Au'
            })

    def test_load_questions(self):
        questions = load_questions(self.file_path)
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]['Question'], 'For the last 8 years of his life, Galileo was under house arrest for espousing this man\'s theory')

    def test_get_random_options(self):
        questions = load_questions(self.file_path)
        correct_answer = 'Copernicus'
        options = get_random_options(questions, correct_answer)
        self.assertIn(correct_answer, options)
        self.assertEqual(len(options), 2)

    def test_shuffle_options(self):
        options = ['Option A', 'Option B', 'Option C']
        # Realizar el shuffle 3 veces y verificar que los resultados no sean iguales
        shuffled_results = set()
        for _ in range(3):
            shuffled = shuffle_options(options[:])  # Copia de la lista original
            shuffled_results.add(tuple(shuffled))  # Convertir a tupla para almacenar en un set

        # Verifica que se hayan obtenido al menos 2 resultados diferentes
        self.assertGreater(len(shuffled_results), 1, "El shuffle no parece estar funcionando correctamente")


    def test_get_random_questions_gen(self):
        questions = load_questions(self.file_path)
        generator = get_random_questions_gen(questions, 1)
        selected = list(generator)
        self.assertEqual(len(selected), 1)
        self.assertIn('Question', selected[0])

    def tearDown(self):
        os.remove(self.file_path)

if __name__ == '__main__':
    unittest.main()
