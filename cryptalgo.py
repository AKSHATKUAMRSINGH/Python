def removeZeroes(a):
    return a.lstrip('0') or '0'  

# Function to convert character string to digit string
def charToDigit(a, digits):
    return ''.join(digits[ord(c) - ord('a')] for c in a)  # Convert characters to corresponding digits

# Function to find sum of numbers in the form of strings
def findSum(a, b):
    if len(a) > len(b):
        a, b = b, a  # Ensure 'a' is the shorter string
    
    str_res = []  # List to store the result
    carry = 0  # Carry for addition

    # Add digits from the rightmost end of both numbers
    for i in range(len(a)):
        sum_digit = int(a[-1 - i]) + int(b[-1 - i]) + carry  # Sum corresponding digits and carry
        str_res.append(str(sum_digit % 10))  # Store the last digit of the sum
        carry = sum_digit // 10  # Update carry

    # Process remaining digits of the longer number
    for i in range(len(a), len(b)):
        sum_digit = int(b[-1 - i]) + carry  # Add remaining digits and carry
        str_res.append(str(sum_digit % 10))
        carry = sum_digit // 10

    if carry:
        str_res.append(str(carry))  # Append the final carry if present
    
    return removeZeroes(''.join(reversed(str_res)))  # Reverse and return the sum string

# Function to check if the puzzle is solved
def isSolved(a, b, sum, digits):
    x = charToDigit(a, digits)  # Convert first word to digits
    y = charToDigit(b, digits)  # Convert second word to digits
    z = charToDigit(sum, digits)  # Convert sum word to digits
    
    res = findSum(x, y)  # Compute sum of first two numbers
    z = removeZeroes(z)  # Remove leading zeroes from expected sum
    
    return z == res  # Check if computed sum matches expected sum

# Function to solve Cryptarithmetic Puzzle using backtracking
def cryptarithmeticSolver(ind, digits, characters, a, b, sum):
    if ind == 26:  # If all characters are assigned
        return isSolved(a, b, sum, digits)  # Check if solution is correct
    
    if digits[ind] != '+':  # If the character is already assigned, move to the next
        return cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum)
    
    # Try assigning digits only for characters that haven't been assigned yet
    for i in range(10):
        if characters[i] == 0:  # Check if digit is available
            characters[i] = 1  # Mark digit as used
            digits[ind] = str(i)  # Assign digit to character
            if cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum):
                return True  # If solution found, return True
            digits[ind] = '+'  # Backtrack and unassign digit
            characters[i] = 0  # Mark digit as unused
    
    return False  # Return False if no valid assignment found

# Function to solve Cryptarithmetic Puzzle
def solvePuzzle(a, b, sum):
    digits = ['-' for _ in range(26)]  # Array to store assigned digits for each character
    characters = [0] * 10  # Array to mark used digits (0-9)
    
    for c in a + b + sum:
        digits[ord(c) - ord('a')] = '+'  # Mark characters that need digit assignment
    
    if cryptarithmeticSolver(0, digits, characters, a, b, sum):  # Start solving from first character
        x = charToDigit(a, digits)  # Get numeric representation of first word
        y = charToDigit(b, digits)  # Get numeric representation of second word
        res = charToDigit(sum, digits)  # Get numeric representation of sum word
        return [x, y, res]  # Return solved values
    else:
        return ["-1"]  # Return -1 if no solution exists

# Taking user input
a = input("Enter the first word: ").lower()  # Get first word from user
b = input("Enter the second word: ").lower()  # Get second word from user
sum = input("Enter the result word: ").lower()  # Get sum word from user

# Solve the puzzle
ans = solvePuzzle(a, b, sum)
print(" ".join(ans))  # Print the solved values
