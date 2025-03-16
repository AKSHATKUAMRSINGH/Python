# Python3 program to demonstrate  
# working of Alpha-Beta Pruning with user input 
 
# Initial values of Alpha and Beta  
MAX, MIN = 1000, -1000 
 
# Function to implement Minimax algorithm with Alpha-Beta Pruning 
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta): 
    # Base case: if we reach a leaf node 
    if depth == 3: 
        return values[nodeIndex] 
 
    if maximizingPlayer: 
        best = MIN  # Initialize best value for maximizer 
 
        # Recur for left and right children 
        for i in range(0, 2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta) 
            best = max(best, val)  # Choose the maximum value 
            alpha = max(alpha, best)  # Update alpha 
 
            # Alpha Beta Pruning 
            if beta <= alpha: 
                break 
         
        return best 
    else: 
        best = MAX  # Initialize best value for minimizer 
 
        # Recur for left and right children 
        for i in range(0, 2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta) 
            best = min(best, val)  # Choose the minimum value 
            beta = min(beta, best)  # Update beta 
 
            # Alpha Beta Pruning 
            if beta <= alpha: 
                break 
         
        return best 
 
# Driver Code 
if __name__ == "__main__": 
    # Taking user input for leaf node values 
    print("Enter 8 values (space-separated) for leaf nodes:") 
    values = list(map(int, input().split()))  # Read input values from user 
     
    if len(values) != 8: 
        print("Error: You must enter exactly 8 values.") 
    else: 
        # Call the minimax function and print the optimal value 
        print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))