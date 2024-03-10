rows=int(input("Enter the number of rows: "))
for i in range(rows-1):      
    for j in range(i-1):     # here, we are declaring the for loop to print the pattern  
        print("*", end=' ')    
    print(" ")