a = -2
b = -3
print(a/b)
print(a//b)
c = "1001"
print(int(c))
print(bool(2<5))
print(int(-7//2))
print(-3%-2)
print(3//-4) 
d=True
e=False
print(d and e)
print(d or e)
print(d, not e)
name = "prakhar aditya"
print(name[2])
print(name[0:14:3])
#[0:14] means 0th letter to last letter 14th and [:3] means every 3rd letter 
naml = "navjot"
print(naml[:4])
print("Aditya" in name)
# "in" to check if the word exist or not 
print(len(name))
#"len" to check the length of the string
data = ("nick",20,6.1,(4,6,8))
print(data)
print(data[3][1])
print(id(data))
# mutable id remains same but content or value can be changed and in inmutable id changes 
print(type(data))
# "type" to check the type of data
data2 = 1,2,3,4,5 
a,b,c,d,e = data2
print(a,b,c,d,e)
#this method is known as unpacking (assigning variables to every no.)
print(data2.count(3))
#counting that ki 3 kitni baar repeat ho raha hai

list1 = [1,2,3,4,5,6,78.9,True,"Aryan",(6,7,"90"),[3,40]]
print(id(list1))
# print(list1[-1][-1])
list1.append("nick")
#append is used to add something in the list without changing its id 
print(list1)
print(id(list1))
list1.insert(7, 70)
print(list1)
list1[5]=10
print(list1)
#these above 2 are methods to exchange the existing value in the list 
list1.remove(5)
print(list1)
#"remove" to remove a value from list 