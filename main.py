# avec sys.argv on peut lire la ligne de commande
import sys

# on importe le module de calcul
from fibonacci import fibo

# acquisition du paramètre à partir de la ligne de commande
n = int(sys.argv[1])

# calcul et affichage
print(f"fibo({n}) = {fibo(n)}")
