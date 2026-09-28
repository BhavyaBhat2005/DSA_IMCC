#write a program to print sum of digits of a given number

num=int(input("Enter a number: "))
sum=0
n=num
while(n>0):
    sum=sum+(num%10)
    n=n//10
print(sum)