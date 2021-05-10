#model code
import torch
import torch
import torch.nn as nn #nn is neural network. This lets us use the basic functions of neural network

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1=nn.Linear(input_size, hidden_size) #level1 (number of patterns)
        self.l2=nn.Linear(hidden_size, hidden_size) #level2 (hidden layer)
        self.l3=nn.Linear(hidden_size, num_classes) #level3 (number of classes)
        self.relu = nn.ReLU() #activation function(passing the output of one to another level)

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        #no activation in the end
        return out