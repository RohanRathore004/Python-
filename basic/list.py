# List - List is the data type of python which contains any data types value like int,string,float,bool etc.

l = [12,3,4,5]
print(l)
print(type(l))
print("\n")

# When we check the data type of list  then we get <class list> here list is a object of List class in real list is a class .
# list are ordered collection of data type - 

# We can also get the items of list with for loop - 
for item in l:
    print(item)
# We can also check the index of list - 
print(l[0])
print(l[1])
print(l[2])
print(l[3])

# We can change the value of list - 
l[0] = 45
print(l)

# you can add multiple data type value in the list - 
information = ["Tony","Indore",45,18,True,12,13,14,1544]
print(information)
print(len(information))
# printing the list element with the help of while loop - 
i = 0
while i < len(information):
    print([information[i]])
    i = i + 1

# Note - List is a mutable data type of python. We can change the element of list -
# A list have a negetive indexing as same like string - 
print(information[len(information)-1])
print(information[-3])

# if you want to convert the negative index into the positive index then you have to do this 👇🏼.
print(information[len(information)-3])



if 45 in information:
    print("Yes")

# Same things apply for string as well!
# printing the all value of the information - 
print(information)
print(information[:])

# There is a concept of jump index - 
print(information[1:-1])
print(information[1::2])