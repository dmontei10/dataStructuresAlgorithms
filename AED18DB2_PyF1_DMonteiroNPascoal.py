# -*- coding: utf-8 -*-

# Trabalho feito pelos Estudantes de Engenharia informática - Turma B - AED
# Integrantes do grupo :\
                        # Neide Eduardo Pascoal - 30003957 - turma B
                        # David Monteiro - 30003043 - turma B


#-------------------------- GESTÃO DE FROTAS - 'ESTAFETAS' ---------------------------- #
class Viatura:
    def __init__(self, matrícula, capacidade):
        self.matrícula = matrícula
        self.capacidade = capacidade


class Camião(Viatura):
    def __init__(self, matrícula):
        super().__init__(matrícula, 1200000)
    def __str__ (self):
        a = '\n=> Descrição do Camião: \nMatrícula: ' + str(self.matrícula) + \
        '\nCapacidade: ' + str(self.capacidade)
        return a

        
        
class Automóvel(Viatura):
    def __init__(self, matrícula):
        super().__init__(matrícula, 80000)

    def __str__(self):
        b = '\n=> Descrição do automóvel: \nMatrícula: ' + str(self.matrícula)+ \
            '\nCapacidade: ' + str(self.capacidade)
        return b


class Mota(Viatura):
    def __init__(self, matrícula):
        super().__init__(matrícula, 0) # Função 'super()' utlizamos esta função \
        # para criar uma especie de Herança, nesse caso a classe Mota Herda de class Viatura!
    def __str__(self): # Função ' __str__ ' função utilizada para afixar valores na tela!
        c = '\n=> Descrição da Mota: \nMatrícula: ' + str(self.matrícula) + \
            '\nCapacidade: ' + str(self.capacidade)
        return c

class Condutor:
    def __init__(self, número, nome, telefone, email):
        self.número = número
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def __str__(self):
        d = '\n => Descrição do Condutor: \nNúmero: ' + str(self.número) + \
            '\nNome: ' + str(self.nome) + \
            '\nTelefone: ' + str(self.telefone) + \
            '\nEmail: ' + str(self.email)
        return d



class Cliente:
    def __init__ (self, número, nome, morada, telefone, email):
        self.número = número
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.email = email


    def __str__(self):
        e = '\n => Descrição dos Clientes: \nNúmero: ' + str(self.número) + \
            '\nNome: ' + str(self.nome) + \
            '\nMorada: ' + str(self.morada) + \
            '\nTelefone: ' + str(self.telefone) + \
            '\nEmail: ' + str(self.email)
        return e


class Entrega: #Criação da Classe Entrega e atribuição dos seus respetivos atributos:
    def __init__(self, identificador, ponto_recolha, ponto_entrega, \
               mercadoria_descrição, mercadoria_volume):
        self.identificador = identificador
        self.ponto_recolha = ponto_recolha
        self.ponto_entrega = ponto_entrega
        self.mercadoria_descrição = mercadoria_descrição
        self.mercadoria_volume = mercadoria_volume

    def __str__(self):
        f = '\n => Descrição da Entrega: \nIdentificador:' + str(self.identificador) + \
            '\nPonto de Recolha: ' + str(self.ponto_recolha) + \
            '\nPonto de Entrega: ' + str(self.ponto_entrega) + \
            '\nMercadoria descrição: ' + str(self.mercadoria_descrição) + \
            '\nMercadoria Volume: ' + str(self.mercadoria_volume)
        return f


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    

class cliTree:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BSTcliTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = cliTree(key)
        self.size = self.size + 1

    def _put(self,key,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,currentNode.leftChild)
            else:
                   currentNode.leftChild = cliTree(key,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,currentNode.rightChild)
            else:
                   currentNode.rightChild = cliTree(key,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.key
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self.root
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): 
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): 
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: 
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.key,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)


print("\n ===> GESTÃO DE FROTAS - ESTAFETA <===")
 

#----------------- Função 'Main' (Função principal do programa) -------------------------#
class Programa:
    
    if __name__ =='__main__' :
        
       
      
        treenames = BSTcliTree()
        treenames.put("Sílvia Cruz")
        treenames.put("David Monteiro")
        treenames.put("Roberta de Carvalho")
        listaCliente=[]
        cliente1= Cliente(6357,'Roberta de Carvalho','Praceta José',967835647,'dm99@xpto.com')
        cliente2=Cliente(7038,'Sílvia Cruz','Rua Rui Grácio',93345048,'teiro@xpto.com')
        cliente3=Cliente( 9728,'David Monteiro','Avenida da Liberdade', 962216021,'yyc43@xpto.com')
        listaCliente.append(cliente1)
        listaCliente.append(cliente2)
        listaCliente.append(cliente3)
        
        
    
        listaEntrega=[]
        entrega1= Entrega('98J76F', 'Rossio','Loures','Mercadoria Frágil',7000)
        entrega2= Entrega('TG4537', 'Amadora','Campo Grande','Carga Pesada',1239000)
        entrega3= Entrega('2CFG45', 'Odivelas','Saldanha Metro','Mercadoria Tóxica',100090)
    
        listaEntrega.append(entrega1)
        listaEntrega.append(entrega2)
        listaEntrega.append(entrega3)
    
        
        camião1= Camião('34-AO-45')
        camião2= Camião('AD-7Y-02')
        camião3= Camião('DV-80-HK')
        listaCamião=[]   
        listaCamião.append(camião1)
        listaCamião.append(camião2)
        listaCamião.append(camião3)
    
        
        
        automovel1= Automóvel('55-8U-MN')
        automovel2= Automóvel('7F-OL-43')
        automovel3= Automóvel('PL-89-SS')
        listaAutomovel=[]
        listaAutomovel.append(automovel1)
        listaAutomovel.append(automovel2)
        listaAutomovel.append(automovel3)
    
    
        mota1= Mota('DM-11-99')
        mota2= Mota('I6-73-PM')
        mota3= Mota('CA-23-OR')
        listaMota=[]
        listaMota.append(mota1)
        listaMota.append(mota2)
        listaMota.append(mota3)
       
        condutor1= Condutor(645738, 'António Franco',935253668,'jpereira@xpto.com')
        condutor2= Condutor(849379, 'Maria Teresa',967839749,'mariatete@xpto.com')
        condutor3= Condutor(222453, 'Andreia Carvalho',934567890,'carvalhoandreia@xpto.com')
        listaCondutor=[]
        listaCondutor.append(condutor1)
        listaCondutor.append(condutor2)
        listaCondutor.append(condutor3)
    
        
            
        FCamiao =Queue()
        for a in listaCamião:
            FCamiao.enqueue(a)
           
        FAutomovel =Queue()
        for b in listaAutomovel:
            FAutomovel.enqueue(b)
        
        FMota =Queue()
        for c in listaMota:
            FMota.enqueue(c)
    
        FCondCamiao=Queue()
        for d in listaCondutor:
            FCondCamiao.enqueue(d)
        
        FCondAutomovel=Queue()
        for e in listaCondutor:
            FCondAutomovel.enqueue(e)
    
        FCondMota=Queue()
        for f in listaCondutor:
            FCondMota.enqueue(f)
    
        
        FEntregaCamião =Queue()    
        FEntregaAutomovel=Queue()
        FEntregaMota=Queue()
      
        for x in listaEntrega:
            if x.mercadoria_volume < 80000:
                FEntregaMota.enqueue(x)
            elif x.mercadoria_volume < 1200000:
                FEntregaAutomovel.enqueue(x)
            else:
                FEntregaCamião.enqueue(x)
        
        
    
    while True: 
        #Menu de Opções Sobre o trabalho / aqui metemos as opções de funcionalidade do app
        # terá Condições dentro de Loops e muito mais...
        # (baixa mais ou pouco)
    
        print("\n========================================================")
        print("\n=> Escolha uma das opções: \n")
        print("1-> Modificar")
        print("2-> Guardar em ficheiro binário os dados existentes")
        print("3-> Adicionar dados (criar) e guardar novos dados no ficheiro binário ")
        print("4-> Afixar na Tela as listas criadas")
        print('5-> Criar um Ficheiro Texto "Entregas" e afixar na tela')
        print("6-> Pesquisar o nome de um cliente:")
        print("7-> Afixar os nomes contidos na árvore, por ordem alfabética")
        print("0-> Sair")
        opcc = int(input())
        if opcc == 1:
            print("\n=> Escolha uma opção: \n")
            print("1- | CONDUTOR  |")
            print("2- | CLIENTE   |")
            print("3- | CAMIÃO    |")
            print("4- | AUTOMÓVEL |")
            print("5- | MOTA      |")
            print("6- | ENTREGA   |")
            opcao = int(input())
            if opcao == 1:
                
                
                for x in listaCondutor:
                    print(x)
                print("\n")    
                print("1- Número")
                print("2- Nome")
                print("3- Telefone")
                print("4- Email")
                opcb = int(input())
                if opcb ==1:
                    escolhaa=input("Digite o Número que deseja alterar: ")
                    for i in listaCondutor:
                        if escolhaa in i.número:
                            novMa2r2 = input("Novo Número: ")
                            i.número=novMa2r2
                        print(i)
                elif opcb==2:
                    escolha22=input("Digite o Nome que deseja alterar: ")
                    for i in listaCondutor:
                        if escolha22 in i.nome:
                            novMa21 = input("Novo Nome: ")
                            i.nome=novMa21
                        print(i)
                elif opcb==3:
                    escolha09=input("Digite o Telefone que deseja alterar: ")
                    for i in listaCondutor:
                        if escolha09 in i.telefone:
                            novMa2m2 = input("Novo Telefone: ")
                            i.telefone=novMa2m2
                        print(i)
                elif opcb==4:
                    escolha14=input("Digite o Email que deseja alterar: ")
                    for i in listaCondutor:
                        if escolha14 in i.email:
                            novMa242 = input("Novo Email: ")
                            i.email=novMa242
                        print(i)
                
            elif opcao == 2:
                
                for x in listaCliente:
                    print(x)
                print("\n")    
                print("1- Número")
                print("2- Nome")
                print("3- Morada")
                print("4- Telefone")
                print("5- Email")
                opca = int(input())
                if opca == 1:
                    escolha5a=input("Digite o Número que deseja alterar: ")
                    for i in listaCliente:
                        if escolha5a in i.número:
                            naovMa4 = input("Novo Número: ")
                            i.número = naovMa4
                            print(i)
                            
                elif opca ==2:
                    escolha3e=input("Digite o Nome que deseja alterar: ")
                    for i in listaCliente:
                        if escolha3e in i.nome:
                            novMma3 = input("Novo Nome: ")
                            i.nome = novMma3
                            print(i)
                            
                elif opca==3:
                    escolha2d=input("Digite a Morada que deseja alterar: ")
                    for i in listaCliente:
                        if escolha2d in i.morada:
                            novvMa1 = input("Nova Morada: ")
                            i.moradaa = novvMa1
                            print(i)
                    
                elif opca==4:
                    escolhaa9=input("Digite o Telefone que deseja alterar: ")
                    for i in listaCliente:
                        if escolhaa9 in i.telefone:
                            nnovMa = input("Novo Telefone: ")
                            i.telefone = nnovMa
                            print(i)
                elif opca==5:
                    
                    escolha9e=input("Digite o Email que deseja alterar: ")
                    for i in listaCliente:
                        if escolha9e in i.email:
                            novMa = input("Novo Email: ")
                            i.email = novMa
                            print(i) 
                            
            elif opcao == 3:
                
                for x in listaCamião:
                    print(x)
                    
                escolha1=input("Digite a matricula que deseja alterar: ")
                for i in listaCamião:
                    if escolha1 in i.matrícula:
                        novMa = input("Nova Matrícula: ")
                        i.matrícula=novMa
                        print(i)
                        
            elif opcao == 4:
                
                for x in listaAutomovel:
                    print(x)
                    
                escolha4=input("Digite a matricula que deseja alterar: ")
                for i in listaAutomovel:
                    if escolha4 in i.matrícula:
                        novMa2 = input("Nova Matrícula: ")
                        i.matrícula=novMa2
                        print(i)
                        
            elif opcao == 5:
                for x in listaMota:
                    print(x)
                escolha3=input("Digite a matricula que deseja alterar: ")
                for i in listaMota:
                    if escolha3 in i.matrícula:
                        novMa2 = input("Nova Matrícula: ")
                        i.matrícula=novMa2
                        print(i)
                        
            elif opcao == 6:
                
                for x in listaEntrega:
                    print(x)
                print("\n")    
                print("1- Identificador")
                print("2- Ponto de Recolha")
                print("3- Ponto de Entrega")
                print("4- Volume da Mercadoria")
                print("5- Descrição da Mercadoria")
                opca = int(input())
                if opca == 1:
                    escolha5=input("Digite o Identificador que deseja alterar: ")
                    for i in listaEntrega:
                        if escolha5 in i.identificador:
                            novMa4 = input("Novo Identificador: ")
                            i.identificador = novMa4
                            print(i)
                elif opca ==2:
                    escolha3=input("Digite o Ponto de Recolha que deseja alterar: ")
                    for i in listaEntrega:
                        if escolha3 in i.ponto_recolha:
                            novMa3 = input("Novo Ponto de Recolha: ")
                            i.ponto_recolha = novMa3
                            print(i)
                            
                elif opca==3:
                    escolha2=input("Digite o Ponto de Entrega que deseja alterar: ")
                    for i in listaEntrega:
                        if escolha2 in i.ponto_entrega:
                            novMa1 = input("Novo Ponto de Entrega: ")
                            i.ponto_entrega = novMa1
                            print(i)
                    
                elif opca==4:
                    escolha9=input("Digite o Volume da Mercadoria que deseja alterar: ")
                    for i in listaEntrega:
                        if escolha9 in i.mercadoria_volume:
                            novMa = input("Novo Volume da Mercadoria: ")
                            i.mercadoria_volume = novMa
                            print(i)
                elif opca==5:
                    
                    escolha9=input("Digite o Volume da Mercadoria que deseja alterar: ")
                    for i in listaEntrega:
                        if escolha9 in i.mercadoria_descrição:
                            novMa = input("Novo Descrição da Mercadoria: ")
                            i.mercadoria_descrição = novMa
                            print(i) 
            else:
                print("Erro! Introduza uma das opções acima")
    
    
        elif opcc == 2:
            
            EstafetasListas= open("EstafetaListas.pkl","w+b") #Abre um arquivo binário especificado para escrita e leitura. Caso o arquivo não exista, este será criado, porém , caso exista, seus dados serão sobrescritos.   
            for i in listaCamião:
                EstafetasListas.write(bytes(str(i),"utf-8"))
            for j in listaAutomovel:
                EstafetasListas.write(bytes(str(j),"utf-8"))
            for k in listaMota:
                EstafetasListas.write(bytes(str(k),"utf-8")) 
            for n in listaCondutor:
                EstafetasListas.write(bytes(str(n),"utf-8"))
            for a in listaCliente:
                EstafetasListas.write(bytes(str(a),"utf-8")) 
            for x in listaEntrega:
                EstafetasListas.write(bytes(str(x),"utf-8")) 
            EstafetasListas.close() #fechar o arquivo    
            print('Ficheiro binário gravado com sucesso!')
    
        elif opcc == 3:
                    print("\nEm Quais das Classes prentendes adicionar Dados?:\n")
                    print("0-> Página inicial do programa <-")
                    print("1-> Camião")
                    print("2-> Automóvel")
                    print("3-> Mota")
                    print("4-> Condutor")
                    print("5-> Cliente")
                    print("6-> Entrega")
                    opc=int(input())
                    
                    if opc==1:
                          EstafetasListas= open("EstafetaListas.pkl","w+b")
                          mttr = str(input("Matricula: "))
                          caam=Camião(mttr)
                          listaCamião.append(caam)
                          for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                          for j in listaAutomovel:
                              EstafetasListas.write(bytes(str(j),"utf-8"))
                          for k in listaMota:
                              EstafetasListas.write(bytes(str(k),"utf-8")) 
                          for n in listaCondutor:
                              EstafetasListas.write(bytes(str(n),"utf-8"))
                          for a in listaCliente:
                              EstafetasListas.write(bytes(str(a),"utf-8")) 
                          for x in listaEntrega:
                              EstafetasListas.write(bytes(str(x),"utf-8")) 
                          EstafetasListas.close()
                          
    
                    
                    elif opc==2:
                        EstafetasListas= open("EstafetaListas.pkl","w+b")
                        matr = str(input("Matricula: "))
                        aut=Automóvel(matr)
                        listaAutomovel.append(aut)
                        for j in listaAutomovel:
                            EstafetasListas.write(bytes(str(j),"utf-8")) 
                        for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                        for k in listaMota:
                              EstafetasListas.write(bytes(str(k),"utf-8")) 
                        for n in listaCondutor:
                              EstafetasListas.write(bytes(str(n),"utf-8"))
                        for a in listaCliente:
                              EstafetasListas.write(bytes(str(a),"utf-8")) 
                        for x in listaEntrega:
                              EstafetasListas.write(bytes(str(x),"utf-8")) 
                        
                        EstafetasListas.close()
                          
                        
                    elif opc==3:
                         EstafetasListas= open("EstafetaListas.pkl","w+b")
                         mtr = str(input("Matricula: "))
                         mot= Mota(mtr)
                         listaMota.append(mot)
                         for k in listaMota:
                             EstafetasListas.write(bytes(str(k),"utf-8"))
                         for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                         for j in listaAutomovel:
                              EstafetasListas.write(bytes(str(j),"utf-8"))
                         for n in listaCondutor:
                              EstafetasListas.write(bytes(str(n),"utf-8"))
                         for a in listaCliente:
                              EstafetasListas.write(bytes(str(a),"utf-8")) 
                         for x in listaEntrega:
                              EstafetasListas.write(bytes(str(x),"utf-8")) 
    
                         EstafetasListas.close()
                          
    
            
    
                    elif opc==4:
                         EstafetasListas= open("EstafetaListas.pkl","w+b")
                         num = int(input("Número: "))
                         Name = input("Nome: ")
                         Tel = int(input("Telefone: "))
                         email = input("Email: ")
                         cond = Condutor(num,Name,Tel,email)
                         listaCondutor.append(cond)
                         for n in listaCondutor:
                             EstafetasListas.write(bytes(str(n),"utf-8")) 
                         for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                         for j in listaAutomovel:
                              EstafetasListas.write(bytes(str(j),"utf-8"))
                         for k in listaMota:
                              EstafetasListas.write(bytes(str(k),"utf-8"))
                         for a in listaCliente:
                              EstafetasListas.write(bytes(str(a),"utf-8")) 
                         for x in listaEntrega:
                              EstafetasListas.write(bytes(str(x),"utf-8")) 
                         EstafetasListas.close()                         
                  
    
                    
                    elif opc==5:
                        EstafetasListas= open("EstafetaListas.pkl","w+b")
                        numm = int(input("Número: "))
                        name = input("Nome: ")
                        morada = input("Morada: ")
                        tel = int(input("Telefone: "))
                        email = input("Email: ")
                        clliente = Cliente(numm,name,morada,tel,email)
                        listaCliente.append(clliente)
                        
                        for a in listaCliente:
                            EstafetasListas.write(bytes(str(a),"utf-8")) 
                        for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                        for j in listaAutomovel:
                              EstafetasListas.write(bytes(str(j),"utf-8"))
                        for k in listaMota:
                              EstafetasListas.write(bytes(str(k),"utf-8")) 
                        for n in listaCondutor:
                              EstafetasListas.write(bytes(str(n),"utf-8"))
                        for x in listaEntrega:
                              EstafetasListas.write(bytes(str(x),"utf-8")) 
    
    
                        EstafetasListas.close()
                        
                        
    
                                      
                    elif opc==6:
                         EstafetasListas= open("EstafetaListas.pkl","w+b")
                         idd = input("Identificador: ")
                         pr = input("Ponto de Recolha: ")
                         pe = input("Ponto de Entrega: ")
                         md = input("Mercadoria Descrição: ")
                         mv = input("Mercadoria Volume: ")
                         entregaa = Entrega(idd,pr,pe,md,mv)
                         
                         
                         listaEntrega.append(entregaa)
                         for x in listaEntrega:
                             EstafetasListas.write(bytes(str(x),"utf-8")) 
                         for i in listaCamião:
                              EstafetasListas.write(bytes(str(i),"utf-8"))
                         for j in listaAutomovel:
                              EstafetasListas.write(bytes(str(j),"utf-8"))
                         for k in listaMota:
                              EstafetasListas.write(bytes(str(k),"utf-8")) 
                         for n in listaCondutor:
                              EstafetasListas.write(bytes(str(n),"utf-8"))
                         for a in listaCliente:
                              EstafetasListas.write(bytes(str(a),"utf-8")) 
    
                    
                         EstafetasListas.close() #fechar o arquivo
                         
                    else:
                        print("Erro! Introduza uma das opções acima")
                      
        elif opcc == 4:
            for cam in listaCamião:
                print(cam)
            for entr in listaEntrega:
                print(entr)
            for mot in listaMota:
                print(mot)
            for client in listaCliente:
                print(client)
            for auto in listaAutomovel:
                print(auto)
            for cond in listaCondutor:
                print(cond)
    
    
        elif opcc == 5:
            
            ficheiroEntregas=open('FEntregas.txt','w')# Ficheiro aberto para escrita
            ficheiroEntregas.write('==> As Entregas para camião:')#escreve no ficheiro
            for i in FEntregaCamião.items :
                ficheiroEntregas.write(str(i))
            ficheiroEntregas.write('==> As Entregas para Automóvel:\n')
            for y in  FEntregaAutomovel.items:
                ficheiroEntregas.write(str(y))
            ficheiroEntregas.write('==> As Entregas para Mota:\n')
            for z in FEntregaMota.items:           
                ficheiroEntregas.write(str(z))
            ficheiroEntregas.close() #fecha o ficheiro
            print('Ficheiro Entregas gravado com sucesso!\n')
            
             #Procedimento para ler e Afixar
            ficheiroEntregas=open('Entregas.txt','r')
            for i in ficheiroEntregas:
                i=i.rstrip()
                print(i)
            ficheiroEntregas.close()
            
    
    
            
        elif opcc == 6:
                nome = input('Digite o nome de um cliente:\n')
                achou= treenames.get(nome)
                if achou == nome:
                    print('O cliente {}, está registrado no sistema.'.format(nome))
                else:
                    print('Este nome não pertence a nenhum dos nossos clientes.')
       
        elif opcc == 7:
            print("Ordenação efetuada com sucesso!\n")
            while treenames.length() > 0:
                no = treenames.findMin()
                print( no.key )
                treenames.delete(treenames.findMin().key)
            
        #elif opcc==8:
            
          #  if FCamiao.size() > 0:
           #     FCamiao.dequeue()
                
            #else:
             #   print("Viatura Indisponível")
                
        elif opcc == 0:
             print('A encerrar o programa...')
             break
        else:
            print('Erro! Introduza uma das opções acima.')
            
            
           # http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
           
           
           
           
