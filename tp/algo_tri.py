# coding : utf-8

# Manipulations :
#    1. faire tourner le code joint, puis
#    2. insérer des compteurs pour pouvoir produire, après chaque calcul:
#       - le nombre de transferts (copie d'une valeur d'une case à  une autre)
#       - le nombre de comparaisons
#    3. déterminer ces valeurs pour 100 essais, et calculer leur moyenne et leur écart-type
#    4. optimiser les algorithmes pour ne faire que les transferts absolument indispensables
#    5. refaire les calculs pour 100 essais aléatoires,
#       et aussi pour l'essai le plus favorable et l'essai le moins favorable

# ----------------------------------------------------------------------
# génération d'une liste d'entiers aléatoires (tous différents)
import random
import numpy as np

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
   c = 0 # compteur comparaison
   for i in range(d,f):
      if best > t[i]:
         best = t[i]
         ibest = i
         c += 1
   #print(c)
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
   # c = 0 # compteur transferts
   a = np.array(l)
   for i in range(len(a)):
      c = 0
      b, ib = champion(a,i,len(a))
      a[i], a[ib] = b, a[i] 
      #l.insert(i,b)
      #l.pop(ib+1)
      #c += len(l[ib+1:])
      #print(f'c = {c}')
      #print(l)

def tri_insertion_bis(l):
   a = np.array(l)
   c = 0    # transferts
   for i in range(len(a)):
      x = a[i] # stock élément
      j = i # stock index
      print(f'boucle for a: {a}')
      while j > 0 and a[j-1] > x:
         # on décrémente j de 1
         a[j] = a[j-1]
         c += 1
         j -= 1
         print(a)
      a[j] = x
      c += 2
   print(c)
   return a

# l.pop(index) := return index-ième élément de la liste l, et le retire de la liste
# l.insert(index, b) := insertion élément b à l'index

def tri_bulles(l):
   for i in range(len(l)):
      for j in range(len(l) - 1, i, -1):
         if l[j-1] > l[j]:
            (l[j], l[j-1]) = (l[j-1], l[j])

# ----------------------------------------------------------------------
# Programme principal

def main():
   L = genere_liste() # génération liste d'entiers
   print(L)
   tri_insertion(L) # tri de la liste
   print(L)


if __name__ == "__main__":
    main()