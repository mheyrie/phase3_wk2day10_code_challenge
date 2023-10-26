class Customer:

    customers_list = []

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
        Customer.customers_list.append(self)
    
    def given_name(self):
        return self.firstname
    
    def family_name(self):
        return self.lastname
    
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    

    @classmethod
    def all(cls):
        return cls.customers_list
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
        pass
    
 
    
 

# customer1 = Customer("Mary", "Oladele")
# customer1.firstname = "Sally"
# customer2 = Customer("Isse", "Dalls")
# customer3 = Customer("Mary", "Oladele")
# customers = Customer.all()
# print(customer1.full_name())
# print(customer2.full_name())
# print(customer3.full_name())
# print(Customer.customers_list)
