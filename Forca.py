import pandas as pd

# Lista de 30 palavras
palavras = [
    'python', 'programação', 'data', 'ciência', 'inteligência', 'artificial',
    'análise', 'estatística', 'aprendizado', 'máquina', 'desenvolvimento', 'web',
    'big', 'dados', 'visualização', 'software', 'engenharia', 'computação',
    'algoritmo', 'estrutura', 'dados', 'backend', 'frontend', 'API', 'javascript',
    'java', 'html', 'css', 'github', 'repositório'
]

df = pd.DataFrame({'Palavra': palavras})

# Salvar o DataFrame em um arquivo CSV sem a coluna de índice
df.to_csv('palavras.csv', index=False)