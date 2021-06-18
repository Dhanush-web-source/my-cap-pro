#print the positive numbers from the given list with square brackets and without square brackets
nlist=[12,-31,42,-53,-45]
mlist=[]
for num in nlist:
    if num>0:
        mlist.append(num)
        print(num,end=" ")
print("\n",mlist)