# Question-1  (student information)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# student1 = Student("Sakshi", 21)
# student1.display()



# Question-2  (food order)


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




# Question-3  (bankaccount)

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





# Question-4  (Library Management System)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.issued = False

#     def issue_book(self):
#         if not self.issued:
#             self.issued = True
#             print(self.title, "issued successfully")
#         else:
#             print("Book is already issued")

# book1 = Book("Python Basics", "Amit")
# book1.issue_book()
# book1.issue_book()




# Question-5  (Hospital Management System)

# class Patient:
#     def __init__(self, name, disease):
#         self.name = name
#         self.disease = disease

#     def display(self):
#         print("Patient:", self.name)
#         print("Problem:", self.disease)

# p1 = Patient("Aman", "Fever")
# p1.display()




# Question-6   (Online Shopping System)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show_product(self):
#         print("Product:", self.name)
#         print("Price:", self.price)

#     def discount(self, percent):
#         self.price -= self.price * percent / 100
#         print("Final Price:", self.price)

# p1 = Product("Shoes", 2000)
# p1.show_product()
# p1.discount(10)



# Question - 7

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

atm = ATM(5000)
atm.check_balance()
atm.withdraw(1000)
atm.check_balance()