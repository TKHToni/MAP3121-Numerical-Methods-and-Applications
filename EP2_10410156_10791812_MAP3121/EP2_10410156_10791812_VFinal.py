# -*- coding: utf-8 -*-
import numpy as np
import os
import sys

def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)

def norm(vector):
    return np.sqrt(sum(i**2 for i in vector))

def e(length):
    return np.insert(np.zeros(length-1),1,1)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def interpretFile(fileName):
    file=open(os.path.join(os.path.dirname(__file__), fileName),"r")
    
    list_of_File = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        if line_list!=[]:
            list_of_File.append(line_list)
    
    file.close()
    while True:
        try:
            matrix=np.zeros((int(list_of_File[0][0]),int(list_of_File[0][0])))
            for i in range(len(list_of_File)):
                for j in range(len(list_of_File[i])):
                    list_of_File[i][j]=float(list_of_File[i][j])
            
            for i in range(1,len(list_of_File)):
                matrix[i-1,:]=list_of_File[i]
            break
        except ValueError:
            print("\nArquivo não está formatado corretamente para este item. Rode o código novamente e escolha outro arquivo ou corrija a formatação.")
            sys.exit()
            
          
    return matrix

def HH(A):
    
    I=np.identity(len(A))
    
    for i in range(1, len(A)):
        
        #Definindo vetores HouseHolder
        ãi=np.append(np.array([0]),A[i:,i-1]) 
        sigma=np.sign(A[i,i-1])
        
        wi=ãi+sigma*norm(ãi)*e(len(ãi))
        wiBar=np.delete(wi,0,0)
    
        #Multiplicação a Esquerda
        for j in range(i-1,len(A[0])):
            A[i:,j]=A[i:,j]-2*dot(wiBar,A[i:,j])/dot(wiBar,wiBar)*wiBar
        A[i-1,i:]=A[i:,i-1] #Igualando a parte simétrica acima da diagonal
        
        #Multiplicação a Direita
        for m in range(i,len(A)):
            A[m,i:]=A[m,i:]-2*dot(wiBar,A[m,i:])/dot(wiBar,wiBar)*wiBar
            
        #Cálculo de HT
        for m in range(len(I)):
            I[m,i:]=I[m,i:]-2*dot(wiBar,I[m,i:])/dot(wiBar,wiBar)*wiBar
    
    np.set_printoptions(precision=5, suppress=True,edgeitems=10,linewidth=100000)
    print("\nMatriz Tridiagonalizada Simétrica:")
    print(A)
    print("\nMatriz HT:")
    print(I)
    return (A, I)
    
def QR(A,V,error):
       
    k=0 #Contador das iterações
    n=1 #Subtrador do lenA para mudar o índice de beta sendo analisado quando o erro desejado for atingido
    """
    while abs(A[len(A)-n,len(A)-(n+1)])==0:
        n+=1
    """
    while abs(A[len(A)-n,len(A)-(n+1)]) >= error or len(A)-(n+1)>-1: 
        
        ##i: Contador das rotações e fornecedor do índice. store_Q: Armazenador das matrizes de rotação. Ambos resetados a cada iteração
        i=1 
        store_Q=[]
    
        ##Fazendo a heurística de Wilkinson conforme o enunciado do EP
        ##Adicionando condição para a primeira iteração em que u=0
        if k==0:
            u=0
        else:
            d=(A[len(A)-(n+1),len(A)-(n+1)]-A[len(A)-n,len(A)-n])/2
            if d >= 0:
                sgnd=1
            else:
                sgnd=-1
            u=A[len(A)-n,len(A)-n]+d-sgnd*np.sqrt(d**2+A[len(A)-n,len(A)-(n+1)]**2)
    
        ##Fazendo o deslocamento espectral antes das rotações
        A=A-u*np.identity(len(A))
    
    
        ##Loop para fornecer os índices de posição da matriz A de maneira a percorrer ela
        while i <= len(A)-1:
            ##Sempre resetando a matriz Q de rotação para uma matriz de zeros que será definida em cada iteração
            Q=np.zeros((len(A),len(A))) 
    
            c=A[i-1,i-1]/np.sqrt(A[i-1,i-1]**2+A[i,i-1]**2)
            s=-A[i,i-1]/np.sqrt(A[i-1,i-1]**2+A[i,i-1]**2)
    
            ##Loop para calcular os novos valores de A com a rotação
            for col in range(len(A)):
                #Definindo as duas variáveis simultaneamente pois a referência muda se forem definidas sequencialmente
                A[i-1,col], A[i,col] = c*A[i-1,col]-s*A[i,col], s*A[i-1,col]+c*A[i,col] 
    
    
            ##Definindo a matriz Q
            Q[i-1,i-1]=c
            Q[i-1,i]=-s
            Q[i,i-1]=s
            Q[i,i]=c
            Q[range(i+1,len(A)),range(i+1,len(A))]=1
            Q[range(i-1),range(i-1)]=1
    
    
            ##Ao fazer uma cópia evita-se o problema da matriz anexada no armazenamento mude de valor indevidamente
            store_Q.append(Q.copy()) 
            i += 1
    
    
        ##Calculando RQi^T para o calculo do A_k+1 e VQi^T para o calculo do V_k+1 resgatando as matrizes de rotação do armazenamento
        for x in range(i-1):
            A=np.matmul(A,store_Q[x].transpose())
            V=np.matmul(V,store_Q[x].transpose())
    
        ##Fazendo o deslocamento espectral novamente após as rotações
        A=A+u*np.identity(len(A))
    
        ##Quando o erro do beta atual é menor que o estabelecido aumenta o contador para analisar o proximo beta 
        if abs(A[len(A)-n,len(A)-(n+1)])<=error:
            ##Aproximando o valor de beta analisado para zero quando a precisão desejada é atingida
            A[len(A)-n,len(A)-(n+1)]=0.0 
            n+=1
            if len(A)-n==0:
                for i in range(1,len(A)):
                    if A[i,i-1]>=1e-6:
                        n=1
        k+=1
    
    print("\nMatriz A Final:")
    print(A,"\n")
    print("Matriz V Final:")
    print(V,"\n")
    print("iterações k com deslocamento:", k)
    print(" ")
    
    return (A,V)

#--------------------------------4.1 Item A-----------------------------------#
def itemA(A=None,flag=None):
    
    #Condicionais para checar se há entrada do usuário ou é o caso default
    if flag==None:
        A=np.array([[2.,4.,1.,1.],[4.,2.,1.,1.],[1.,1.,1.,2.],[1.,1.,2.,1.]])
        reminder=True
    else:
        reminder=False
    
    
    print("\n",A)
    eigenAns=np.array([7.,2.,-1.,-2])
    Acopy=A.copy()
    
    #Execução dos algoritmos
    resultHH=HH(A)
    
    resultQR=QR(resultHH[0],resultHH[1],1e-6)
    Af=resultQR[0]
    V=resultQR[1]
    
    #Obtenção dos autovalores em uma lista
    eigenAlgo=[]
    for i in range(len(Af)):
        eigenAlgo.append(Af[i,i])
    eigenAlgo=np.asarray(eigenAlgo)
    
    #Checando se todos os autovalores e autovetores satisfazem suas condições
    for i in range(len(V)):
        print("A*v"+str(i+1)+"=",np.matmul(Acopy,V[:,i])," λ"+str(i+1)+"*v"+str(i+1)+"=",Af[i,i]*V[:,i], " Iguais:", np.allclose(np.matmul(Acopy,V[:,i]),Af[i,i]*V[:,i],rtol=1e-6,atol=1e-6),"\n")
    
    #Checagem para o autovetor
    print("V*V^T:\n",np.matmul(V,V.transpose()),"\n\nV*V^T = I:",np.allclose(np.matmul(V,V.transpose()),np.identity(len(V)),rtol=1e-6,atol=1e-6))
    
    print("\nSoluções Calculadas:",np.sort(eigenAlgo))
    if reminder==True:
        print("\nSoluções analíticas:",np.sort(eigenAns))
        print("\nAutovalores dados iguais a Autovetores Calculados:",np.allclose(np.sort(eigenAns),np.sort(eigenAlgo),rtol=1e-6,atol=1e-6))
       
    
    
#---------------------------------4.1 Item B----------------------------------#
def itemB(A=None,flag=None):
    
    if flag==None:
        #Montando a matriz de entrada
        A=np.zeros((20,20))
        n=20
        A[0,0]=n
        for i in range(1,len(A)):
            A[i,:i+1]=np.full((1,i+1),n-i)
            A[:i,i]=np.full((1,i),n-i)
        Acopy=A.copy()
    
        #Calculando os autovetores Analíticos
        eigenAns=[]
        for i in range(1,21):
            lamb=1/(2*(1-np.cos(((2*i-1)*np.pi)/(2*n+1))))
            eigenAns.append(lamb)
        eigenAns=np.asarray(eigenAns)
        
        reminder=True
    else:
        Acopy=A.copy()
        reminder=False
        
    print("\n",A)
    
    #Solução
    resultHH=HH(A)
    
    resultQR=QR(resultHH[0],resultHH[1],1e-6)
    Af=resultQR[0]
    V=resultQR[1]
    
    eigenAlgo=[] #Vamos armazenar os autovalores em uma lista pra comparar com os calculados analiticamente
    for i in range(len(Af)):
        eigenAlgo.append(Af[i,i])
    eigenAlgo=np.asarray(eigenAlgo)
        
    #Saídas
    for i in range(len(V)):
        print("A*v"+str(i+1)+"=",np.matmul(Acopy,V[:,i])," λ"+str(i+1)+"*v"+str(i+1)+"=",Af[i,i]*V[:,i], " Iguais:", np.allclose(np.matmul(Acopy,V[:,i]),Af[i,i]*V[:,i],rtol=1e-6,atol=1e-6),"\n")
     
    print("V*V^T:\n",np.matmul(V,V.transpose()),"\n\nV*V^T = I:",np.allclose(np.matmul(V,V.transpose()),np.identity(len(V)),rtol=1e-6,atol=1e-6))       
    
    
    print("\nSoluções Calculadas:",np.sort(eigenAlgo))
    if reminder==True:
        print("\nSoluções analíticas:",np.sort(eigenAns))    
        print("\nAutovalores analíticos iguais a autovalores Calculados:",np.allclose(np.sort(eigenAns),np.sort(eigenAlgo),rtol=1e-06,atol=1e-06))
        
#-------------------------------4.2 Item C------------------------------------#
def itemC(fileName):
    
    #Checando se o arquivo de entrada está na mesma pasta
    while True:
        try:
            inputCFile=open(os.path.join(os.path.dirname(__file__), fileName),"r")
                   
            list_of_CFile = []
            for line in inputCFile:
                stripped_line = line.strip()
                line_list = stripped_line.split()
                if line_list!=[]:
                    list_of_CFile.append(line_list)
            
            inputCFile.close()
            break
        except FileNotFoundError:
            print("\nO arquivo input-c não se encontra na mesma pasta que o código ou possui outro nome. Verifique e rode o código novamente.")
            sys.exit()
            
    #Checando a formatação do arquivo
    while True:
        try:
            barsDic={(int(list_of_CFile[i][0]),int(list_of_CFile[i][1])):(float(list_of_CFile[i][2]),float(list_of_CFile[i][3])) for i in range(2,len(list_of_CFile))}
            #print(barsDic)
            
            rho=float(list_of_CFile[1][0])
            Ar=float(list_of_CFile[1][1])
            E=float(list_of_CFile[1][2])*1e9
            
            nPosUnfixedKnots=int(list_of_CFile[0][1])*2
            nBars=int(list_of_CFile[0][2])
            break
        except ValueError:
            print("\nArquivo não está formatado corretamente para este item. Rode o código novamente e escolha outro arquivo ou corrija a formatação.")
            sys.exit()
        
    matrixK=np.zeros((nBars,nBars))
    matrixM=np.zeros((nPosUnfixedKnots,nPosUnfixedKnots))
    
    #Iterar sobre todas as barras para montar a matriz k de cada uma
    for bar, info in barsDic.items():
        k=np.zeros((4,4))
        #Calculando os dois casos de linha que matriz k possui
        kc=np.array([np.cos(np.radians(info[0]))**2,np.cos(np.radians(info[0]))*np.sin(np.radians(info[0])),(np.cos(np.radians(info[0]))**2)*(-1),np.cos(np.radians(info[0]))*np.sin(np.radians(info[0]))*(-1)])
        ks=np.array([np.sin(np.radians(info[0]))**2,np.cos(np.radians(info[0]))*np.sin(np.radians(info[0]))*(-1),(np.sin(np.radians(info[0]))**2)*(-1)])
        
        #Distribuindo na matriz k cada linha
        k[0,:]=kc
        k[1:,0]=kc[1:]
        
        k[1,1:]=ks
        k[2:,1]=ks[1:]
            
        k[2,2:]=kc[:2]
        k[3,2]=kc[1]
        
        k[3,3]=ks[0]
        
        k=(Ar*E/info[1])*k
        
        #Distribuindo valores de k na matriz total K
        
        #linha 1
        matrixK[2*bar[0]-2,2*bar[0]-2]+=k[0,0]
        matrixK[2*bar[0]-2,2*bar[0]-1]+=k[0,1]
        matrixK[2*bar[0]-2,2*bar[1]-2]+=k[0,2]
        matrixK[2*bar[0]-2,2*bar[1]-1]+=k[0,3]
        
        #linha 2
        matrixK[2*bar[0]-1,2*bar[0]-2]+=k[1,0]
        matrixK[2*bar[0]-1,2*bar[0]-1]+=k[1,1]
        matrixK[2*bar[0]-1,2*bar[1]-2]+=k[1,2]
        matrixK[2*bar[0]-1,2*bar[1]-1]+=k[1,3]
        
        #linha 3
        matrixK[2*bar[1]-2,2*bar[0]-2]+=k[2,0]
        matrixK[2*bar[1]-2,2*bar[0]-1]+=k[2,1]
        matrixK[2*bar[1]-2,2*bar[1]-2]+=k[2,2]
        matrixK[2*bar[1]-2,2*bar[1]-1]+=k[2,3]
        
        #linha 4
        matrixK[2*bar[1]-1,2*bar[0]-2]+=k[3,0]
        matrixK[2*bar[1]-1,2*bar[0]-1]+=k[3,1]
        matrixK[2*bar[1]-1,2*bar[1]-2]+=k[3,2]
        matrixK[2*bar[1]-1,2*bar[1]-1]+=k[3,3]
    
        #Distribuindo as contribuições de massa na matriz de massa M
        m=0.5*rho*Ar*info[1]
        #Somando para o nó i
        matrixM[2*bar[0]-2,2*bar[0]-2]+=m
        matrixM[2*bar[0]-1,2*bar[0]-1]+=m
        #Somando para o nó j exluindo os nós 13 e 14
        if bar[1]<=int(nPosUnfixedKnots/2):
            matrixM[2*bar[1]-2,2*bar[1]-2]+=m
            matrixM[2*bar[1]-1,2*bar[1]-1]+=m
        
    #Extraindo apenas a parte 24x24 da matriz calculada
    matrixK=matrixK[:nPosUnfixedKnots,:nPosUnfixedKnots]
    
    
    
    #Montando a matriz M^(-1/2)
    matrixMInv=matrixM.copy()
    for i in range(len(matrixMInv)):    
        matrixMInv[i,i]=np.sqrt(1/matrixMInv[i,i])
        
    
    #Multiplicação de MInv a esquerda
    for i in range(len(matrixK)):
        for j in range(i,len(matrixK)):
            matrixK[i,j]=dot(matrixMInv[i],matrixK[j])
            matrixK[j,i]=matrixK[i,j] #Igualando a simetria
    
    #Multiplicação de MInv a direita
    for i in range(len(matrixMInv)):
        for j in range(i,len(matrixMInv)):
            matrixK[i,j]=dot(matrixK[i],matrixMInv[j])
            matrixK[j,i]=matrixK[i,j]
    
    #Solução da matriz K~ com método de householder e algoritmo QR retornando seus autovalores e autovetores
    
    resultHH=HH(matrixK)
    matrixK=resultHH[0]
    matrixHT=resultHH[1]
    
    resultQR=QR(matrixK,matrixHT,1e-10)
    matrixK=resultQR[0]
    matrixHT=resultQR[1]
    
    
    eigenAlgo=[] #Vamos armazenar os autovalores em uma lista
    for i in range(len(matrixK)):
        eigenAlgo.append(matrixK[i,i])
    eigenAlgo=np.sort(np.asarray(eigenAlgo))
    
    #Pegando os primeiros 5 autovalores
    firstEigens=eigenAlgo[:5]
    
    #Checando se não há zeros, caso sim desconsiderá-los
    count=1
    for i in range(len(eigenAlgo[:5])):
        if abs(eigenAlgo[i])<=1e-6:
            firstEigens[i]=0.0
            firstEigens=np.append(firstEigens,eigenAlgo[4+count])
            count+=1
    
    firstEigens=np.sqrt(firstEigens)
            
    print("\n5 menores frequências sem contar os zeros:")
    for i in range(len(firstEigens)):
        print("ω"+str(i+1)+": ",firstEigens[i])
    
    print("\n5 autovetores correspondentes:\n")
    #Como os autovalores foram "bagunçados" precisamos achar seus índices na matriz de autovalores base e usá-los para pegar os autovetores correspondentes
    for i in range(len(firstEigens)):
        print("v"+str(i+1)+": ", matrixHT[:,np.where(matrixK==eigenAlgo[i])[0][0]],"\n")
    

#------------------------------UI e execução------------------------------------#
while True:
    while True:
        itemTarefa=input("Escolha entre o item a, b ou c: ").lower()
        if itemTarefa.lower() not in ("a", "b","c"):
            print("Entrada Inválida")
        else:
            break
    
    
    while True:
        userChoice=input("Deseja inserir sua própria entrada? (S/N): ").lower()
        if userChoice.lower() not in ("s", "n"):
            print("Entrada Inválida")
        else:
            break
        
    if userChoice=="s":
        
        if itemTarefa=="c":
            userChoice2="2"
        else:
            while True:
                userChoice2=input("Deseja digitar a matriz (1) ou escolher arquivo formatado igual os inputs do EP (2)? Escolha 1 ou 2: ").lower()
                if userChoice2.lower() not in ("1", "2"):
                    print("Entrada Inválida")
                else:
                    break
        
        if userChoice2=="1":
            while True:
                 try:
                     ordem = int(input("Digite a ordem da matriz: "))
                     if ordem<=1:
                         print("\nEntrada Inválida. Digite um número inteiro maior que 1")
                     else:
                        break
                 except ValueError:
                     print("\nEntrada inválida. Digite apenas números")
                     
            print("\nDigite agora os valores de cada linha,da diagonal principal para cima, começando pela linha 1. Separe os valores com espaços\n")
            print("Lembrete: Apenas os valores da diagonal para cima pois a matriz de entrada deve ser simétrica\n")
            userList=[]
            for i in range(ordem):
                while True:
                    try: 
                        userLine = list(map(float,input("Digite "+str(ordem-i)+" valores para a linha "+str(i+1)+": ").strip().split()))
                        if len(userLine)==ordem-i:
                            userList.append(userLine)
                            break
                        else:
                            print("\nEntrada Inválida. Digite a linha com ",ordem-i,"elementos")
                    except ValueError:
                        print("\nEntrada Inválida. Digite apenas números separados por espaços")
                        
            userMatrix=np.zeros((ordem,ordem))
            for i in range(len(userList)):
                userMatrix[i,i:]=userList[i]
                userMatrix[i+1:,i]=userList[i][1:]
                
        elif userChoice2=="2":
            while True:
                 try:
                     fileName=str(input("Digite o nome do arquivo. O arquivo deve estar na mesma pasta que o código. "))
                     filePath=open(os.path.join(os.path.dirname(__file__),fileName))
                     break
                 except FileNotFoundError:
                     print("\nArquivo inexistente ou não encontrado")
            
            filePath.close()
        
    if itemTarefa=="a":
        if userChoice=="n":
            itemA()
        elif userChoice2=="1":
            itemA(userMatrix,flag="yes")
        else:
            itemA(interpretFile(fileName),flag="yes")
            
    
    elif itemTarefa=="b":
        if userChoice=="n":
            itemB()
        elif userChoice2=="1":
            itemB(userMatrix,flag="yes")
        else:
            itemB(interpretFile(fileName),flag="yes")
        
    elif itemTarefa=="c":
        if userChoice=="n":    
            itemC("input-c")
        else:
            itemC(fileName)

    while True:
        answer = str(input('Rodar o código novamente? (S/N): ')).lower()
        if answer in ('s', 'n'):
            break
        print("Entrada Inválida")
    if answer == 's':
        print("\n")
        continue
    else:
        print("\nTchau, até mais")
        break
    


