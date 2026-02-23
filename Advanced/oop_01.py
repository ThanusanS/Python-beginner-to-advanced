

class car:
  
  def __init__(self,No_of_wheels,No_of_airbage):
     print("Constructor")
     self.__no_of_wheels=No_of_wheels
     self.no_of_airbage=No_of_airbage
     self.mileage=500
  
  

  def move(self,speed):
    print("moving",speed)

  def back(self):
    print("back") 

  def get(self):
     return ("No of wheels:", self.__no_of_wheels)
       



car1=car(4,7) # create object - Instantiation

print(car1.mileage,car1.get(),car1.no_of_airbage)




car2=car(7,9) # create object - Instantiation

print(car2.mileage,car2.get(),car2.no_of_airbage)



class makeJuice:
  def __init__(self,a,b,c):
    self.sugar=a
    self.mangoMl=b
    self.appleMl=7




customer1=makeJuice(5,10,7)    

print(customer1.sugar,customer1.mangoMl,customer1.appleMl) 












class Bank_Account:

    def __init__(self,d,e,f):
        self.customer_name=d
        self.balance=e
        self.account_number=f

    def __delete__(self):
       print("Hello")    
   
    def __str__(self):
       return (self.customer_name)
       





account1=Bank_Account("kamal",2000,1234)

print(account1)



print(account1.customer_name)
print(account1.balance)
print(account1.account_number)




account2=Bank_Account("vimal",3000,4555)



print(account2.customer_name)
print(account2.balance)
print(account2.account_number)




account3=Bank_Account("nimal",5000,3534)



print(account3.customer_name)
print(account3.balance)
print(account3.account_number)

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Dog()
b = Cat()

a.sound()
b.sound()



class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b
MathUtils.add(5, 3)  # 8
                          



























