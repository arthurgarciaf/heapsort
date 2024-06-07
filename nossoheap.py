def maxheap(vetor,tamanho,i):
    maior = i # Inicializa a variavel MAIOR com I(I sendo a posição atual do vetor)
    esquerda = 2 * i + 1 # define a variavel da esquerda como 2* A posição atual do vetor mais um
    direita = 2 * i + 2 # mesma coisa, porém com a variavel da direita, e ao invés de ser mais um, adiciona mais 2

    # Verificar se o sub-categoria da posição do vetor existe, e é maior que que o vetor raiz
    if esquerda < tamanho and vetor[i] < vetor[esquerda]:
        maior = esquerda

    # Mesma verificação, porém com o valor da direita
    if direita < tamanho and vetor[maior] < vetor[direita]:
        maior = direita

    # Trocar a raiz, se necessario
    if maior != i:
        vetor[i],vetor[maior] = vetor[maior],vetor[i]

        # Nos "heapificamos" a raiz
        maxheap(vetor,tamanho,maior)

    # Parte principal onde iremos organizar o vetor de um tamanho definido

def organizar(vetor):
        tamanho = len(vetor)

        # Transforma o vetor em um padrão de maxheap
        for i in range(tamanho,-1,-1):
            maxheap(vetor,tamanho,i)
        
        # Extrair os elementos um por um
        for i in range(tamanho-1,0 ,-1):
            vetor[i],vetor[0] = vetor[0],vetor[i] # troca os valores de lugar
            maxheap(vetor,i-1,0)


print("Olá, quantos valores você precisará organizar?")
valores = int(input())
lista = []
while valores <= 1:
    print("Você não pode organizar menos que dois valores, tente novamente.")
    valores = int(input())
print("Agora digite os ",valores," valores que deseja organizar")
for i in range(valores):
    print("Digite o ",i+1,"° item da lista")
    lista.append(float(input()))
print("Essa é sua lista antes do heapsort",lista)

organizar(lista)
print("Essa é sua lista depois do heapsort",lista)

