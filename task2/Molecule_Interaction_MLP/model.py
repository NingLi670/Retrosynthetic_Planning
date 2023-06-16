from torch import nn
import torch.nn.functional as F

def MLP():
    return nn.Sequential(
    nn.Flatten(),
    nn.Linear(2048, 512), nn.ReLU(),
    nn.Linear(512, 64), nn.ReLU(),
    nn.Linear(64, 1)
)

def Multi_MLP():
    return nn.Sequential(
    nn.Flatten(),
    nn.Linear(2048*3, 2048), nn.ReLU(),
    nn.Linear(2048, 512), nn.ReLU(),
    nn.Linear(512, 64), nn.ReLU(),
    nn.Linear(64, 1)
)

def Interaction_MLP():
    return nn.Sequential(
    nn.Flatten(),
    nn.Linear(2048*6, 2048), nn.ReLU(),
    nn.Linear(2048, 512), nn.ReLU(),
    nn.Linear(512, 64), nn.ReLU(),
    nn.Linear(64, 1)
)
