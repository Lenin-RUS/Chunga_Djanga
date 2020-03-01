import numpy as np
import time

def rand():
    print(np.random.normal(1,100,100))
    print(np.random.pareto(1,100))

while True:
    time.sleep(1)
    rand()