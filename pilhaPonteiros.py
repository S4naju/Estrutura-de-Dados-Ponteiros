class No:
    def __init__(self, valor):
        self.valor = valor #dado q o nó armazena
        self.proximo = None #ponteiro p o próximo nó

class Pilha: #LIFO - last in, frist out
    def __init__(self):
        self.topo = None #topo começa valendo nada
        self.tamanho = 0

    def is_empty(self):
        return self.topo is None #se tiver vazia retorna True
    
    def push(self, valor):
        novoNo = No(valor) #criar um novo nó que vai passar o valor
        novoNo.proximo = self.topo #novoNo vai apontar pro antigo topo (q é o topo atual)
        self.topo = novoNo #o novoNo vai se tornar o novo topo 
        self.tamanho += 1 #aumenta o tam da pilha
        print(f"Push: {valor} foi adicionado à pilha!") #concatena o valor em string
    
    def pop(self):
        if self.is_empty(): 
            print("Erro: a pilha está vazia! não é possivel remover!\n")
            return None #usamos isso p n usar else
        
        #se n tiver vazia a pilha:
        valorRemovido = self.topo.valor  #valor removido é o do topo
        self.topo = self.topo.proximo #o proximo topo será o próximo valor
        self.tamanho -= 1 #diminui o tam da pilha
        print(f"Pop: {valorRemovido} foi removido da pilha!")
        return valorRemovido #retorna o valor removido
    
    def peek(self): 
        if self.is_empty():
            return"pilha vazia!"
        return self.topo.valor #se n tiver vazia retorna o valor do topo, mas sem remove-lo
    
    def exibir(self): #mostra a pilha
        print("\n" + "-" *40)
        print(f"{'PILHA':^40}") #esse ^ significa centralizar o texto
        print("-" *40)
        if self.topo is None:
            return f"{'|   |':^40}"
        
        noAtual = self.topo # chamando self.topo de atual, para assim poder percorrer a pilha sem alterar o self.topo
        while noAtual is not None: 
            if noAtual == self.topo:
                print(f"{'-> | ' + str(noAtual.valor) + ' | <- INÍCIO':^45}") #str() - converte o valor para string
            else:
                print(f"{'| ' + str(noAtual.valor) + ' |':^38}")
            noAtual = noAtual.proximo
        print("-"*40)

lista = Pilha() #criando a pilha
lista.push(15) #adicionando valores na pilha
lista.push(23)
lista.push(31)
lista.push(44)
lista.exibir()
print("\ntopo atual da pilha: ", lista.peek()) #mostra o topo atual
print("a pilha está vazia? ", lista.is_empty(), "\n")

lista.pop()
lista.pop()
lista.exibir()
print("\ntopo atual da pilha: ", lista.peek(),) 
print("a pilha está vazia? ", lista.is_empty(), "\n")

lista.pop()
lista.pop()
lista.exibir()
print("\ntopo atual da pilha: ", lista.peek(),) 
print("a pilha está vazia? ", lista.is_empty(), "\n")