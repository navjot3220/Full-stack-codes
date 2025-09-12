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
data3 = ("nick",20,6.1,(4,6,8))
print(data3)
print(data3[3][1])
print(id(data3))
# mutable id remains same but content or value can be changed and in inmutable id changes 
print(type(data3))
# "type" to check the type of data3
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

data3 = {"name" : "john" , "age" :"30" , 1 : "one" , "marks" : [50 , 70, 60], 6.7: "float" , True: 1}
print(data3)
print(data3["age"])
print(data3.get("age"))
#upper 2 are the ways to get the value
for key in data3:
    print(key)
# in this the "in" is used to find the "key" in "data3"
for i in data3:
    print(i, data3[i])
data3["name"] = "nick"
print(data3)
#to change the current value
data3["gender"] = "male"
print(data3)
#it can also be used to add a new value
data3.pop("age")
data3.popitem()
del data3["marks"]
data3.clear()
print(data3)
#"pop" was used to remove a specific key and "popitem" was used to remove the last key and "del" is used to "delete" the key and its reference in memory too and to clear all we use "clear"
print(len(data3))
#to find length

data4 = dict(name = "fury" , age= 43)
print(data4)
print(type(data4))

data5 = dict(("name" , "cap") , ("age" , 96))
print(data5)

data6 = set()
print(type(data6))
data6 = {"doc",54,64,86}
print(id(data6))
data6.add("jog")
print(id(data6))
#both id is same which means set is muatable
data7=data6
print(id(data7))
#same id ayegi
data8 = data6.copy()
print(data8)
#".copy" to copy a set and get a different id 
data6.remove("jog")
data6.discard("dac")
print(data6)
#both ".remove and .discard" is used for the same perpose but discard will not give any error for example "dac"is a wrong spelling but still no error

data9 ={"name" :"brock" , "age" : 23}
if "age" in data9:
    print("votingg")
else:
    print("not eligible to vote")
# "age" is present in dict if we find "date" then it will show the else statement

print(range(1 , 10))
for i in range(1,11):
    print(i) 

for i in range(3):
    print("hello")
