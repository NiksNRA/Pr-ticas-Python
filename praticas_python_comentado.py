# Práticas Completas em Python
# Autor: [Teu Nome Aqui]
# Descrição: Exercícios variados com foco em lógica, vetores, conjuntos e distância euclidiana para classificação.

# ----------------------------
# Célula 1
# Soma e exponenciação
10 + 20 + 30**3

# ----------------------------
# Célula 2
# Expressão aritmética com variável
x = 5
3 * x + 10

# ----------------------------
# Célula 3
# Cálculo de comissão
comissao = 10 / 100
50000 * comissao + 750

# ----------------------------
# Célula 4
# Verifica se a meta mensal foi atingida
comissao = 10 / 100
mensal = (50000 * comissao + 750 >= 6000)

# ----------------------------
# Célula 5
# Expressão do tipo ax + b
x = 30
5 * x + 10

# ----------------------------
# Célula 6
# Outro exemplo de ax + b
x = 5
10 * x

# ----------------------------
# Célula 7
# Comparação de duas expressões
x = 30
(50 * x + 35) < (75 * x + 36)

# ----------------------------
# Célula 8
# Proporção de linguagens compradas
lista = {'C', 'java', 'javascript', 'ruby', 'php', 'python', 'Kotlin', 'Golang', 'html', 'css'}
buyer = {'html', 'css', 'javascript'}
quantidade = len(lista)
quantidade2 = len(buyer)
(quantidade2 / quantidade)

# ----------------------------
# Célula 9
# Razão inversa: total sobre compradas
len(lista) / len(buyer)

# ----------------------------
# Célula 10
# Soma de idades com conjunto
idade = {22, 42, 55, 19, 99, 19, 12}
total = sum(idade)
print(total)

# ----------------------------
# Célula 11
# Acesso a valor em lista
idade = [22, 42, 55, 19, 99, 19, 12]
print(idade[4])

# ----------------------------
# Célula 13
# Cálculo de desconto e checagem de filme assistido
mensal = 30
vouncher = mensal * (10 / 100)
total = mensal - vouncher
filmes = ['gigantes de aco', 'o poderoso chefao', 'cidade kane', 'star wars', 'titanic', 'lista de schindle', 'casablanca', 'senhor dos aneis', 'forrest gump', 'pulp fiction']
assistiu = ['gigantes de aco']
nao_assistiu = len(assistiu) > 0
nao_assistiu * mensal

# ----------------------------
# Célula 14
# Outro teste de assinatura e valor alternativo
mensal = 40
vouncher = mensal * (10 / 100)
total = mensal - vouncher
filmes = ['a', 'o poderoso chefao', 'cidade kane', 'star wars', 'titanic', 'lista de schindle', 'casablanca', 'senhor dos aneis', 'forrest gump', 'pulp fiction']
assistidos = []
assistiu = len(assistidos) > 0
(assistiu * mensal) + (not assistiu) * 36

# ----------------------------
# Célula 15
# Carrinho e cálculo de desconto
carrinho = {"A", "Camiseta", "Tenis", "Notebook", "Cafeteira", "Fone de ouvido", "Smartphone", "Mochila", "Livro", "Relogio", "Camera fotografica"}
comprados = {"A", "Camera fotografica"}
total = 500
desconto_vazio = 500 * (10 / 100)
desconto_cheio = 500 * (15 / 100)

# ----------------------------
# Célula 16
# Comparação entre vetores binários com distância euclidiana
import numpy as np

universo = {'html', 'css', 'javascript', 'C', 'java', 'python'}
usuario_A = {'html', 'css', 'javascript'}
usuario_B = {'C', 'java'}

vetor_A = np.isin(list(universo), list(usuario_A)).astype(int)
vetor_B = np.isin(list(universo), list(usuario_B)).astype(int)

from scipy.spatial.distance import euclidean
print("Distância Euclidiana:", euclidean(vetor_A, vetor_B))

intersecao = usuario_A & usuario_B
uniao = usuario_A | usuario_B
similaridade_jaccard = len(intersecao) / len(uniao)
print("Similaridade Jaccard:", similaridade_jaccard)

# ----------------------------
# Célula 17
# Comparando flores usando vetores e distância
import numpy as np

girasol = {'caule', 'meio'}
rosa = {'espinhos', 'caule', 'meio'}
florzinha = {'caule', 'espinhos'}

universo = girasol.union(rosa).union(florzinha)

un = np.isin(list(universo), np.array(list(universo))).astype(int)
um_girasol = np.isin(list(universo), np.array(list(girasol))).astype(int)
um_rosa = np.isin(list(universo), np.array(list(rosa))).astype(int)
um_florzinha = np.isin(list(universo), np.array(list(florzinha))).astype(int)

girasol_rosa = np.linalg.norm(um_girasol - um_rosa)
rosa_florzinha = np.linalg.norm(um_florzinha - um_rosa)
florzinha_girasol = np.linalg.norm(um_florzinha - um_girasol)

resultado = ((rosa_florzinha < florzinha_girasol) and (rosa_florzinha < girasol_rosa)) * 'rosa florzinha' + \
            ((girasol_rosa < florzinha_girasol) and (girasol_rosa < rosa_florzinha)) * 'Girasol Rosa' + \
            ((florzinha_girasol < girasol_rosa) and (florzinha_girasol < rosa_florzinha)) * 'Florzinha Girasol'

print(resultado)
