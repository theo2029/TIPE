from random import *
import matplotlib.pyplot as plt

N = 10 #taille de la ville
n = 3 #nombre de caserne

Ville = [[[i,j] for i in range(N)] for j in range(N)] #ville

class caserne():
    def __init__(self):
        self.x = randint(0,N-1)
        self.y = randint(0,N-1)
    def nexplace(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "caserne , x : " + str(self.x) + " , y : " + str(self.y)

def distance(caserne,maison):
    return abs(caserne.x-maison[0]) + abs(caserne.y-maison[1])

def Di(caserne,Ville): #distance par rapport a chaque point de la ville
    D = []
    for ligne in Ville:
        for maison in ligne:
                D += [distance(caserne,maison)**2] #distance mis au carre
    return D

def moyenne(liste):
    somme = 0
    for p in liste:
        somme += p
    return somme/len(liste)

def moyenne_distance_regiment(regiment,Ville):
    M = []
    for caserne in regiment:
        M += [moyenne(Di(caserne,Ville))]
    return moyenne(M)

def distance_moyenne_entre_regiment(regiment):
    S = 0
    for caserne in regiment:
        for caserne2 in regiment:
            if caserne != caserne2:
                S += (abs(caserne.x-caserne2.x) + abs(caserne.y-caserne2.y))**2
    return S/len(regiment)

"""def moyenne_distance_entre_caserne(regiment):
    M = []
    if len(regiment) == 1:
        return 1 #A REDEFIIR
    else:
        for caserne in regiment:
            for caserne2 in regiment:
                if caserne != caserne2 :
                    M += [(abs(caserne.x-caserne2.x) + abs(caserne.y-caserne2.y))**2]
        return moyenne(M)"""
    
"""def aire_superpose(regiment,R):
    air_inutile = 0
    for caserne in regiment:
        for caserne2 in regiment:
            if caserne != caserne2:
                dx = abs(caserne.x - caserne2.x)
                dy = abs(caserne.y - caserne2.y)

                if dx < R and dy < R:
                    air_inutile += R**2 - dx*R - dy*(R-dx)
    return air_inutile/len(regiment)"""

def best_regiment():
    R = (N+1)/n
    meilleur_regiment_de_caserne = [caserne() for i in range(n)]
    meilleur_moyenne_distance_regiment = moyenne_distance_regiment(meilleur_regiment_de_caserne,Ville)
    #meilleur_air_occupe = aire_superpose(meilleur_regiment_de_caserne,R)
    meilleur_distance_moyenne_entre_regiment = distance_moyenne_entre_regiment(meilleur_regiment_de_caserne)
    meilleur_rapport = meilleur_moyenne_distance_regiment/meilleur_moyenne_distance_regiment

    gen = 1000

    for i in range(gen):
        regiment = [caserne() for i in range(n)]
        try:
            moyenne_distance_regiment_ = moyenne_distance_regiment(regiment,Ville)
            distance_moyenne_entre_regiment_ = distance_moyenne_entre_regiment(regiment)
            #aire_superpose_ = aire_superpose(regiment,R)
            rapport = moyenne_distance_regiment_/distance_moyenne_entre_regiment_
            
            if rapport < meilleur_rapport:
                meilleur_rapport = rapport
                meilleur_regiment_de_caserne = regiment
                meilleur_moyenne_distance_regiment = moyenne_distance_regiment_
                #meilleur_air_occupe = aire_superpose_
                meilleur_distance_moyenne_entre_regiment = distance_moyenne_entre_regiment_
            #print(meilleur_rapport,rapport,distance_moyenne_entre_regiment_,moyenne_distance_regiment_)
        except ZeroDivisionError as err:
            pass 
    return meilleur_regiment_de_caserne  




############################################################################

fig, ax = plt.subplots()
densite = [[0 for i in range(N)] for j in range(N)] #ville

for i in range(100):
    regiment = best_regiment()
    print(i)
    for caserne_ in regiment:
        i = caserne_.x
        j = caserne_.y
        densite[i][j] += 1

plt.imshow(densite, extent=[0,N,0,N], aspect="auto")
plt.title("taille " + str(N) + " et " + str(n) + " casernes")
plt.colorbar()
plt.show()


"""for i in range(10):
    print(i)
    for caserne in :
        i = caserne.y
        j = caserne.x
        #Densite[i][j] += 1
    fig, ax = plt.subplots()
    ax.scatter(i, j, edgecolors='none')

plt.show()"""