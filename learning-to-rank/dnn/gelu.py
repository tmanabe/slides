#!/usr/bin/env python

import matplotlib.pyplot as plt

import torch

plt.rcParams["font.size"] = 16
plt.figure()

x = torch.linspace(-4, 4, 161)
y = torch.nn.functional.gelu(x)

plt.plot(x, y, linewidth=8)
plt.xlabel("Input")
plt.ylabel("Gaussian Error Linear Unit (GELU)    ")
plt.savefig(__file__.replace(".py", ".png"), bbox_inches="tight")
