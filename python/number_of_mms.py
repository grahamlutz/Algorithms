"""
How many times must you pick to guarantee you've picked all colors of M&M's?

Constraints:

1) There are n colors of M&M's
2) There is an equal number of each M&M
3) We don't know the total number of M&M's
"""

import matplotlib.pylab as plt
import numpy as np

def run(n):
    """
    n: number of different M&M's
    return: number of picks it took to get all 10
    """
    totalpicks = 0
    picked = set()
    while True:
        # check if we have enough
        if len(picked) == n:
            break
        # pick an M&M
        currentpick = np.random.randint(0, n)  # choose a M&M, randomly 1/n
        totalpicks += 1
        picked.add(currentpick)

    return totalpicks

def run_sequence(n, trials):
    for y in range(1, n+1):
        totalpicks = 0

        for x in range(1, trials):
            totalpicks += run(y)

        print(totalpicks / float(trials))
        plt.ion()
        plt.figure("M&M's Picked")
        plt.plot(y,(totalpicks / float(trials)), marker='o', ms = 10, alpha=1, color='b')

    plt.show("M&M's Picked")

if __name__ == '__main__':
    run_sequence(10, 1000)