# from class1 import Student 
# s2=Student()
# s2.display("hey")





# class Animal:
#     def __init__(self,name):
#         self.name =name


#     def eat(self):
#         print(self.name, "is eiting")




# ___________________________________________________



# class Father:
#     def __init__(self):
#         print("Father construction")

#     def skills(self):
#         print("Father: driving")


# class mother:
#     def __init__(self):
#         print("mother construction")

#     def hobbies(self):
#         print("mother : cooking")


# class child (Father,mother):
#     def __init__(self):
#         Father.__init__ (self)
#         mother.__init__ (self)
#         print("child construction")

#     def study(self):
#         print("child: studying")




# c=child()
# c.skills()
# c.hobbies()
# c.study()





# ______________________________________________________________




# class grandparent:
#     def __init__(self):
#         print("grandparent construction")

#     def house(self):
#         print("grandparent has a house")


# class parent(grandparent):
#     def __init__(self):
#         super().__init__()
#         print("parent construction")

#     def car(self):
#         print("parent has a car")


# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child construction")

#     def bike(self):
#         print("child has a bike")



# c = child()
# c.house()
# c.car()
# c.bike()




# ____________________________________________________________________



# class animal:
#     def __init__(self ,name):
#         self .name = name
#         print("animal comstruction")

#     def eat(self):
#         print(self.name, "is eating")


# class dog (animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print("dog construction")


#     def bark(self):
#         print(self.name, "is barking")


# class cat(animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print("cat construction")

#     def meow(self):
#         print(self.name, "is meowing")



# d= dog ("tommy")
# d.eat()
# d.bark()
# print()
# c = cat("kitty")
# c.eat()
# c.meow()
    
    
# _____________________________________________________________________


class animal:
    def __init__(self):
        print("animal construction")


    def eat(self):
        print("animal is eating")


class dog(animal):
    def dog_sound (self):
        print("dog says woof")

class cat(animal):
    def cat_sound (self):
        print("cat says meow")


class pet(dog,cat):
    def __init__(self):
        animal.__init__(self)
        print("pet construction")


    def play(self):
        print("pet is playing")


p = pet()
p.eat()
p.dog_sound()
p.cat_sound()
p.play()











