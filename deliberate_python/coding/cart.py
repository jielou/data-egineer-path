"""
This example is for understanding function & operator overloading in Python.

Shopping cart class example implements dunder method like __len__...

reference: https://realpython.com/operator-function-overloading/
"""

class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        """len()"""
        return len(self.cart) # must be integer

    def __abs__(self):
        """abs()"""
        return self.__len__()*len(self.customer)

    def __str__(self):
        """str() or print()"""
        return f"this is a order of {self.customer}"

    def __repr__(self):
        """ the parsable string representation of an object

        In cases where the __str__() method is not defined, 
        Python uses the __repr__() method to print the object, 
        as well as to represent the object when str() is called on it.
        
        """
        return f"order {self.cart} for {self.customer}"

    def __bool__(self):
        """obtain the truth value of an object"""
        return len(self.cart) > 0

    def __iadd__(self, other):
        """should make changes directly to the self argument 
        and return the result
        if nothing returned, it would be None.

        When __iadd__() or its friends are missing from your class definition 
        but you still use their operators on your objects, 
        Python uses __add__() and its friends to get the result of the operation 
        and assigns that to the calling instance. 
        """
        self.cart.append(other)
        return self

    def __add__(self, other):
        """ return a new Order instance that has our required changes 
        instead of making the changes directly to our instance """
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __radd__(self, other):
        """works when item is the right operand...reverse speial methods"""
        return self.__add__(other)

    def __getitem__(self, key):
        """key can be interger or string for dictionary"""
        return self.cart[key]

    def __setitem__(self, key, value):
        """key can be interger or string for dictionary"""
        self.cart[key] = value

    def __eq__(self, other):
        return (self.cart == other.cart) and (self.customer==other.customer)

    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == "__main__":
    order = Order(["banana", "apple", "mango"], "Jie")
    print(f"the length of order: {len(order)}")
    print(f"absolute value of order: {abs(order)}")
    print(order)
    print(repr(order))
    print(bool(order))
    new_order = order + "peach"
    print(repr(new_order))
    order += "peach"
    print(repr(order))
    print(f"the first item is: {order[0]}")
    order[0]="water"
    print("after edit the first item", repr(order))
    # also works
    new_order_2 = "ice" + order
    print(repr(new_order_2))
    print(new_order==new_order_2)
    