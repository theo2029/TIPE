X = 101 #taille de la map
Y = 101 #taille de la map
#░ ▒ ▒ ▓

map = [[0 for i in range(X)] for j in range(Y)] #0 = emplacement batiment
n = 10 #taille quartier

for i in range(X):
    if i%n == 0:
        for j in range(Y):
            map[i][j] = 1

for j in range(Y):
    if j%n == 0:
        for i in range(Y):
            map[i][j] = 1

def affichage_map(map):
    for i in range(len(map)):
        map_aff = ""
        for j in range(len(map[0])):
            if map[i][j] == 1:
                map_aff += "▓"
            if map[i][j] == 0:
                map_aff += "░"
            
        print(map_aff)

print(map)
affichage_map(map)

