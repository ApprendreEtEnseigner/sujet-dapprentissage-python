from random import randint


questions = [
    {
    'question': 'Quelle est la capitale de la France?',
    'reponses': ['Paris', 'Londres', 'Berlin', 'Madrid'],
    'bonneReponse': 'Paris'
    },
    
    {
    'question': 'Quel est le plus grand océan du monde?',
    'reponses': ['Atlantique', 'Pacifique', 'Indien', 'Arctique'],
    'bonneReponse': 'Pacifique'
    }
]


def afficherQuestion(questions):
    index = randint(0, len(questions)-1)
    print(index)
    question = questions[index]
    
    print(question['question'])

print(afficherQuestion(questions))