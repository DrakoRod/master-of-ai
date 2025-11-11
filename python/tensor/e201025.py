#from tqdm.autonotebook import tqdm #Barra de progreso
from tqdm import tqdm
 
 # Utilities
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
import time

#PyTorch
import torch
import torch.nn as nn
import torch.nn.functional as F
from   torch.utils.data import *


import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('png', 'pdf')
 
def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
 
torch.backends.cudnn.deterministic=True
set_seed(42)

def moveTo(obj, device): 
    '''
    obj:    the python object to move to a device, or to move its contents to a device
    device: the compute device to move objects to 
    '''
    if isinstance(obj, list):
        return [moveTo(x, device) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(moveTo(list(obj), device))
    elif isinstance(obj, set):
        return set(moveTo(list(obj), device))
    elif isinstance(obj, dict):
        to_ret = dict()
        for key, value in obj.items():
            to_ret[moveTo(key, device)] = moveTo(value, device)
        return to_ret
    elif hasattr(obj, 'to'):
        return obj.to(device)
    else:
        return obj


if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(device)  # "mps" si disponible, sinon "cpu"
some_tensors = [torch.tensor(1), torch.tensor(2)]
print(some_tensors, '\n')
print(moveTo(some_tensors, device))


# THE TRAINING LOOP
 
def train_simple_network(model, loss_func, training_loader, epochs=20, device="cpu"):
    #We create the optimizer and move the model to the compute device
    #SGD is Stochastic Gradient Decent over the parameters $\Theta$
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
 
    #Place the model on the correct compute resource (CPU or GPU)
    model.to(device)
    #The next two for loops handle the Red steps, iterating through all the data (batches) multiple times (epochs)
    for epoch in tqdm(range(epochs), desc="Epoch", ncols=100):
        model = model.train()#Put our model in training mode
        running_loss = 0.0
 
        #for inputs, labels in tqdm(training_loader, desc="Batch", leave=False):
        for inputs, labels in training_loader:
            #Move the batch of data to the device we are using. this is the last red step
            inputs = moveTo(inputs, device)
            labels = moveTo(labels, device)
 
            #First a yellow step, prepare the optimizer. Most PyTorch code will do this first to make sure everything is in a clean and ready state.
 
            #PyTorch stores gradients in a mutable data structure. So we need to set it to a clean state before we use it. 
            #Otherwise, it will have old information from a previous iteration
            optimizer.zero_grad()
 
            #The next two lines of code perform the two blue steps
            y_hat = model(inputs) #this just computed $f_\theta(\boldsymbol{x_i})$
 
            # Compute loss.
            loss = loss_func(y_hat, labels)
 
            #Now the remaining two yellow steps, compute the gradient and ".step()" the optimizer
            loss.backward()# $\nabla_\Theta$ just got computed by this one call
 
            #Now we just need to update all the parameters
            optimizer.step()# $\Theta_{k+1} = \Theta_k − \eta \cdot \nabla_\Theta \ell(\hat{y}, y)$
 
            #Now we are just grabbing some information we would like to have
            running_loss += loss.item()
 
#Caption: This code defines a simple training loop, which can be used to learn the 
#         parameters $\Theta$ to almost any neural network $f_\Theta(\cdot)$.

X = np.linspace(0, 20, num=200)   #1-dimensional input
y = X                             #1-dimensional output
 
sns.scatterplot(x=X, y=y)

plt.show()

# Adding consistent oscillation up and down
y = X + np.sin(X)*2
sns.scatterplot(x=X, y=y)

plt.show()

# Adding some noise
y = X + np.sin(X)*2 + np.random.normal(size=X.shape)
sns.scatterplot(x=X, y=y)
plt.show()

class Simple1DRegressionDataset(Dataset):
    def __init__(self, X, y):
        super(Simple1DRegressionDataset, self).__init__()
        self.X = X.reshape(-1,1)
        self.y = y.reshape(-1,1)
    def __getitem__(self, index):
        return torch.tensor(self.X[index,:], dtype=torch.float32), torch.tensor(self.y[index], dtype=torch.float32)
 
    def __len__(self):
        return self.X.shape[0]
    
ds=Simple1DRegressionDataset(X, y)

training_loader = DataLoader(Simple1DRegressionDataset(X, y), shuffle=True)

in_features = 1
out_features = 1
model = nn.Linear(in_features, out_features)

loss_func = nn.MSELoss()

# Some statements have already been defined above.
device = torch.device("cpu")
train_simple_network(model, loss_func, training_loader, device=device)

with torch.no_grad():
    Y_pred = model(torch.tensor(X.reshape(-1,1), device=device, dtype=torch.float32)).cpu().numpy()

sns.scatterplot(x=X, y=y, color='blue', label='Data') #The data
sns.lineplot(x=X, y=Y_pred.ravel(), color='red', label='Linear Model') #What our model learned

plt.show()

activation_input = np.linspace(-2, 2, num=200)
tanh_activation = np.tanh(activation_input)
sigmoid_activation = np.exp(activation_input)/(np.exp(activation_input)+1)
sns.lineplot(x=activation_input, y=activation_input, color='black', label="linear")
sns.lineplot(x=activation_input, y=tanh_activation, color='red', label="tanh(x)")
ax = sns.lineplot(x=activation_input, y=sigmoid_activation
                  , color='blue', label="$\sigma(x)$")
ax.set_xlabel('Input value x')
ax.set_ylabel('Activation')