# Question-1

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# student1 = Student("Sakshi", 21)
# student1.display()



# Question-2


# class Food:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show_details(self):
#         print(f"Food: {self.name}")
#         print(f"Price: ₹{self.price}")


# class Order(Food):
#     def __init__(self, name, price, quantity):
#         super().__init__(name, price)
#         self.__quantity = quantity

#     def calculate_bill(self):
#         return self.price * self.__quantity

#     def show_details(self):
#         super().show_details()
#         print(f"Quantity: {self.__quantity}")
#         print(f"Total Bill: ₹{self.calculate_bill()}")


# # Creating objects
# food1 = Order("Pizza", 200, 2)
# food2 = Order("Burger", 100, 3)

# print("=== FOOD DELIVERY APP ===")

# print("\nFirst Order:")
# food1.show_details()

# print("\nSecond Order:")
# food2.show_details()




# Question-3

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance or invalid amount")

#     def show_balance(self):
#         print("Balance:", self.balance)

# account = BankAccount(5000)
# account.deposit(1000)
# account.withdraw(2000)
# account.show_balance()