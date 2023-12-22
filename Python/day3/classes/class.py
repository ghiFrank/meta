class myClass:
    a = 5
    def hello(self):
        print("hello")
        pass

newclass = myClass()
print(newclass.a)
newclass.hello()

class House:
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self, rate):
        cost = rate * self.num_rooms
        return cost
    
house = House()
house.num_rooms = 7
print("the house with {} rooms will cost {}".format(house.num_rooms,house.cost_evaluation(5)))
