import torch
from torch.utils.data import Dataset, DataLoader

class ACDataset(Dataset):
    def __init__(self, data, label):
        self.X, self.y = torch.from_numpy(data).float(), label.flatten()
        self.len = self.y.shape[0]

    def __getitem__(self, index):
        X, y = self.X[index], self.y[index]
        return X, y

    def __len__(self):
        return self.len

def get_data_loader(batch_size, data, label, shuffle):
    dataset = ACDataset(data, label)
    data_loader = DataLoader(dataset, batch_size, shuffle)

    return data_loader