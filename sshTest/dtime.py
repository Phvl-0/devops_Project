Class Animal:
    def __init__(self,name_param,specie_param):
        self.name = name_param
        self.specie = specie_param

    def intro(self):
        print(f"Hello! My name is {self.name} and I am a {self.specie}")

    def sound(self):
        print(f"{self.name} the {self.specie} makes a sound.")



print("==================Creating Dogs========================")
dogA = Animal("Cheryl","Pug")
dogB = Animal("Tilly", "Golden Rietriver")
dogC = Animal("Bullet", "Poodle")

print("\n ====================Dog Intro==============================")
dogA.intro()
dogA.sound()
dogC.intro()
dogC.sound()
dogB.intro()
dogB.sound()