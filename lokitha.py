n=int(input("Enter number of elements: "))
even=0
odd=0
for i in range(n):
    c=int(input())
    if c%2==0:
        even=even+c
    else:
        odd=odd+c
print("sum of even numbers :",even)
print("sum of odd numbers: odd", odd)