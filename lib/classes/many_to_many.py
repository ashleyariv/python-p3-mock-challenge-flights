class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.bookings_list = []
        self.flights_list = []
        
    def bookings(self):
        return self.bookings_list
    
    def flights(self):
        return self.flights_list

    def num_cheap_bookings(self):
        pass

    def has_booked_flight(self, flight):
        pass

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,first_name):
        if type(first_name) == str and 1 <= len(first_name) <= 25:
            self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,last_name):
        if type(last_name) == str and 1 <= len(last_name) <= 25:
            self._last_name = last_name

class Flight:
    def __init__(self, airline):
        self.airline = airline
        self.bookings_list = []
        self.customers_list = []
        
    def bookings(self):
        return self.bookings_list
    
    def customers(self):
        return self.customers_list

    def average_price(self):
        pass

    @property
    def airline(self):
        return self._airline
    @airline.setter
    def airline(self, airline):
        if type(airline) == str and len(airline) >= 1:
            self._airline = airline

    @classmethod
    def top_two_expensive_flights(cls):
        pass

class Booking:    
    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price

        self.flight.bookings_list.append(self)
        self.customer.bookings_list.append(self)

        if not(customer in self.flight.customers_list):
            self.flight.customers_list.append(customer)
        if not(flight in self.customer.flights_list):
            self.customer.flights_list.append(flight)

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            print('Error')
        elif type(price) == int and 500 <= price <= 3000:
            self._price = price

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if type(customer) == Customer:
            self._customer = customer

    @property
    def flight(self):
        return self._flight
    @flight.setter
    def flight(self, flight):
        if type(flight) == Flight:
            self._flight = flight 