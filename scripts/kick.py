#!/usr/bin/python

import sys
sys.path.append("/home/olivier/Projets/boulot/search_kicks")

import numpy as np 
import matplotlib.pyplot as plt
import search_kicks.core as skcore

if len(sys.argv) > 1 and str(sys.argv[1]) == "xkcd":
    xkcd = True
else:
    xkcd = False

if not xkcd:
    import seaborn as sns
    sns.set_style("whitegrid")

kick_t = 11.
x, t = skcore.build_sine(kick_t, 6.2, [1, 4])

kick_x = x[np.argmin(abs(t-kick_t))]

if xkcd:
    plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(t, x)
plt.xlabel("Phase [rad]")
plt.ylabel("Distance to the ideal orbit")
#plt.title("Example of a kick in the orbit")

ax.annotate('Kick', xy=(kick_t, kick_x), xytext=(13., -1.),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylim(-1.3, 1.3)
if xkcd:
    plt.savefig("../img/xkcd_kick.pdf")
else:
    plt.savefig("../img/kick.pdf")
plt.show()
