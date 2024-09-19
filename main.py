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