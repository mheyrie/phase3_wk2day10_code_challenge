from Customer import Customer
from Restaurant import Restaurant


class Review:

    all_reviews = []

    def __init__(self, customer, restaurant, ratings: int):
        self.customer = customer
        self.restaurant = restaurant
        self.ratings = ratings

        Review.all_reviews.append(self)

    @property
    def rating(self):
        return self.ratings
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant
    
    @classmethod
    def all(cls):
        return cls.all_reviews
    


restaurant1 = Restaurant("Dominos")
customer1 = Customer("Mary", "Oladele")

review1 = Review(customer1, restaurant1, 5)
# print(review1.customer.full_name())
rating1 = review1.rating()
print(rating1)
reviews = Review.all()
for review in reviews:
    print(f"Reviewed by: {review1.customer.full_name()} for {review1.restaurant._name} Restaurant, rating: {review1.rating()}")