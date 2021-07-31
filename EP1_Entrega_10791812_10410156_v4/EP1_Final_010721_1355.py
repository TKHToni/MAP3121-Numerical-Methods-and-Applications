#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------------Inputs do usuário------------------------------------------------------------

#Todo o corpo do código está inserido dentro de um loop para possibilitar o usuário a repetir ou não o código no final 
while True:
    while True:
        itemTarefa=input("Escolha entre o item a, b ou c: ").lower()
        if itemTarefa.lower() not in ("a", "b","c"):
            print("Entrada Inválida")
        else:
            break

    if itemTarefa=="a":
        userChoice="c"
        while True:
            dimension=input("Escolha a dimensão n=4,8,16 ou 32: ")
            if dimension not in ("4", "8", "16", "32"):
                print("Entrada Inválida")
            else:
                break

    if itemTarefa=="b":
        while True:
            userChoice=input("Escolha com ou sem deslocamento espectral (C/S): ").lower()
            if userChoice not in ("c", "s"):
                print("Entrada Inválida")
            else:
                break
                
        while True:
            userInput=input("Deseja escolher a ordem n da matriz e seus X0? (S/N): ").lower()
            if userInput not in ("s", "n"):
                print("Entrada Inválida")
            else:
                break
                
        if userInput=="s":
            while True:
                userN=input("Digite um número inteiro maior que 1 para ordem n: ")
                try:
                    int(userN)
                    it_is = True
                except ValueError:
                    it_is = False
                if it_is==False or it_is==True and int(userN)<=1:
                    print("Entrada Inválida")
                else:
                    userN=int(userN)
                    break 
            while True:
                try: 
                    userX0 = list(map(float,input("Digite os valores: ").strip().split()))
                    if userN==len(userX0):
                        break
                    else:
                        print("Entrada Inválida. Digite uma matriz de ordem",userN)
                except ValueError:
                    print("Entrada Inválida. Digite apenas números separados por espaços")
            
        else:
            while True:
                case=input("Escolha entre os casos 1 (X(0)=-2,-3,-1,-3,-1), 2 (X(0)=1,10,-4,3,-2) ou 3 (X(0) correspondente ao modo de maior frequência): ")
                if case.lower() not in ("1", "2","3"):
                    print("Entrada Inválida")
                else:
                    break

    elif itemTarefa=="c":
        while True:
            userChoice=input("Escolha com ou sem deslocamento espectral (C/S): ").lower()
            if userChoice not in ("c", "s"):
                print("Entrada Inválida")
            else:
                break
                
        while True:
            userInput=input("Deseja escolher a ordem n da matriz e seus X0? (S/N): ").lower()
            if userInput not in ("s", "n"):
                print("Entrada Inválida")
            else:
                break
                
        if userInput=="s":
            while True:
                userN=input("Digite um número inteiro maior que 1 para ordem n: ")
                try:
                    int(userN)
                    it_is = True
                except ValueError:
                    it_is = False
                if it_is==False or it_is==True and int(userN)<=1:
                    print("Entrada Inválida")
                else:
                    userN=int(userN)
                    break 
            while True:
                try: 
                    userX0 = list(map(float,input("Digite os valores: ").strip().split()))
                    if len(userX0)==userN:
                        break
                    else:
                        print("Entrada Inválida. Digite uma matriz de ordem",userN)
                except ValueError:
                    print("Entrada Inválida. Digite apenas números separados por espaços")
        else:
            while True:
                case=input("Escolha entre os casos 1, 2 ou 3: ")
                if case.lower() not in ("1", "2","3"):
                    print("Entrada Inválida")
                else:
                    break

    print(" ")

    #---------------------------------------Definindo condições iniciais para cada Item------------------------------------------------------------------------------
    if itemTarefa=="a":
        ##Definindo a matriz A
        N=int(dimension)
        A=np.zeros((N,N))
        for q in range(N):
            A[q,q]=2.0
            if q>=1:
                A[q,q-1]=-1.0
                A[q-1,q]=-1.0
        copyA=A.copy()
        print("Matriz A:")
        print(A)
        print(" ")

    elif itemTarefa=="b":
        if userInput=="n":
            ##Definindo os k's das molas
            store_K=[]
            for q in range(1,7):
                store_K.append(40+2*q)
            print("K das molas:")
            print(store_K)
            print(" ")

            ##Definindo a matriz A
            m=2.0
            N=5
            A=np.zeros((N,N))
            for q in range(N):
                A[q,q]=store_K[q]+store_K[q+1]
                if q>=1:
                    A[q,q-1]=-store_K[q]
                    A[q-1,q]=-store_K[q]
            A=A*(1/m)
            print("Matriz A:")
            print(A)
            print(" ")
        else:
            store_K=[]
            for q in range(1,userN+2):
                store_K.append(40+2*q)
            print("K das molas:")
            print(store_K)
            print(" ")

            ##Definindo a matriz A
            m=2.0
            N=userN
            A=np.zeros((N,N))
            for q in range(N):
                A[q,q]=store_K[q]+store_K[q+1]
                if q>=1:
                    A[q,q-1]=-store_K[q]
                    A[q-1,q]=-store_K[q]
            A=A*(1/m)
            print("Matriz A:")
            print(A)
            print(" ")   
    elif itemTarefa=="c":
        if userInput=="n":
            ##Definindo os k's das molas
            store_K=[]
            for q in range(1,12):
                store_K.append(40+2*(-1)**q)
            print("K das molas:")
            print(store_K)
            print(" ")

            ##Definindo a matriz A
            m=2.0
            N=10
            A=np.zeros((N,N))
            for q in range(N):
                A[q,q]=store_K[q]+store_K[q+1]
                if q>=1:
                    A[q,q-1]=-store_K[q]
                    A[q-1,q]=-store_K[q]
            A=A*(1/m)
            print("Matriz A:")
            print(A)
            print(" ")
        else:
            store_K=[]
            for q in range(1,userN+2):
                store_K.append(40+2*(-1)**q)
            print("K das molas:")
            print(store_K)
            print(" ")

            ##Definindo a matriz A
            m=2.0
            N=userN
            A=np.zeros((N,N))
            for q in range(N):
                A[q,q]=store_K[q]+store_K[q+1]
                if q>=1:
                    A[q,q-1]=-store_K[q]
                    A[q-1,q]=-store_K[q]
            A=A*(1/m)
            print("Matriz A:")
            print(A)
            print(" ")            


    V=np.identity(len(A)) #Matriz autovetores inicial
    k=0 #Contador das iterações
    n=1 #Subtrador do lenA para mudar o índice de beta sendo analisado quando o erro desejado for atingido

    #--------------Fornecedor da matriz A diagonalizada e da matriz de autovetores V com deslocamentos--------------------------------------
    if itemTarefa=="a" or userChoice=="c":
        while abs(A[len(A)-n,len(A)-(n+1)]) >= 1e-6 and len(A)-(n+1)>-1:

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
            if abs(A[len(A)-n,len(A)-(n+1)])<=1e-6:
                ##Aproximando o valor de beta analisado para zero quando a precisão desejada é atingida
                A[len(A)-n,len(A)-(n+1)]=0.0 
                n+=1

            k+=1

        print("Matriz A Final:")
        print(A)
        print(" ")
        print("Matriz V Final:")
        print(V)
        print(" ")
        print("iterações k com deslocamento:", k)
        print(" ")

    #---------------------------------Calculo da Matriz A final sem deslocamento---------------------------------------------------
    if itemTarefa=="a" or userChoice=="s":
        
        if userChoice=="s":
            copyA=A
        V=np.identity(len(A))
        k=0 
        n=1 

        while abs(copyA[len(copyA)-n,len(copyA)-(n+1)]) >= 1e-6 and len(copyA)-(n+1)>-1:

            ##i: Contador das rotações e fornecedor do índice. store_Q: Armazenador das matrizes de rotação. Ambos resetados a cada iteração
            i=1 
            store_Q=[]

            ##Loop para fornecer os índices de posição da matriz A de maneira a percorrer ela
            while i <= len(copyA)-1:
                ##Sempre resetando a matriz Q de rotação para uma matriz de zeros que será definida em cada iteração
                Q=np.zeros((len(copyA),len(copyA))) 

                c=copyA[i-1,i-1]/np.sqrt(copyA[i-1,i-1]**2+copyA[i,i-1]**2)
                s=-copyA[i,i-1]/np.sqrt(copyA[i-1,i-1]**2+copyA[i,i-1]**2)

                ##Loop para calcular os novos valores de A com a rotação
                for col in range(len(copyA)):
                    #Definindo as duas variáveis simultaneamente pois a referência muda se forem definidas sequencialmente
                    copyA[i-1,col], copyA[i,col] = c*copyA[i-1,col]-s*copyA[i,col], s*copyA[i-1,col]+c*copyA[i,col] 


                ##Definindo a matriz Q
                Q[i-1,i-1]=c
                Q[i-1,i]=-s
                Q[i,i-1]=s
                Q[i,i]=c
                Q[range(i+1,len(copyA)),range(i+1,len(copyA))]=1
                Q[range(i-1),range(i-1)]=1


                ##Ao fazer uma cópia evita-se o problema da matriz anexada no armazenamento mude de valor indevidamente
                store_Q.append(Q.copy()) 
                i += 1


            ##Calculando RQi^T para o calculo do A_k+1 e VQi^T para o calculo do V_k+1 resgatando as matrizes de rotação do armazenamento
            for x in range(i-1):
                copyA=np.matmul(copyA,store_Q[x].transpose())
                V=np.matmul(V,store_Q[x].transpose())

            ##Quando o erro do beta atual é menor que o estabelecido aumenta o contador para analisar o proximo beta 
            if abs(copyA[len(copyA)-n,len(copyA)-(n+1)])<=1e-6:
                ##Aproximando o valor de beta analisado para zero quando a precisão desejada é atingida
                copyA[len(copyA)-n,len(copyA)-(n+1)]=0.0 
                n+=1

            k+=1
        if itemTarefa=="a":
            print("iterações k sem deslocamento: ", k)
            print(" ")
        else:
            print("Matriz A Final:")
            print(copyA)
            print(" ")
            print("Matriz V Final:")
            print(V)
            print(" ")
            print("iterações k sem deslocamento:", k)
            print(" ")
            A=copyA
            
        
        #----------------------Calculando autovalores e autovetores Analiticamente----------------------------------------------
        if itemTarefa=="a":
            lambdasAnalit=[]
            eigenVectorsAnalit=[]
            for j in range(1,len(copyA)+1):
                vector=[]
                lambdasAnalit.append(2*(1-np.cos((j*np.pi)/(len(copyA)+1))))
                for i in range(1,len(copyA)+1):
                    vector.append(np.sin((j*i*np.pi)/(len(copyA)+1)))
                eigenVectorsAnalit.append(vector)

            if len(copyA)==4:
                print(" ")
                print("Autovalores Analiticamente: ")
                for i in range(len(lambdasAnalit)):
                    print("λ"+str(i+1)+"="+str(lambdasAnalit[i]),end=" ")
                print(" ")
                print(" ")
                print("Autovetores Analiticamente: ")
                for j in range(len(eigenVectorsAnalit)):
                    print("v"+str(j+1)+"="+str(eigenVectorsAnalit[j]))
                    print(" ")
            else:
                while True:
                    show=input("Deseja ver os resultados analíticos? (S/N): ").lower()
                    if show.lower() not in ("s", "n"):
                        print("Entrada Inválida")
                    else:
                        break
                if show=="s":
                    print(" ")
                    print("Autovalores Analiticamente: ")
                    for i in range(len(lambdasAnalit)):
                        print("λ"+str(i+1)+"="+str(lambdasAnalit[i]),end=" ")
                    print(" ")
                    print(" ")
                    print("Autovetores Analiticamente: ")
                    for j in range(len(eigenVectorsAnalit)):
                        print("v"+str(j+1)+"="+str(eigenVectorsAnalit[j]))
                        print(" ")
            

    #----------------------------------Equação matricial do movimento das massas------------------------------------------------

    if itemTarefa=="b" or itemTarefa=="c":

        #Matriz de tempo
        T=[]
        t=0.0
        while t<10.0:
            T.append(t)
            t+=0.025

        #Posições iniciais
        if userInput=="n":
            if case=="1":
                initPositions=np.array([-2.0,-3.0,-1.0,-3.0,-1.0])
                if itemTarefa=="c":
                    initPositions=np.append(initPositions,initPositions)

            elif case=="2":
                initPositions=np.array([1.0,10.0,-4.0,3.0,-2.0])
                if itemTarefa=="c":
                    initPositions=np.append(initPositions,initPositions)

            elif case=="3":

                if itemTarefa=="b":
                    #Para achar o maior modo de frequencia é preciso achar o maior autovalor. Vasculhar o maior autovalor e resgatar o autovetor correspondente
                    lambdas=[]
                    for j in range(len(A)):
                        lambdas.append(A[j,j])
                    indexMax=lambdas.index(max(lambdas))
                    initPositions=np.zeros(len(V))
                    for j in range(len(V)):
                        initPositions[j]=V[j,indexMax]

                if itemTarefa=="c":
                    lambdas=[]
                    for j in range(len(A)):
                        lambdas.append(A[j,j])
                    indexMax=lambdas.index(max(lambdas))
                    initPositions=np.zeros(len(V))
                    for j in range(len(V)):
                        initPositions[j]=V[j,indexMax]

                print("Maior Autovalor e sua frequência: λ="+str(max(lambdas))+" f="+str(np.sqrt(max(lambdas))/(2*np.pi)))
                print(" ")
                print("Posições iniciais (Autovetor correspondente): "+str(initPositions))
                print(" ")
        else:
            initPositions=np.array(userX0)

        #Matriz store_X armazena os valores de posição por tempo de cada massa. Matriz gammas acha os coeficientes a e b.
        store_X=[]
        Y0=np.matmul(V.transpose(),np.array(initPositions)).tolist()

        #Armazenando valores da posição por tempo de cada massa em store_X
        for j in range(len(initPositions)):
            t=0.0
            x=[]
            while t<=10.0:
                x.append(Y0[j]*np.cos(np.sqrt(A[j,j])*t))
                t += 0.025
            store_X.append(x.copy())

        store_X=np.matmul(V,np.array(store_X))
         
    #--------------------------Calculo de deslocamento de cada mola em relação a posição de equilíbrio------------------------------
        store_Spring=[]
        for j in range(len(initPositions)+1):
            s=[]
            for q in range(len(T)):
                if j==0:
                    s.append(store_X[j][q]-0)
                elif j==len(initPositions):
                    s.append(0-store_X[j-1][q])
                else:
                    s.append(store_X[j][q]-store_X[j-1][q])
            store_Spring.append(s.copy())

    #----------------------------------------------------Plotando-------------------------------------------------------------------
        for j in range(len(initPositions)):
            plt.plot(T,store_X[j])
            plt.xlabel("Time")
            plt.ylabel("Position")
            plt.title("Massa "+str(j+1)+": Position x Time")
            plt.show()

            plt.plot(T,store_Spring[j])
            plt.xlabel("Time")
            plt.ylabel("Position Relative to Eq.")
            plt.title("Mola "+str(j+1)+": Position Relative to Eq. X Time")
            plt.show()
            if j==len(initPositions)-1:
                plt.plot(T,store_Spring[j+1])
                plt.xlabel("Time")
                plt.ylabel("Position Relative to Eq.")
                plt.title("Mola "+str(j+2)+": Position Relative to Eq. X Time")
                plt.show()
                
        #Calculando e exibindo os outros modos de vibração
        if userInput=="n":
            if case=="3":
                print("Os outros modos de vibração e suas respectivas frequências são: ")
                print(" ")
                i=0
                while i<len(lambdas):
                    if i==indexMax:
                        i+=1
                    else:
                        currentVector=[]
                        for j in range(len(V)):
                            currentVector.append(V[j,i])
                        print("f="+str(np.sqrt(lambdas[i])/(2*np.pi))+" Autovetor="+str(currentVector))
                        print(" ")
                        i+=1
                
    print("")
    while True:
        answer = str(input('Rodar o código novamente? (S/N): ')).lower()
        if answer in ('s', 'n'):
            break
        print("Entrada Inválida")
    if answer == 's':
        print("")
        continue
    else:
        print(" ")
        print("Até mais")
        break

