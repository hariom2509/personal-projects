# class Student:
#     name = "hari"

# s1 =Student()
# print(s1.name)
# class Student:
#     collenge_name = "ABC PS"
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#         print ("adding new student")
    
#     def get_avg(self):
#         sum = 0
#         for value in self.marks:
#             sum+=value
#         print("hi ", self.name, "Your avg marks is: " , sum/3)

#     @staticmethod
#     def hello():
#         print("hello")

# s1 = Student("karan", [52,82,93])
# print(s1.name,s1.marks)
# print(Student.collenge_name)
# s1.get_avg()
# s1.hello()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("car started")

# car1 = Car()
# car1.start()

class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print ("Rs",amount,"was debited")
        print(self.get_balance())

    def credit(self,amount):
        self.balance +- amount
        print ("Rs",amount,"was credited")
        print(self.get_balance())
    
    def get_balance(self):
        return self.balance
        
acc1 = account(10000,12345678)
print (acc1.balance)
print(acc1.account_no)
acc1.credit(100)
acc1.debit(500)

        