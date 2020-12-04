
n = 75
M = [[(i,j) for j in range(n)] for i in range(n)]
densite = [[0 for i in range(n)] for j in range(n)] #villeDe0

"Ce sont les espérances du dossier au facteur 4 près, (donc 16 pour la variance)"

def E(n):
    S=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            S+=i+j
    return S/(n**2)

def Ecarre(n):
    S=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            S+=(i+j)**2
    return S/(n**2)

def V(n):
    return Ecarre(n) - E(n)**2
    
def Geo(n): #Teste de la variance trouvée par Geoffrey
    return (n+1)*(2*n+1)/3 - 0.5*(n+1)**2

T=True

"""for i in range(1,1001):
    if not abs(V(i) - Geo(i)) < 10**(-3):
        print(i)
        T = False
print(T) #CETTE FONCTION RETURN TRUE !"""

print(E(100), V(100), V(100)**0.5)