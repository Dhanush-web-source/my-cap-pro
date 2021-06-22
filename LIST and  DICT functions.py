#program to print the list functions in python
mylst=["A.R.rahman","uvanshankarraja","Anirudh"]
print(mylst)
#append function
mylst.append("harrisjayaraj")
print(mylst)
#clear
mylst.clear()
print(mylst)
#copy
mylst=["A.R.rahman","uvanshankarraja","Anirudh"]
myst=mylst.copy()
print(myst)
#count
print(mylst.count(0))
#length
print(len(mylst))
#index
print(mylst[-1])
print(mylst[0:])
#insert
mylst.insert(2,"santhosh")
print(mylst)
#pop
mylst.pop(2)
print(mylst)
#remove
mylst.remove("Anirudh")
print(mylst)
#reverse
mylst.reverse()
print(mylst)
#sort
nums=[20,4,32,1,16]
nums.sort()
print(nums)
#list will allow the duplicates
nums.append(20)
print(nums)
#allows different data types and for loop
mums=[96,99,6.2,"theend"]
for i in mums:
    print(i)
#extend
mylst.extend(nums)
print(mylst)
#while loop
i=0
while i<len(mums):
    print(mums[i])
    i=i+1
#list comprehension
[print(x) for x in mums]
mems=["choclates","candies","lollies"]
germs=[]
for i in mems:
    if "c" in i:
        germs.append(i)
print(germs)
num1=[v for v in range(10)]
print(num1)
num1=[y for y in range(20) if y<15]
print(num1)
#sort in descending
germs.sort(reverse=True)
print(germs)
#JOIN THE TWO LISTS
m1=[1,2,3,4,5]
m2=[6,7,8,9,10]
m=m1+m2
print(m)
print("--------------------------------------------dictionary starts--------------------------------------------")
my_dict={"red":"colour","mango":"fruit","potato":"vegetable"}
print(my_dict)
print(my_dict["red"])
print(len(my_dict))
print(type("color"))
x=my_dict["potato"]
print(x)
print(my_dict.get("red"))
print(my_dict.keys())
my_dict["potato"]="snacks"
print(my_dict)
z=my_dict.values()
print(z)
for i in my_dict:
    print(i)
print(my_dict.values())
n=my_dict.items()
print(n)
my_dict.update({"fruit":"jack"})
print(my_dict)
my_dict.pop("fruit")
print(my_dict)
ndict=my_dict.copy()
print(ndict)
#fromkeys
e={"k1","k2","k3","k4"}
f=0
thisdict = dict.fromkeys(e,f)
print(thisdict)