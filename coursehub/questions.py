#for loop

'''a = 'manasa'
for i in a :
    print(i)

b = 5
for i in range(1,b+1):
    print(i)


#while loop
c = 5
count = 1
while count <= c :
    print(count)
    count = count + 1



n = 5
for i in range(1,n+1):
    print(i * " *")


for i in range(5):
    x=' *'
    x=x*i
    print(f'{x:^10}')


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
#Write a program that prints the first 10 natural numbers using a loop.
c=10
for i in range(1,c+1):
    print(i)

#Calculate the sum of the first 10 natural numbers
d=10
total_sum=0
for i in range(1,d+1):
    total_sum += i
print("Sum: ", total_sum)

#Print a multiplication table for a given number
e=int(input())
for i in range(1,11):
    a=e*i
    print(f"{e} X {i} = {a}")

#Print all even numbers from 1 to 20
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)

#Reverse a given string
a=str(input())
rev=""
for name in a:
    rev=name+rev
print(rev)

#Calculate the factorial of a given number
f=int(input())
fact=1
for i in range(1,f+1):
    fact=fact*i
print(fact)

#Count the number of vowels in a given string
g=str(input())
h=['a','e','i','o','u']
count=0
for char in g:
    if char.lower() in h:
        count+=1
print(count)

#Print the elements of a list
i = 5
count = 1
while count <= i :
    print(count)
    count = count + 1

#Find the largest element in a list
k=[10,99,50,60,70,80]
larg_num = k[0]
l = len(k)
for i in range(1,l):
    if k[i] > larg_num :
        larg_num = k[i]
print(larg_num)

#functions

def numbers(a,b):
    return a+b
c = 3
d = 2
res = numbers(c,d)
print(res)

e = 5
f = 10
res = numbers(e,f)
print(res)


#to add two numbers using functions
def add_two_numbers(a, b):
    return a+b
result=add_two_numbers(2,3)
print(result)'''

#fibonacci series
'''def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def fib(n):
    series=[]
    for i in range(n):
        series.append(fibonacci(i))
    return series
print(fib(10))'''

#palindrome or not
'''def palindrome(s):
    return s==s[::-1]
print(palindrome("mom"))'''

#factorial of a number
'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))'''

#prime number or not
'''def find_max(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

print(find_max([1, 2, 3, 9, 5]))'''









