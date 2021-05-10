#training file
import json
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from chat.model import NeuralNet
from chat.ex import tokenize, stem, bow
with open('chat/CB.json','r') as f:
    intents = json.load(f)

all_words= []
tags = []
xy= []

for intent in intents['intents']:
    tag=intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w=tokenize(pattern)
        all_words.extend(w)
        xy.append((w,tag))

word =['?','!']
all_words = [stem(w) for w in all_words if w not in word]
all_words = sorted(set(all_words))
tags=sorted(set(tags))


x=[]
y=[]

for (pattern_sentence, tag) in xy:
    bag=bow(pattern_sentence, all_words)
    x.append(bag)
    label = tags.index(tag)
    y.append(label) 
x=np.array(x)
y=np.array(y)

class ChatDataset(Dataset):
    def __init__(self): 
        self.n_samples = len(x)
        self.x_data = x
        self.y_data = y

    #dataset[index]
    def __getitem__(self,index):
        return self.x_data[index], self.y_data[index] #returns as tuple
    
    def __len__(self):
        return self.n_samples

#Hyper parameter
batch_size = 8
hidden_size = 8
output_size = len(tags) #number of diff classes or texts
input_size = len(x[0]) #number of length of each bow and bow has the same length as all words array
print(input_size, len(all_words))
print(output_size, tags)

learn_rate = 0.001
num_epochs =1000

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle = True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #if we have GPU support 
model = NeuralNet(input_size, hidden_size, output_size)

#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate) #optimize model

#training loop
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device) #pushing to the device
        labels = labels.long().to(device)

        #forward 
        outputs = model(words) #words as input
        loss = criterion(outputs, labels) 

        #backward and optimizer step
        
        optimizer.zero_grad()#empty gradients first
        loss.backward() #back propogation calc
        optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}') 

print(f'final loss, loss={loss.item():.4f}') 

#save and load model and implementation


data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags":tags
}

FILE="data.pth"
torch.save(data,FILE)
print(f'training complete. file saved to {FILE} ')