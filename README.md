# `git add` ligne à ligne

## survol

dans ce repo vous allez trouver, on va appeler ça la 'v0', un petit programme en deux fichiers

* `main.py`
* `fibonnacci.py`

ensuite on va vous donner (en clair dans ce README) le code de ces deux mêmes fichiers dans ce qu'on va appeler la 'v2'  
et 'v2' parce qu'entre la v0 et la v2 on a fait en fait 2 modifications dans la logique du programme

et du coup votre mission ça va être de faire 2 commits séparés, qui correspondent à l'enchainement de ces deux modifications  
(par opposition à une approche dite de *force brute* qui consisterait à tout entasser dans un seul commit)

## le code de départ

vous pouvez exécuter le code comme ceci

```
python main.py 30
```

ouvrez ces deux fichiers et prenez le temps de les lire; que pouvez-vous en dire ?

***
***
***

* la fonction `fibo()` est écrite de manière totalement sous-optimale, sa complexité est en $O(2^n)$
* on utilise `sys.argv` pour faire l'acquisition lire la ligne de commande  
  c'est comme ça qu'on peut trouver le `30` qui est tapé dans le terminal pour le passer à la fonction `fibo()`

## les deux modifications

ce qu'on a fait dans la v2, c'est la somme de deux choses

* `v1`: dans `fibonacci.py`, on a renommé la fonction `fibo()` en `fibo_cached()`,
  et on a modifié son implémentation (par un simple caching) pour rendre l'algorithme linéaire  
  le changement du nom de fonction a du coup rendu certains changements nécéssaires dans `main.py` également (dans la vraie vie on aurait certainement conservé le même nom, justement pour éviter ça, mais là dans cet exercice on fait exprés de changer le nom)
* `v2`: à ce stade, on a changé la méthode d'acquisition du paramètre depuis la ligne de commande; au lieu d'utiliser `sys.argv` qui est simple mais très limité, on passe par [le module `argparse`](https://docs.python.org/3/howto/argparse.html) qui permet par exemple d'ajouter des options

## à vous de jouer

je vous donne en annexe le code correspondant à la v2; à vous de produire deux commits correspondants à la `v1` et à la `v2` respectivement

n'oubliez pas les bonnes pratiques à propos de la rédaction des messages des commits

### indice

vous allez voir qu'à un moment vous allez avoir besoin d'ajouter dans l'index (qui on le rappelle s'appelle aussi le *stage*) seulement certaines lignes, et pas tout un un fichier d'un coup

pour cela vous avez deux options abordables

* vs-code
* sourcetree

## pour vérifier

pour vérifier que tout est OK vous devez pouvoir
exécuter le programme avec toutes les 3 versions

aprés vous être assuré de ne plus avoir de différence pendante (cf `git status`), vous devez pouvoir faire par exemple

```
# la v2, le code doit pouvoir tourner
$ python main.py 40
fibo_cached(50) = 102334155


# remettre la v1 dans les fichiers
$ git restore --source=HEAD~ -- main.py fibonacci.py

# le code doit toujours tourner
$ python main.py 40
fibo_cached(50) = 102334155


# remettre la v0 dans les fichiers
$ git restore --source=HEAD~2 -- main.py fibonacci.py

# le code doit encore tourner
# mais jusque 30 max.
$ python main.py 30
fibo(30) = 832040
```

## pour les rapides

pour ceux qui ont fini avant les autres:

faites une v3, qui permet de choisir sur la ligne de commande entre les deux versions de fibonacci

```
$ python main.py 30
fibo(30) = 832040
$ python main.py --cached 40
fibo_cached(40) = 102334155
```

***
***
***

## annexe: le code de la `v2`

***
`main.py` en `v2`
***

```python
# avec argparse aussi on peut lire la ligne de commande
# et c'est beaucoup plus puissant
from argparse import ArgumentParser

# on importe le module de calcul
from fibonacci import fibo_cached

# acquisition du paramètre à partir de la ligne de commande
parser = ArgumentParser()
parser.add_argument('n', type=int)
args = parser.parse_args()
n = args.n

# calcul et affichage
print(f"fibo_cached({n}) = {fibo_cached(n)}")
```

***
`fibonacci.py` en `v2`
***

```python
"""
la suite de fibonacci
"""

# on optimise

from functools import cache

@cache
def fibo_cached(n):
    """
    en cachant les résultats on arrive
    à une complexité linéaire
    """
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)
```

## pour vérifier

vous trouverez un repo organisé comme celui qu'on vous demande de créer à cette adresse

<https://github.com/ue12-p23/git-tp-add-by-lines-reference>
