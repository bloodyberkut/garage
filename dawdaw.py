from random import randint, choice


class Customer:
    def __init__(self, lst):
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

    def recommend(self, money, brand):
        selected = [x for x in brand if money >= brand[x]]
        if len(selected):
            print("Sure, with your money, you can buy this models of chosen brand: ", *selected)
        else:
            print("Sorry, you cant buy any model of chosen brand :(")

WatchShop = Shop()
Bob = Customer(WatchShop.brandlst)
WatchShop.recommend(Bob.money, Bob.brand)