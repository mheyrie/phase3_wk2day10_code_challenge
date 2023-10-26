"""
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
  """

#from Review import Review
from Customer import Customer


class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews = []
        

    @property
    def name(self): 
        return self._name
    
    def reviews(self):
        return self.reviews
    
    def review_addition(self, value):
        return self.reviews.append(value)
  
    def customers():
        return Customer.customers_list
    

restaurant1 = Restaurant("Dominos")
restaurant1_name = restaurant1.name

print(restaurant1_name)