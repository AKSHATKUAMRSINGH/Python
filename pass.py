while True:
    try:
        x=int(input("What's x? "))
    except ValueError:
        pass
    
print(f"x is{x}")