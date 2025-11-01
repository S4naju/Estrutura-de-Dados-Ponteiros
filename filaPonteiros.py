class No:
    def __init__(self, valor):
        self.valor = valor #dado q o nó armazena
        self.proximo = None #ponteiro p o próximo nó

class Fila: #FIFO - frist in, frist out
    def __init__(self):
        self.inicio = None #nó do início da fila
        self.fim = None #nó do fim da fila
        self.tamanho = 0
    
    def is_empty(self):
        return self.inicio is None

    def enqueue (self, valor): #adiciona um novo valor no FIM da fila
        novoNo = No(valor)

        if self.is_empty(): #se a fila estiver vazia o novoNo é o inicio e fim
            self.inicio = novoNo 
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo #o ponteiro do ultimo nó aponta pro novoNo
            self.fim = novoNo #o novoNo se torna o novo fim
        
        self.tamanho += 1 #tamanho da fila aumenta 
        print(f"Enqueue: {valor} entrou na fila!")

    def dequeue(self): #remove o valor do INICIO da fila
        if self.is_empty():
            print("Erro: a fila está vazia! não é possivel remover!\n")
            return None #usamos isso p n usar else

        valorRemovido = self.inicio.valor
        self.inicio = self.inicio.proximo #move o ponteiro do inicio p o próximo nó da fila

        self.tamanho -= 1 #a fila diminui o tamanho
        print(f"Dequeue: {valorRemovido} saiu da fila!")
        return valorRemovido
    
    def peek(self):
        if self.is_empty():
            return "fila vazia!"
        return self.inicio.valor #se n tiver vazia retorna o valor do topo, mas sem remove-lo
    
    def exibir(self): #mostra a fila
        print("\n" + "-" *40)
        print(f"{'FILA':^40}")
        print("-" *40)
        if self.inicio is None:
            return f"{'|   |':^40}"
        
        noAtual = self.inicio #chamando self.inicio de noAtuall, p assim poder percorrer a filha sem alterar o self.inicio
        while noAtual is not None: 
            if noAtual == self.inicio:
                print(f"{'-> | ' + str(noAtual.valor) + ' | <- INÍCIO':^45}") #str() - converte o valor para string
            elif noAtual == self.fim:
                print(f"{'-> | ' + str(noAtual.valor) + ' | <- FIM':^43}")
            else:
                print(f"{'| ' + str(noAtual.valor) + ' |':^38}")
            noAtual = noAtual.proximo
        print("-"*40)

lista = Fila() #criando a fila - instância
lista.enqueue(15) #chamando o método
lista.enqueue(23) 
lista.enqueue(31)
lista.enqueue(44)
lista.exibir()
print("\ntopo atual da fila: ", lista.peek()) #mostra o topo atual
print("a fila está vazia? ", lista.is_empty(), "\n")

lista.dequeue()
lista.dequeue()
lista.exibir()
print("\ntopo atual da fila: ", lista.peek(),) 
print("a fila está vazia? ", lista.is_empty(), "\n")

lista.dequeue()
lista.dequeue()
lista.exibir()
print("\ntopo atual da fila: ", lista.peek(),) 
print("a fila está vazia? ", lista.is_empty(), "\n")