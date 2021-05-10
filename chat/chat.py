import random
import json
import torch

from chat.model import NeuralNet
from chat.ex import bow,tokenize

def load_chatbot():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #if we have GPU support 

    with open('chat/CB.json','r') as f:
        intents = json.load(f)

    FILE="chat/data.pth"
    data = torch.load(FILE)
    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]


    model = NeuralNet(input_size, hidden_size, output_size)
    model.load_state_dict(model_state)
    model.eval()
    return model, all_words, tags, intents

CHATBOT_MODEL, CHATBOT_ALL_WORDS, CHATBOT_TAGS, CHATBOT_INTENTS=load_chatbot()

def chatbot_output(user_response, model, all_words, tags, intents):
    sentence = tokenize(user_response)
    ab = bow(sentence, all_words)
    ab = ab.reshape(1, ab.shape[0])
    ab = torch.from_numpy(ab) #as bow returns numpy array
    output = model(ab) #gives us the prediction
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    #softmax
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() >0.725:
        #check if tag present in the intents and print that response
        for intent in intents["intents"]:
            if tag==intent["tag"]:
                return f"{random.choice(intent['responses'])}"

    else:
        return "I do not understand."
# while True:
#     sentence = input('You: ')
#     if sentence == "quit":
#         print("Have a nice day, byeeee")
#         break
    
#     sentence = tokenize(sentence)
#     ab = bow(sentence, all_words)
#     ab = ab.reshape(1, ab.shape[0])
#     ab = torch.from_numpy(ab) #as bow returns numpy array
#     output = model(ab) #gives us the prediction
#     _, predicted = torch.max(output, dim=1)
#     tag = tags[predicted.item()]

#     #softmax
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]

#     if prob.item() >0.725:
#         #check if tag present in the intents and print that response
#         for intent in intents["intents"]:
#             if tag==intent["tag"]:
#                 print(f"{bot_name}:{random.choice(intent['responses'])}")

#     else:
#         print(f"{bot_name}: I do not understand.")