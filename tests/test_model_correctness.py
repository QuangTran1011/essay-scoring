from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Define path to our model
model_path = "./models/model_weighted_training"

def test_model_correctness():
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    essay = """
     People always wish they had the same technology that they have seen in movies, or the best new piece of technology that is all over social media. However, nobody seems to think of the risks that these kinds of new technologies may have. Cars have been around for many decades, and now manufacturers are starting to get on the bandwagon and come up with the new and improved technology that they hope will appeal to everyone. As of right now, it seems as though the negative characteristics of these cars consume the positive idea that these manufacturers have tried to convey.

Currently, this new technology in cars has a very long way to go before being completely "driverless". Drivers still need to be on alert when they are driving, as well as control the car near any accidents or complicated traffic situations. This seems to totally defeat the purpose of the "driverless" car. Eventually the technology may improve, but nobody can be certain that the driverless car will eventually become completely "driverless". This idea just seems like a lot of hard work and money for something that is not very neccessary. If someone does not want to drive their car they can just take a city bus or a subway. There are so many options of transportation that can already solve this problem. Even if masnufacturers are trying to make driving more "fun", driving is not meant to be "fun" it is meant to get people where they need to go. Playing around in a car just to have "fun" is just a recipe for disaster.

The idea of the driverless car also raises many questions about who will be liable when someone gets into an accident in one of these new cars. Many states do not even let people drive semi-automatic cars because there are not even laws that pertain to the liability of anyone who get into an accident while driving these type of cars. If these cars become more popular, states may pass new laws. However, this topic also raises questions about who is able to dictate whether or not it was the car or the human's fault for an accident. Since this technology is so new, there could be many problems with the car's system that nobody has even discovered since they have not drove the car themselves. If someone test drives this kind of car or even purchases one and they get into a crash not knowing what could possibly happen to them, they will want to sue the car manufacturer since they were not aware of any bugs in the car's system. These lawsuits can add up and eventually the manufactuers will be in a bunch of debt, which could cost them their whole idea of the driverless car.

The technology car manufacturers are trying to develope may just be a diasaster in the making. There are many alternative options of transportations if you do not feel like driving yourself, and these options are way less expensive than buying a brand new car. Although this technology is relatively new, we can not be certain that this new idea will even pay off in the end, it may just be a waste of money and time. Sometimes the newest technology is not the most benefical.            
    """

    inputs = tokenizer(essay, return_tensors="pt")
    with torch.no_grad():  
        outputs = model(**inputs)
        predictions = outputs.logits.argmax(dim=-1) + 1  # Add 1 because class is [0->5] while score is [1->6]

    score = predictions.item()
    assert predictions.numpy()[0] == 4
