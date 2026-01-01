#!/usr/bin/env python

# pip install matplotlib

import matplotlib.pyplot as plt

import os
import torch

x = torch.linspace(-6, 6, 241)
y = torch.nn.functional.relu(x)

plt.figure(dpi=600)
plt.plot(x, y, label="Rectified Linear Unit (ReLU)")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.savefig(
    os.path.join(
        os.path.dirname(__file__),
        "relu.png",
    )
)
