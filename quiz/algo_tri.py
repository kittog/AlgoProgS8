# coding : utf-8

# Manipulations :
#    1. faire tourner le code joint, puis
#    2. insérer des compteurs pour pouvoir produire, après chaque calcul:
#       - le nombre de transferts (copie d'une valeur d'une case à  une autre)
#       - le nombre de comparaisons
#    3. déterminer ces valeurs pour 100 essais, et calculer leur moyenne et leur écart-type
#    4. optimiser les algorithmes pour ne faire que les transferts absolument indispensables
#    5. refaire les calculs pour 100 essais alÃ©atoires,
#       et aussi pour l'essai le plus favorable et l'essai le moins favorable

# ----------------------------------------------------------------------
# génération d'une liste d'entiers aléatoires (tous différents)
import random
def genere_liste():
   Min = 1
   Max = 29
   N = 20
   L = random.sample(range(Min, Max), N)
   return L

# champion sur un sous-range
def champion(t,d,f): 
   best = t[d]
   ibest = d
   for i in range(d,f):
      if best > t[i]:
          best = t[i]
          ibest = i
   return best, ibest

# échange de deux valeurs dans une liste t
# (manipulées par leur indices)
def echange(t,i,j):
   prov = t[i]
   t[i] = t[j]
   t[j] = prov

# Un algorithme de tri (tri par sélection)
def tri_selection(t):
   for i in range(len(t)):
      b,ib = champion(t,i,len(t))
      echange(t,i,ib)

# Un algorithme de tri (tri par insertion)
def tri_insertion(l):
   for i in range(len(l)):
      b, ib = champion(l,i,len(l))
      l.insert(i,b)
      l.pop(ib+1)

# ----------------------------------------------------------------------
# Programme principal

def main():
   L = genere_liste()
   print(L)
   tri_insertion(L)
   print(L)


if __name__ == "__main__":
    main()