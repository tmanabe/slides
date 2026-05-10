#!/usr/bin/env python

import matplotlib.pyplot as plt

import torch

plt.rcParams["font.size"] = 16
plt.figure()

m = torch.linspace(1, 50, 100)
y = 1 / torch.log2(1 + m)

plt.plot(m, y, linewidth=8)
plt.xlabel("Rank")
plt.ylabel("Weight")
plt.ylim(bottom=0)
plt.savefig(__file__.replace(".py", ".png"), bbox_inches="tight")
