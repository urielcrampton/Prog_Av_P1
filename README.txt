Juego de Trivia en Python
Este proyecto es un juego de trivia desarrollado en Python que utiliza varios conceptos avanzados de programación funcional. A continuación, se detallan los conceptos implementados y dónde se encuentran en el código.

Como ejecutarlo:
python -m trivia_game.main

Conceptos Implementados
1. Recursión
    Ubicación: main.py en la función ask_question_recursively.
    Descripción: La recursión se utiliza en la función ask_question_recursively para permitir que el juego vuelva a preguntar al usuario cuando se ingresa una respuesta inválida, hasta que se ingrese una respuesta válida.
2. Generadores
    Ubicación: generators.py en la función question_generator.
    Descripción: La función question_generator implementa un generador que produce preguntas una por una, lo que permite procesar grandes conjuntos de preguntas sin cargarlas todas en memoria al mismo tiempo.
3. Listas por comprensión
    Ubicación: main.py en la función play_game.
    Descripción: Se utiliza una lista por comprensión en la línea correct_answers = sum([ask_question_recursively(q, questions) for q in selected_questions]) para iterar sobre las preguntas seleccionadas y calcular el número de respuestas correctas de forma concisa y eficiente.
4. Decoradores
    Ubicación: decorators.py en la función timeit.
    Descripción: El decorador timeit mide y muestra el tiempo de ejecución de la función play_game. Se aplica sobre la función para envolverla y añadir funcionalidad sin modificar su código original.
5. itertools.chain
    Ubicación: questions.py en la función get_random_options.
    Descripción: itertools.chain se utiliza para concatenar las opciones de respuesta correctas e incorrectas en una sola lista antes de barajarlas y presentarlas al usuario.
6. Mónadas
    Ubicación: monads.py en la clase Maybe.
    Descripción: La clase Maybe implementa un patrón de mónada, que se usa para manejar valores que pueden o no existir (es decir, valores opcionales). Proporciona métodos como bind para encadenar operaciones de manera segura sobre estos valores.
7. Funciones lambda
    Ubicación: utils.py en la función evaluate_answer.
    Descripción: Se utiliza una función lambda para comparar la respuesta del usuario con la respuesta correcta en la función evaluate_answer, permitiendo evaluar las respuestas de manera compacta y eficiente.

Estructura del Proyecto
    main.py: Contiene la lógica principal del juego, incluida la interacción con el usuario y la ejecución del flujo del juego.
    decorators.py: Define decoradores reutilizables, como timeit.
    questions.py: Maneja la carga y selección de preguntas, así como la generación de opciones de respuesta.
    utils.py: Contiene funciones de utilidad como calculate_score y evaluate_answer.
    monads.py: Implementa el concepto de mónadas a través de la clase Maybe.
    generators.py: Define generadores utilizados para la producción de preguntas