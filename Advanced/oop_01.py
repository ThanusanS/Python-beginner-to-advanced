

class car:
  
  no_of_wheels=0
  no_of_airbage=0
  mileage=0.0

  def move(self):
    print("moving")

  def back(self):
    print("back") 



car1=car()  # create object - Instantiation

print(car1.no_of_wheels)
print(car1.mileage)




car2=car()

car2.mileage=33

print(car2.mileage)





car3=car()

car3.move()


