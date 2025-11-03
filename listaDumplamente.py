class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None 
        self.anterior = None #ponteiro p nó anterior

class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None #ponteiro p o último nó

    def is_empty(self):
        return self.inicio is None 

    def inserirFinal (self, valor):
        novoNo = NoDuplo(valor)
        if self.inicio is None: #se a lista tiver vazia o inicio e o fim apontam p novoNo
            self.inicio = novoNo
            self.fim = novoNo
        else:
            novoNo.anterior = self.fim #novoNo aponta para o antio fim
            self.fim.proximo = novoNo #antigo fim aponta p o novoNo
            self.fim = novoNo #fim da lista é atualizado - novoNo
    
    def removerValor(self, valor):
        noAtual = self.inicio #noAtual aponta pro primeiro nó da lista 
        while noAtual is not None and noAtual.valor != valor: #se ainda tiver nós na lista e o valor do nó atual for diferente do valor...
            noAtual = noAtual.proximo #noAtual aponta pro próximo nó 
        
        if noAtual is None: 
            print(f"valor {valor} não encontrado na lista!\n")
            return

        if noAtual.anterior is not None: #se o nó n for o primeiro 
            noAtual.anterior.proximo = noAtual.proximo #o anterior vai "pular" o removido e vai apontar pro próximo nó
        else:
            self.inicio = noAtual.proximo #se for o primeiro nó, remove

        if noAtual.proximo is not None: #caso o nó n for o último...
            noAtual.proximo.anterior = noAtual.anterior #o próximo vai "pular" o removido e passa apontar p o nó anterior 
        else:
            self.fim = noAtual.anterior #removendo o fim da lista
        
    def __str__(self): #imprimir a lista do início ao fim
        print("-"*60)
        print(f"{'LISTA DUPLAMENTE ENCADEADA':^60}")
        print("-"*60)
        if self.is_empty():
            return "|   |".center(60) + "\n" + "-"*60 + "\n"

        elementos = [] 
        noAtual = self.inicio #noAtual aponta pro 1 nó da lista - começa pelo início
        while noAtual is not None: #se o noAtual tiver valor...
            elementos.append(str(noAtual.valor)) #transforma o noAtual em string e adiciona a lista elementos
            noAtual = noAtual.proximo #noAtual aponta pro próximo nó, até chegar no final (none) - move p frente
        conteudo = f" INÍCIO -> | " + " -> ".join(elementos) + " | <- FIM" #junta os valores da lista
        return conteudo.center(55) + "\n" + "-"*60 + "\n" 

    def exibirContrario (self):
        print("="*60)
        print(f"{'LISTA AO CONTRÁRIO':^60}")
        print("="*60)
        if self.is_empty():
            return "|   |".center(60) + "\n" + "="*60 + "\n" 
        
        elementos = [] 
        noAtual = self.fim #noAtual aponta pro último nó da lista - começa pelo fim
        while noAtual is not None: 
            elementos.append(str(noAtual.valor)) 
            noAtual = noAtual.anterior #move p tras 
        conteudo = f" FIM -> | " + " -> ".join(elementos) + " | <- INÍCIO" 
        return conteudo.center(55) + "\n" + "="*60 + "\n"

lista = ListaDuplamente() #criando a lista
lista.inserirFinal(15) #adicionando valores na lista
lista.inserirFinal(23)
lista.inserirFinal(31)
lista.inserirFinal(44)
print(lista)
print(lista.exibirContrario())
print("a lista está vazia? ", lista.is_empty(), "\n")

lista.removerValor(15)
lista.removerValor(23)
lista.removerValor(33)
print(lista)
print(lista.exibirContrario())
print("a lista está vazia? ", lista.is_empty(), "\n")

lista.removerValor(31)
lista.removerValor(44)
print(lista)
print(lista.exibirContrario())
print("a lista está vazia? ", lista.is_empty(), "\n")
