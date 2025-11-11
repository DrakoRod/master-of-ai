import torch
from torch.utils.data import Dataset
#from torchvision import transforms
torch.manual_seed(1)

# Define class for dataset
class my_DS(Dataset):
    # Constructor with defult values
    def __init__(self, length = 10, transform = None):
        self.len = length
        self.x = 2 * torch.ones(length, 2)
        self.y = torch.ones(length, 1)
        self.transform = transform
    
    # Getter
    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample
    # Get Length
    def __len__(self):
        return self.len


class add_mult(object):

    # Constructor
    def __init__(self, addx=1, mult=2):
        self.addx = addx
        self.mult = mult
    
    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x + self.addx
        y = y * self.mult
        sample = x, y
        return sample


class mult(object):

    # Constructor
    def __init__(self, mult=2):
        self.mult = mult
    
    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x * self.mult
        y = y * self.mult
        sample = x, y
        return sample
    

class double_DS(Dataset):
     # Constructor with defult values
    def __init__(self, length = 100, transform = None):
        self.len = length
        # self.x = torch.linspace(start=0.0, end=float(length), steps=0.5)
        self.x = torch.linspace(start=0.0, end=100.0, steps=200)
        self.y = 2 * self.x
        self.transform = transform
    
    # Getter
    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample
    # Get Length
    def __len__(self):
        return self.len
    
    
    def __get_y_value():
        pass


if __name__ == "__main__":
    my_datase = double_DS()

    for i in range(len(my_datase)):
        sample = my_datase[i]
        print(i, sample)