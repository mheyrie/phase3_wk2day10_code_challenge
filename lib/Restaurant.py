"""
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
  """

from Review import Review
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

    

# restaurant1 = Restaurant("Dominos")
# restaurant1_name = restaurant1.name
# restaurant1.name= "KFC"
# print(restaurant1_name)