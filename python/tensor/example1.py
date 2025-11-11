import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ten1 = torch.zeros(10)

ten2 = torch.ones(10)

ten3 = torch.rand(10)

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]    

B = [
    [1,1],
    [2,2],
   [2,2],
]    


tA = torch.tensor(A)
tB = torch.tensor(B)

print(tA)
print(tB)

def f(x):
    return torch.pow((x-2.0),2)

def fP(x):
    return 2*x-4

x_axis_values = np.linspace(-7,9,100)
y_axis_values = f(torch.tensor(x_axis_values)).numpy()

sns.lineplot(x=x_axis_values, y=y_axis_values, label="$f(x)=(x-2)^2$")

y_axis_vals_p = fP(torch.tensor(x_axis_values)).numpy()

sns.lineplot(x=x_axis_values, y=[0.0]*len(y_axis_values), label="0", color="black")
sns.lineplot(x=x_axis_values, y=y_axis_values, label="Function to Minimize $f(x)=(x-2)^2$", color="blue")
sns.lineplot(x=x_axis_values, y=y_axis_vals_p, label="Gradient of the function  $f\'(x)=2 x - 4$", color="yellow")

plt.title('Sample Bar Plot')
plt.show()