#program to print the most frequent  letters in the words using dict function
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
print(most_frequent("Mississippi"))
