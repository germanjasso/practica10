from time import time
from fuerza_bruta import buscador

t0= time()
con= "K1tM"
buscador(con)
t1= time()
t2= round(t1-t0,6)
print("El tiempo de ejecucion fue de{}".format(t2))