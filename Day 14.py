#for loop
fruits=["banana","mango","apple"]
for fruit in fruits:
    print(fruit)

#while loop
i=1
while i<6:
    print(i)
    i+=1

#nested lopps
for i in range(1,4):
    for j in range(1,4):
        print(f"i={i},j={j}")

#iterating over a list
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")

#break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

 #example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
for number in numbers:
    if number == target:
        print("Target found!")
        break

#continue statement
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

#example
#Skipping Even Numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

#the pass statement
for i in range(1, 10):
    if i == 5:
        pass
    print(i)
