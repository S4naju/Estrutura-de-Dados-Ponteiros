class No:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None 

class ListaEncadeada:
    def __init__(self):
        self.inicio = None 
    
    def is_empty(self):
        return self.inicio is None 

    def inserirInicio (self, valor):
        novoNo = No(valor)
        novoNo.proximo = self.inicio #aponta pro antigo primeiro nó
        self.inicio = novoNo #self.incio se torna o novoNo

    def inserirFinal(self, valor):
        novoNo = No(valor)
        if self.is_empty(): #se estiver vazia...
            self.inicio = novoNo #...self.incio se torna o novoNo
            return
        
        #se a fila n estiver vazia...
        noAtual = self.inicio #noAtual aponta pro primeiro nó da lista
        while noAtual.proximo is not None: #quando tiver um próximo nó...
            noAtual = noAtual.proximo #...nó atual aponta por próximo nó

        #no entanto, se n existir um próximo nó...
        noAtual.proximo = novoNo #...o noAtual é o novoNo e é o último nó da lista tbm
    
    def removerValor (self, valor):
        if self.is_empty(): #se tiver vazia nada é feito
            return
        
        if self.inicio.valor == valor: #se tiver valor no primeiro nó...
            self.inicio = self.inicio.proximo #... self.inicio se torna o próximo nó
            return

        #se o primieiro nó n tiver valor...
        anterior = self.inicio #aponta pro 1 nó da lista
        atual = self.inicio.proximo #aponta pro 2 nó da lista
        while atual is not None and atual.valor != valor: #se ainda tiver nós na lista e o valor do nó atual for diferente do valor...
            anterior = atual  #nó atual passa a ser o nóa anterior
            atual = atual.proximo #e o próximo nó passa a ser o nó atual 

        if atual is not None: #se encontramos o valor q queremos remover...
            anterior.proximo = atual.proximo #nó anterior passa apontar por próximo nó, "pulando" o nó atual q vai ser removido da lista
        else:
            print(f"valor {valor} não encontrado na lista!\n")

    def __str__(self): #imprimir a lista
        print("-"*50)
        print(f"{'LISTA ENCADEADA':^50}")
        print("-"*50)
        if self.is_empty():
            return "|   |".center(50) + "\n" + "-"*50

        elementos = [] #cria uma lista de string q vai armazenar os valores dos nó
        noAtual = self.inicio #noAtual aponta pro 1 nó da lista - começa pelo início
        while noAtual is not None: #se o noAtual tiver valor...
            elementos.append(str(noAtual.valor)) #transforma o noAtual em string e adiciona a lista elementos
            noAtual = noAtual.proximo #noAtual aponta pro próximo nó, até chegar no final (none)
        conteudo = f" INÍCIO -> | " + " -> ".join(elementos) + " | <- FIM" #junta os valores da lista
        return conteudo.center(45) + "\n" + "-"*50 + "\n"


lista = ListaEncadeada() #criando a lista
lista.inserirInicio(15) #adicionando valores na lista
lista.inserirInicio(23)
lista.inserirFinal(31)
lista.inserirFinal(44)
print(lista)
print("a lista está vazia? ", lista.is_empty(), "\n")

lista.removerValor(15)
lista.removerValor(23)
lista.removerValor(33)
print(lista)
print("a lista está vazia? ", lista.is_empty(), "\n")

lista.removerValor(31)
lista.removerValor(44)
print(lista)
print("a lista está vazia? ", lista.is_empty(), "\n")