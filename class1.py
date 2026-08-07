# a= (1,2,3,"python",5,6)
# print(a[0])

# b=tuple()
# print(type(b))
# print(1 in a)
# print(a.count(3))
# print(a.index (2))
# c= (10,11,12,13)
# print(a+c)







# emptyset=set()
myset={"apple","banana","cherry","Apple"}
# print(myset)
# for i in myset:
#     print(i)
# myset.add("orange")
# print(myset)
# myset.remove ("orange")
# print(myset)

# myset.discard("orange")
# print(myset)
# set1={1,2,3}
# set2={3,4,5}
# print(set1|set2)
# print(set1&set2)
# print(set1-set2)
# print(set1^set2)

# set_a={1,2}
# set_b={1,2,3}
# print(set_a.issubset (set_b))
# print(set_b.issuperset(set_a))



import copy
original_list=[1,2,[3,4]]
# shalow_copied_list=copy.copy(original_list)
# shalow_copied_list[1]=99
# print(original_list)
# print(shalow_copied_list)


# deepcopied=copy.deepcopy(original_list)
# deepcopied[1]=99
# print(deepcopied)
# print(original_list)


# a=3
# b=0
# c=a/b
# print(c)

# try:
#     a=3
#     b=0
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("this will always excute")



class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_details(self):
        print(f"car barnd ={self.brand},car model ={self.model},car year ={self.year}")

# car1=Car("bmw","m4",2000)
# car2=Car("swift","dezire",2001)
# car1.display_details ()
# car2.display_details()


class Student:
    def __init__(self):
        print("first_constructor")
    def __init__(self):
        print("second_constructor")
    def display(self,name):
        print(name)
s1=Student()
s1.display("nova")