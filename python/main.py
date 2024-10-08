import random

# Perguntas e respostas sobre Python
questions = [
    {
        "question": "Qual é a função para imprimir algo na tela em Python?",
        "options": ["a) print()", "b) echo()", "c) printf()", "d) write()"],
        "answer": "a"
    },
    {
        "question": "Qual dessas estruturas de dados é imutável em Python?",
        "options": ["a) Lista", "b) Dicionário", "c) Conjunto", "d) Tupla"],
        "answer": "d"
    },
    {
        "question": "Como você cria um comentário em Python?",
        "options": ["a) // Comentário", "b) <!-- Comentário -->", "c) # Comentário", "d) /* Comentário */"],
        "answer": "c"
    },
    {
        "question": "Qual dessas palavras-chave é usada para criar uma função em Python?",
        "options": ["a) func", "b) def", "c) function", "d) lambda"],
        "answer": "b"
    },
    {
        "question": "Como você inicializa um dicionário em Python?",
        "options": ["a) {}", "b) []", "c) ()", "d) set()"],
        "answer": "a"
    },
    {
        "question": "Qual dessas bibliotecas é usada para análise de dados em Python?",
        "options": ["a) NumPy", "b) Pandas", "c) Matplotlib", "d) Todas as anteriores"],
        "answer": "d"
    },
    {
        "question": "Qual a função usada para obter o tamanho de uma lista em Python?",
        "options": ["a) size()", "b) length()", "c) len()", "d) count()"],
        "answer": "c"
    },
    {
        "question": "Qual dessas palavras-chave é usada para lidar com exceções em Python?",
        "options": ["a) try", "b) except", "c) finally", "d) Todas as anteriores"],
        "answer": "d"
    }
]

# Função para fazer perguntas
def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    
    answer = input("Escolha sua resposta (a, b, c, d): ").lower()
    return answer == question["answer"]

# Função principal do jogo
def python_trivia():
    print("Bem-vindo ao Jogo de Perguntas e Respostas sobre Python!\n")
    score = 0
    random.shuffle(questions)  # Embaralha as perguntas
    
    for question in questions:
        if ask_question(question):
            print("Correto!")
            score += 1
        else:
            print(f"Errado! A resposta correta era: {question['answer']}")
    
    print(f"\nVocê acertou {score} de {len(questions)} perguntas.")

# Inicia o jogo
python_trivia()
