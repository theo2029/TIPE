""" Pour une matrice (n,n) on cherchera comment placer k points 
dans la matrice de telle sorte que tout point de la matrice soit
à une distance minimal d'un point k"""

from random import *


n = 20
M = [[(i,j) for j in range(n)] for i in range(n)]

def distance_a_la_diago(i,j): 
    return abs(i-j)

def distance_euclidienne(A,B):
    return ((A[1]-B[1])**2+(A[0]-B[0])**2)**(0.5)

def distance_man(A,B):
    return abs(A[1]-B[1]) + abs(A[0]-B[0])

#X = distance_man([0,0],[3,3])
#print(X)
def moyenne_de_liste(L):
    n = len(L)
    S = sum(L[i] for i in range(n))
    return S/n

def moyenne_aux_points(X,M,distance): #M est la matrice ville, X un point de la matrice
    """ Cette fonction donne pour un point de la ville, la moyenne de la distance à l'ensemble des points 
    de la ville (ici la ville est représentée par une matrice"""
    L = []
    for i in range(n):
        for j in range(n):
            K = [i,j]
            L = L + [distance([i,j] ,X )]

    return moyenne_de_liste(L)

"""moy = moyenne_aux_points([10,10],M, distance_man)
print(moy)"""

def RechercheDeSolution (M,k,distance,nbr_test): #M une matrice, d une distance k nombre de points
    """On va faire la moyenne des moyennes des distances aux points de la matrice"""
    #La distance maximale pour d est d = 2n pour manhatann

    MeilleureConfiguration=[]
    MeilleureMoyenne = -1

    for geoffrey in range(nbr_test): #On test nbr_test fois
        Points = [[randint(0,n),randint(0,n)]] #On met un point dans la liste
        i,j=0,0

        while len(Points) < k : #On veut mettre k points dans la liste
            x,y = randint(0,n),randint(0,n)
            if [x,y] not in Points :
                Points.append([x,y])
            if i%1000 == 0: 
                print(i)
            i=i+1
        #On a désormais une liste de points distincts que l'on stocke au cas ou elle serait cool
        Moyennes=[moyenne_aux_points(Points[i],M,distance_man) for i in range(k)]
        MoyenneGlobale = moyenne_de_liste(Moyennes)
        if MoyenneGlobale > MeilleureMoyenne or MeilleureMoyenne < 0:
            MeilleureMoyenne = MoyenneGlobale
            MeilleureConfiguration = Points
    return MeilleureConfiguration , MeilleureMoyenne

Test = RechercheDeSolution(M,3,distance_man,100000)
print(Test)
    

        
    

        
    

    




