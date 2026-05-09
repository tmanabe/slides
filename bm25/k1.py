#!/usr/bin/env python

import matplotlib.pyplot as plt

import torch

plt.rcParams["font.size"] = 36
plt.figure(dpi=50)

x = torch.linspace(0, 7, 141)
y = (1.2 + 1) * x / (1.2 * ((1 - 0.75) + 0.75 * 113 / 1_000) + x)

plt.plot(x, y, linewidth=8)
plt.xlabel("Term Frequency (TF)")
plt.ylabel("Score Contrib.")
plt.savefig(__file__.replace(".py", ".png"), bbox_inches="tight")
