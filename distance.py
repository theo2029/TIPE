""" Pour une matrice (n,n) on cherchera comment placer k points 
dans la matrice de telle sorte que tout point de la matrice soit
à une distance minimal d'un point k"""

from random import randint
import matplotlib.pyplot as plt
from time import *

n = 20
M = [[(i,j) for j in range(n)] for i in range(n)]
densite = [[0 for i in range(n)] for j in range(n)] #villeDe0
loop = 0

def distance_a_la_diago(i,j): 
    return abs(i-j)

def distance_euclidienne(A,B):
    return ((A[1]-B[1])**2+(A[0]-B[0])**2)**(0.5)

def distance_man(A,B):
    return abs(A[1]-B[1]) + abs(A[0]-B[0])

def moyenne_de_liste(L):
    n = len(L)
    S = sum(L[i] for i in range(n))
    return S/n

def moyenne_aux_points(X,M,distance): #M est la matrice ville, X un point de la matrice
    """ Cette fonction donne pour un point de la ville, la moyenne de la distance à 
    l'ensemble des points de la ville (ici la ville est représentée par une matrice"""
    L = []
    for i in range(n):
        for j in range(n):
            if [i,j] != X: #Le point ne compte pas lui meme dans la moyenne !!
                L = L + [distance([i,j] ,X )]
    return moyenne_de_liste(L)

def RechercheDeSolution (M,k,distance,nbr_test): #M une matrice, d une distance k nombre de points
    """On va faire la moyenne des moyennes des distances aux points de la matrice"""
    #La distance maximale pour d est d = 2n pour manhatann

    MeilleureConfiguration=[]
    MeilleureMoyenne = -1

    for J in range(nbr_test): #On test nbr_test fois
        Points = [[randint(0,n),randint(0,n)]] #On met un point dans la liste
        while len(Points) < k : #On veut mettre k points dans la liste
            x,y = randint(0,n),randint(0,n)
            if [x,y] not in Points :
                Points.append([x,y])
        #On a désormais une liste de points distincts que l'on stocke au cas ou elle serait cool
        Moyennes=[moyenne_aux_points(Points[i],M,distance_man) for i in range(k)]
        MoyenneGlobale = moyenne_de_liste(Moyennes)
        if MoyenneGlobale < MeilleureMoyenne or MeilleureMoyenne < 0:
            MeilleureMoyenne = MoyenneGlobale
            MeilleureConfiguration = Points
        if J%100 == 0: print(J)

    return MeilleureConfiguration , MeilleureMoyenne

"""Résultats et problèmes:
On trouve pour k=3 et M : 10x10, trois points au centre de la matrice
([[4, 4], [5, 5], [4, 5]], 5.0)
ce qui est mathématiquement correcte mais pas optimal dans la réalité, en effet
toutes les casernes seront collées à un points du centre. """

def Interdistance (X,ListeDePoints,interdistance,distance): #return un booléen
    for point in ListeDePoints:
        if distance(X,point) < interdistance : return False
    return True

def RechercheDeSolution_V2 (M,k,distance, interdistance,nbr_test): #M une matrice, k nombre de points
    """On va faire la moyenne des moyennes des distances aux points de la matrice"""
    #La distance maximale pour d est d = 2n pour manhatann
    MeilleureConfiguration=[]
    MeilleureMoyenne = -1
    global n
    for J in range(nbr_test+1): #On test nbr_test fois
        Points = [[randint(0,n),randint(0,n)]] #On met un point dans la liste (initialisation)
        """ remarque post mortem:
        Tous les points suivront dépendent de ce point choisi aléatoirement...
        Mais ce n'est pas si grave puisque l on répète l operaiton plein de fois"""
        while len(Points) < k : #On veut mettre k points dans la liste
            x,y = randint(0,n),randint(0,n)
            if [x,y] not in Points and Interdistance([x,y],Points,interdistance,distance_man) :
                Points.append([x,y])
        #On a désormais une liste de points distincts que l'on stocke au cas ou elle serait cool
        Moyennes=[moyenne_aux_points(Points[i],M,distance_man) for i in range(k)]
        MoyenneGlobale = moyenne_de_liste(Moyennes)
        if MoyenneGlobale < MeilleureMoyenne or MeilleureMoyenne < 0:
            MeilleureMoyenne = MoyenneGlobale
            MeilleureConfiguration = Points
        if J%100==0:print(J)
    print(MeilleureConfiguration)
    return MeilleureConfiguration , MeilleureMoyenne, interdistance,k,nbr_test

def Affichage_Sauvegarde(Liste):
    global densite
    global loop
    global n
    VDZ = [[0 for i in range(n)] for j in range(n)] #Ville de zeros
    for Test in Liste:
        loop+=1
        for point in Test[0]:
            i = point[0]
            j = point[1]
            VDZ[i][j] += 1
        
        MeilleureMoyenne=Test[1];interdistance=Test[2];k=Test[3];nbr_test=Test[4] #oui

        plt.imshow(VDZ, extent=[0,n,0,n], aspect="auto")
        plt.title("n="+str(n)+",k="+str(k)+",inter="+str(interdistance)+',boucles='+str(nbr_test))
        plt.savefig(str(loop)+'.png')
        VDZ = [[0 for i in range(n)] for j in range(n)] 
T1 = time()
D = [RechercheDeSolution_V2(M,5,distance_man,10,50) for i in range(5)]
DT = time()-T1
print(DT)
Affichage_Sauvegarde(D)


