class Pizza_shop(object) :
    '''class docstring'''
    def __init__(self,customers,min_order,min_price)->None :
        '''function docstring'''
        self._c = customers
        self._mo = min_order
        self._mp = min_price
    def Who_is_eligible(self)->list :
        '''This function takes a dictionary of customers, a minimum number of orders and a minimum order price 
           and Return a list of customers that are eligible for a free pizza.'''
        eligilbles = list()
        c = 0
        for customer in self._c :
            for order in self._c[customer] :
                if order >= self._mp :
                    c+=1
            if c >= self._mo :
                eligilbles.append(customer)
                c = 0
            else :
                c = 0
        return eligilbles
customers_dict = {"Batman": [22, 30, 11, 17, 15, 52, 27, 12],
                  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]}
vals = [(5,20),(3,10),(5,100)]
for order , price in vals :
    minimum_number_of_orders = order
    minimum_order_price = price
    shop = Pizza_shop(customers_dict,minimum_number_of_orders,minimum_order_price)
    print(shop.Who_is_eligible())
exit = input('Enter any key to exit :')
