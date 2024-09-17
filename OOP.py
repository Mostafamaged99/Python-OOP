# class Member:
#     not_allowed = ["spam", "eggs"]
#     member_nums = 0

#     def __init__(self, fname, lname, gender):
#         self.fname = fname
#         self.lname = lname
#         self.gender = gender
#         Member.member_nums += 1

#     @staticmethod
#     def say_hello():
#         print("Hello")

#     @classmethod
#     def get_member_nums(cls):
#         return cls.member_nums

#     def full_name(self):
#         if self.fname in Member.not_allowed or self.lname in Member.not_allowed:
#             raise ValueError("Name not allowed")        
#         else:
#             return f"{self.fname} {self.lname}"
    
#     def full_name_with_title(self):
#         if self.gender == "Male":    
#             return f"Hello Mr {self.full_name()}"
#         if self.gender == "Female":    
#             return f"Hello Miss {self.full_name()}"
        
#     def delete_user(self):
#         Member.member_nums -= 1
#         return f"{self.fname} has been deleted"

#     def all_data(self):
#         return f"{self.full_name_with_title()}, your full name is {self.full_name()}"

# print(Member.say_hello())
# print(Member.get_member_nums())
# member_one = Member("John", "Doe", "Male")
# member_two = Member("Sara", "Doe", "Female")
# member_three = Member("eggs", "Doe", "Female")
# print(Member.get_member_nums())

# # print(member_one.all_data())
# # print(member_two.all_data())
# # print(member_three.all_data())
# print(member_three.delete_user())
# print(Member.get_member_nums())
##########################################################
# class Skills:
#     def __init__(self):
#         self.skills = ["Html", "Css", "Javascript"] 

#     def __str__(self):   
#         return f"My skills are => {self.skills}"
    
#     def __len__(self):
#         return len(self.skills)
    
#     def add_skills(self, skill):
#         self.skills.append(skill)

# omr_skills = Skills()
# print(omr_skills)   
# print(len(omr_skills)) 
# omr_skills.add_skills("Python")
# omr_skills.add_skills("Java")
# print(omr_skills)   
# print(len(omr_skills)) 
# omr_skills.skills.append("C++")  
# print(omr_skills)   
# print(len(omr_skills)) 
##########################################################
# class Food:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"Hello from parent class => name = {self.name}, price = {self.price}"
    
#     def parent_method(self):
#         return "Hello from parent method"

# class Apple(Food):
#     def __init__(self,name,price,amount):
#         super().__init__(name,price)
#         self.amount = amount

#     def __str__(self):
#         return f"Hello from child class => name = {self.name}, price = {self.price}, amount = {self.amount}"
    
# print(Food("Apple",100))
# print(Apple("Apple",100,10))
# food_two = Apple("banana",200,20)
# print(food_two.parent_method())
##########################################################
# class Base:
#     def __init__(self, name):
#         self.name = name

#     def base_method(self):
#         print(f"Base class method => {self.name}")

# class Child_one(Base):
#     def __init__(self, name):
#         super().__init__(name)

#     def child_method(self):
#         print(f"Child class method => {self.name}")

# class Child_two(Child_one):
#     def __init__(self, name):
#         super().__init__(name)

#     def child_two_method(self):
#         print(f"Child_two class method => {self.name}")

# base_two = Child_two("omr")
# base_two.base_method()
#######################################################
# class A:
#     def do_something(self):
#         print("A")
#         raise NotImplementedError("Not yet implemented")

# class B(A):
#     def do_something(self):
#         print("B")

# class C(A):
#     def do_something(self):
#         print("C")

# b = B()
# b.do_something()
# c = C()
# c.do_something()
######################################################
# class Member:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#     def get_name(self):
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
#     @property
#     def get_age(self):
#         return f"{self.age*356} days"

# omr = Member("omr", 25)
# print(omr.get_name())
# omr.set_name("ali")
# print(omr.get_name())
# print(omr.get_age)
####################################################
# from abc import ABCMeta, abstractmethod
# class Programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass
# class Python(Programming):
#     def has_oop(self):
#         return "yes"
# class Pascal(Programming):
#     def has_oop(self):
#         return "no"
#         #pass
    
# python = Python()
# print(python.has_oop())
# pascal = Pascal()
# print(pascal.has_oop())