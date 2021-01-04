import time
import random
import math
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from ascii_graph.colordata import hcolor

heads = 0
tails = 0

diff = []
start = time.time()
for y in range(100):
    heads = 0
    tails = 0
    for x in range(100):
        x = random.randint(0,1)
        if x == 0:
            heads = heads + 1
        elif x == 1:
            tails = tails + 1
    
    result = f"Heads: {heads}  Tails: {tails} Diff: {abs(heads - tails)}"
    diff.append(('diff', abs(heads-tails)))
    graph = Pyasciigraph()
for line in graph.graph('Diff', diff):
    print(line)

