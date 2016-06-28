#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import search_kicks.core as skcore

sns.set_style("ticks")

kick_t = 16.74
x, t = skcore.build_sine(kick_t, 6.4, [1, 4])

kick_x = x[np.argmin(abs(t-kick_t))]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(t, x)
plt.grid()
plt.xlabel(r"Phase [rad]")
plt.ylabel(r"Distance to the ideal orbit")
#plt.title("Example of a kick in the orbit")

ax.annotate(r'Kick', xy=(kick_t, kick_x), xytext=(11., -.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylim(-1.3, 1.3)
plt.xlim(-0, 6.4*2*np.pi)
sns.despine()

plt.savefig("../img/kick.pdf")
plt.show()
