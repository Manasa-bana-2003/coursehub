#for loop

'''a = 'manasa'
for i in a :
    print(i)'''

'''b = 5
for i in range(1,b+1):
    print(i)'''

'''c = 5
count = 1
while count <= c :
    print(count)
    count = count + 1'''



'''n = 5
for i in range(1,n+1):
    print(i * " *")


for i in range(5):
    x=' *'
    x=x*i
    print(f'{x:^10}')'''


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()


a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*", end =" ")
    print()


b=int(input())
for i in range(1,b+1):
    for j in range(i-1,b):
        print("*", end=" ")
    print()
