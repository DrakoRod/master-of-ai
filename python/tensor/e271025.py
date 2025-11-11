import torch
from torch.utils.data import Dataset

class  CustomDataset(Dataset):
    def __init__(self, x, y, transform=None):
        self.x = x
        self.y = y
        self.transform = transform

    def __len__(self):
        return len(self.x)

    def __getitem__(self, i):
        sample = self.x[i]
        label = self.y[i]

        if self.transform:
            sample = self.transform(sample)

        return sample, label


x = torch.tensor(
    [
        [3, 3, 1, 0],
        [3, 3, 1, 1],
        [2, 3, 1, 0],
     ]
    )

y = torch.tensor([0, 0, 1])