import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def f(x):
    return torch.pow((x-2.0),2)

def fP(x):
    return 2*x-4


x.data = torch.tensor([1.1])

value = f(x)
value.backward()
print(value)
print(x.grad)
x.grad.zero_()

