#!/usr/bin/env python

import matplotlib.pyplot as plt

import torch

plt.rcParams["font.size"] = 36
plt.figure(dpi=50)

x = torch.linspace(1, 150_000, 151)
y = torch.log(1_270_000 / x)

plt.plot(x, y, linewidth=8)
plt.xlabel("Document Freq. (DF)")
plt.ylabel("Its Inverse (IDF)")
plt.ylim(bottom=0)
plt.savefig(__file__.replace(".py", ".png"), bbox_inches="tight")
