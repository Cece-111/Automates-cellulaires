from tkinter import *

def initialiseRegles(numRegle) :
    ''' Paramètre : numRegle est un entier compris entre 0 et 255.
    A partir de l'écriture en base 2 de numRegle, listeResultats est
    la liste des 8 résultats correspondant à chaque configuration définie
    dans listeConfigurations.
    initialiseRegles retoune une liste de 8 listes, chacune de longueur 4.
    '''
    listeConfigurations = ['111','110','101','100','011','010','001','000']
    if numRegle == 54 :
        #0b110110
        return [[1,1,1,0], [1,1,0,0], [1,0,1,1], [1,0,0,1], [0,1,1,0], [0,1,0,1], [0,0,1,1], [0,0,0,0]]

    elif numRegle == 90 :
        #0b1011010
        return [[1,1,1,0], [1,1,0,1], [1,0,1,0], [1,0,0,1], [0,1,1,1], [0,1,0,0], [0,0,1,1], [0,0,0,0]]

    elif numRegle == 103 :
        #0b1100111
        return [[1,1,1,0], [1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,0], [0,1,0,1], [0,0,1,1], [0,0,0,1]]

    elif numRegle == 57 :
        #0b111001
        return [[1,1,1,0], [1,1,0,0], [1,0,1,1], [1,0,0,1], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

    else :
        print("numéro de règle non connu")

def afficheRegles(regles):
    '''
    Fonction permettant d'afficher les regles.

    '''
    for elem in regles:
        print(elem)

def etatSuivant(numCellule,tableauCourant,regles):
    '''
    Fonction qui retourne un booléen donnant l’état futur de la cellule.

    '''
    print('numCellule:',numCellule)
    print('tableaucourant:',tableauCourant)
    if numCellule==99:
        l=[tableauCourant[numCellule-1],tableauCourant[numCellule],tableauCourant[0]]
    else:
        l=[tableauCourant[numCellule-1],tableauCourant[numCellule],tableauCourant[numCellule+1]]
    for i in range(9):
        if l==[regles[i][0],regles[i][1],regles[i][2]]:
            return regles[i][3]!=0

def initSimple(position):
    '''
    Fonction qui retourne une liste deNB_CELLULESde booléens 'False' sauf celui d’indice position qui est 'True'.

    '''
    l=[]
    for i in range(position-1):
        l.append(False)
    l.append(True)
    for i in range(NB_CELLULES-position):
        l.append(False)
    return(l)

def generation(noRegle):
    '''
    Fonction qui génère et dessine la colonie surNB_JOURSsuivant la règle 'noRegle'.

    '''
    colonie=initSimple(50)

    for i in range(NB_JOURS):
        dessineColonie(colonie,i)

        temp=[]
        for j in range(NB_CELLULES):
            temp.append(etatSuivant(j,colonie,regles))
        colonie=temp

#-------------------------------------------------------------
#
#   NE RIEN MODIFIER CI-DESSOUS SAUF LE NUMERO DE LA REGLE
#
#-------------------------------------------------------------

# Marge autour du Canevas
MARGE   = 10

# Largeur d'une Cellule
COTE    = 5

# Dimensions de la grille
NB_CELLULES  = 100
NB_JOURS  = 100

# Dimensions du Canevas
LARGEUR = 2*MARGE + NB_CELLULES*COTE
HAUTEUR = 2*MARGE + NB_JOURS*COTE

def dessineCarre(colonie,numGen,numCel):
   x = MARGE + numCel*COTE
   y = MARGE + numGen*COTE
   if colonie[numCel]:
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE,fill="blue")
   else:
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE)

def dessineColonie(colonie,numGen):
    for i in range(len(colonie)):
        dessineCarre(colonie,numGen,i)

# Numéro à choisir parmi les suivants : 54, 57, 90, 103
numeroRegle = 103


regles = initialiseRegles(numeroRegle)
afficheRegles(regles)

fenetre = Tk()
fenetre.title("Automate cellulaire 1D")
zoneDessin = Canvas(fenetre,width=LARGEUR,height=HAUTEUR)
zoneDessin.pack(side=TOP)

generation(numeroRegle)
fenetre.mainloop()











