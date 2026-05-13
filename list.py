a = ["apple", "mango", "cherry"]
print(a)
print(type(a))

# creating list 
fruits = ["berry", "melon", "apple"]
print(fruits)

#accessing items 
names = ["raghini", "shyam", "anu"]
print(names[0])
print(names[1])

#negative indexing
toys = ["car","bus","bike"]
print(toys[-2])

#range of indexs
toys = ["car", "bus", "bike"]
print(toys[1:2])

#change item value 
toys = ["car", "bus", "bike"]
toys[1] = "doll"
print(toys)

#change a range of items 
toys = ["car","bus","bike"]
toys[1:2]=["hii", "hello"]
print(toys)

#insert items 
toys = ["car", "bus", "bike"]
toys.insert(2,"heyy")
print(toys)

# append items 
names =["raghini", "shyam","anu"]
names.append("bhaskar")
print(names)

# extend 
names = ["raghini","bhaskar","shyam"]
surname = ["priya","vijay"]
names.extend(surname)
print(names)

#remove list
names = ["raghini","bhaskar","shyam"]
names.remove("bhaskar")
print(names)

# delete the list
names=["hii","hello","what"]
del names

#loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  #using list comprehension

  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#join two list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



