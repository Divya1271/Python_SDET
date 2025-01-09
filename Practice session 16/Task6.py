class Appliance:
    def turn_on(self):
        print("Appliances turning on")
class WashingMachine(Appliance):
    def turn_on(self):
        print("Please turn on the washing machine")
class Refridgerator(Appliance):
    def turn_on(self):
        print("Now its refridgerator turning on")
class Microwave(Appliance):
    def turn_on(self):
        print("Microwave is turning on")
Ans=[WashingMachine(),Refridgerator(),Microwave()]
for i in Ans:
    i.turn_on()
