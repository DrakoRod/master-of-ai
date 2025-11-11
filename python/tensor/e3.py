import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def f(x):
    return torch.pow((x-2.0),2)

x = torch.tensor([-3.5], requires_grad=True)

print("-----------------------")
print(x)
print("-----------------------")

x_cur = x.clone()
 
# Makes the initial “previous” solution larger so it’s different and the while loop will start
x_prev = x_cur*100
 
epsilon = 1e-5 # Stopping condition threshold for the optimization
eta = 0.2 #  Learning rate
epoch = 0
 
while torch.linalg.norm(x_cur-x_prev) > epsilon:
    x_prev = x_cur.clone()
    value = f(x)
    value.backward()
    x.data -= eta * x.grad
    print(f"Epoch: {epoch}, x_prev = {x_prev.data}, inc = {x.grad*eta}, x_cur = {x.data}")
    x.grad.zero_()
    x_cur = x.data
    epoch += 1
print(x_cur)