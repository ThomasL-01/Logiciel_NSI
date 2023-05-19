#ASR2 
#Ex 176
# 1. Les LED ne peuvent pas être de plusieurs couleurs en même temps
# 2/3. Si une LED est déjà acquise, acquerirLED() se bloque donc la LED est bloquée et ne peut pas être acquérit et changer dans une autre couleur
# 4. P1 change la couleur de la LED A et B , P2 B et C et P3 C et A donc on a bien une boucle pour que toutes les LED soient changées

#Ex 177
import threading 

class LED:
    def __init__(self) -> None:
        status = "off"
        couleur = "vert"
A = LED()
B = LED()
C = LED()

def P1():
    A.couleur = "vert"
    print("A changé")
    B.couleur = "vert"
    print("B changé")


#sujet 23
animaux = [ {'nom':'Medor','espece':'chien', 'age':5, 'enclos':2},              
            {'nom':'Titine','espece':'chat',  'age':2, 'enclos':5},
            {'nom':'Tom','espece':'chat',  'age':7, 'enclos':4},
            {'nom':'Belle','espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza','espece':'chat',  'age':6, 'enclos':5}]


def selection_enclos(table_animaux, num_enclos):
    res = []
    for i in range(len(table_animaux)):
        if table_animaux[i]["enclos"] == num_enclos:
            res.append(table_animaux[i])
    return res

#print(selection_enclos(animaux,5))

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    '''Renvoie la valeur de l'intrus situé entre les indices g
    et d dans la liste tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3.'''
    if g == d:
        return f"L'intrus est {tab[d]}"
    else:
        nombre_de_triplets = (d-g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice +1] :
            return trouver_intrus(tab,indice + 3 , d)
        else:
            return trouver_intrus(tab,g , indice)


print(trouver_intrus(tab_c,0,15))

#sujet 43

def ecriture_binaire_entier_positif(n):
    """Fonction qui renvoie l'écriture binaire d'un nombre en base 10 positif"""
    res = []
    while n > 0:
        res.append(n%2)
        n = n//2
    res.reverse()
    return res

print(ecriture_binaire_entier_positif(18))
T  = [7, 9, 4, 3]

def tri_bulles(T):
    '''
    Renvoie le tableau T trié par ordre croissant
    '''
    n = len(T)
    for i in range(...,...,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T