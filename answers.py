from random import choice

piadas = [
    "Por que o livro de matemática ficou triste? Porque tinha muitos problemas!",
    "O que o zero disse para o oito? Que cinto maneiro!",
    "O que é um ponto amarelo no alto do prédio? Um milhonaire!",
    "O que uma impressora disse para a outra? Essa folha é sua ou é impressão minha?",
    "Qual é o animal mais antigo do mundo? A zebra… porque está em preto e branco!"
]

cumprimentos = {
    "olá bom dia": "Bom dia!",
    "bom dia": "Bom dia!",
    "boa tarde": "Boa tarde!",
    "boa noite": "Boa noite!",
    "tudo bem": "Sim, e você?",
    "como você está": "Estou bem, e você?",
    "como vai": "Estou ótima, e você?",
    "olá": "Olá",
    "oi": "Oi",
    'agradecido': "De nada",
    'muito obrigado': 'De nada',
    'me conte uma piada': f'É pra já: {choice(piadas)}',
    'conte uma piada': f'É pra já: {choice(piadas)}',
    'está me escutando': 'Sim, estou',
    'consegue me escutar': 'Sim, consigo'
}
