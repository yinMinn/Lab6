class Pet:
   def __init__(self,fur,breed,call):
      self.f = fur
      self.b = breed
      self.c = call
   def eat(self):
      if self.c == 'meow':
        print("The pet is eating fish,",self.c)
      if self.c == 'woof':
        print("The pet is chewing bone,",self.c)
class Cat(Pet):
   def __init__(self,fur,breed):
      Pet.__init__(self,fur,breed,'meow')
class Dog(Pet):
   def __init__(self,fur,breed):
       Pet.__init__(self,fur,breed,'woof')
myKitty = Cat('white','siam')
myKitty.eat()
myLassie = Dog('White','Collar')
myLassie.eat()