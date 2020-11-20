from random import randint

N = 10 #taille de la ville
n = 10 #nombre de caserne

Ville = [[[i,j] for i in range(N)] for j in range(N)] #ville

class caserne():
    def __init__(self):
        self.x = randint(1,N)
        self.y = randint(1,N)
    def nexplace(self,x,y):
        self.x = x
        self.y = y

def distance(caserne,maison):
    return abs(caserne.x-maison[0]) + abs(caserne.y-maison[1])

def Di(caserne,V): #distance par rapport à chaque point de la ville
    D = []
    for ligne in V:
        for maison in ligne:
                D += [distance(caserne,maison)]
    return D

def moyenne(liste):
    somme = 0
    for p in liste:
        somme += p
    return somme/len(liste)

def Coord(n):
    L=[]
    for i in range(n):
        for j in range(n):
            L+=[i,j]
    return L


"""def distance_minimale_sauvage(regiment, Ville ): 
    #On cherche l'ensemble des coordonnées pour que la disposition soit optimale
    C = Coord(n)
    i=0
    j=0
    for caserne in regiment: #On a n casernes
        caserne.x=i%N
        caserne.y=i//N
        i+=1
    #On a désormais l'ensemble des casernes allignés dans le carré Ville/ Cependant, est-ce utile ?
    """

regiment = [caserne() for i in range(n)]


print(len(regiment))