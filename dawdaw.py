from random import randint, choice


class Customer:
    def __init__(self):
        self.money = randint(15000, 50000)
        self.brand = choice(lst)
        print("I want to buy ", self.brand, "I have some money: ", self.money, "Can you recommend me smth?")


class Shop:
    def __init__(self):
        self.brand1 = {"model1": 15000, "model2": 20000, "model3": 18000}
        self.brand2 = {"model1": 32000, "model2": 12000, "model3": 19000}
        self.brand3 = {"model1": 38000, "model2": 28000, "model3": 30000}
        self.brand4 = {"model1": 11000, "model2": 29000, "model3": 49000}
        self.brand5 = {"model1": 45000, "model2": 20000, "model3": 43000}
        self.brandlst = [self.brand1, self.brand2, self.brand3, self.brand4, self.brand5]

    def recommend(self):
        pass
