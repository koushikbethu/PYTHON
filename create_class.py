class Dog: #Deines the class named Dog
  Family="German Shipherd"
  
# Initiaser
  def __init__(self,name,age): #The self Keyword refers to the instance itself
    self.name=name
    self.age=age
  
  def bark(self):
    return f"{self.name} says Woof!"

  def get_age(self):
    return self.age
  
#creating the Objects
dog1=Dog("buddy",3)
dog2=Dog("chinnn",5)

#Accessss

print(dog1.Family) #Output = "German Shepherd"

print(dog1.name)
print(dog1.age)  
