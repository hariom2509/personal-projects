# class student:
#     def __init__(self,name):
#         self.name = name

# s1= student("hari")
# print(s1.name)
# del s1.name
# print(s1.name)


# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def resetpass(self):
#         print(self.__acc_pass) #  __name = "ananya" --> private
    
# acc1 = account("12345", "abcded")

# print (acc1.acc_no)
# print(acc1.resetpass())


# INHERITENCE
# class car:
#     @staticmethod
#     def start():
#         print("car started ....")
#     @staticmethod
#     def stop():
#         print("car stopped ....")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name = name

# class brand(toyotacar):
#     def __init__(self,brand):
#         self.brand = brand


        
# car1=toyotacar("fortuner")
# car2=toyotacar("prius")
# car3=brand("toyota")

# print(car1.name)
# print(car2.name)
# print(car3.brand)
# print(car1.start())
# print(car1.stop())
# print(car3.stop())

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))