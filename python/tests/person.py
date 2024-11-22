class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def call_name(self):
        print(f"Hello, {self.name}!")
        
    def age(self):
        print(f"You are {self.age} years old.")
        
    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

    def get_age_group(self):
        if self.age < 18:
            return "child"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"

bushra = Person("Bushra", 16)
sahil = Person("Sahil", 24)

sahil.introduce()
bushra.introduce()
print(bushra.get_age_group())