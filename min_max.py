import math 
 
# Function implementing the Minimax algorithm 
def minimax(curDepth, nodeIndex, isMaxTurn, scores, targetDepth): 
    """ 
    curDepth: Current depth of the node in the tree 
    nodeIndex: Index of the current node in the scores array 
    isMaxTurn: Boolean flag to determine if it's maximizer's or minimizer's turn 
    scores: List containing values at leaf nodes 
    targetDepth: Total depth of the tree (log2 of number of leaf nodes) 
    """ 
 
    # Base Case: If we reach the target depth, return the node value 
    if curDepth == targetDepth: 
        return scores[nodeIndex] 
 
    # If it's the maximizer's turn, take the maximum of the two child nodes 
    if isMaxTurn: 
        return max( 
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth), 
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth) 
        ) 
 
    # If it's the minimizer's turn, take the minimum of the two child nodes 
    else: 
        return min( 
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth), 
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth) 
        ) 
 
# Take user input for the number of leaf nodes 
n = int(input("Enter the number of leaf nodes (must be a power of 2): ")) 
 
# Validate that the number of leaf nodes is a power of 2 
if math.log2(n) % 1 != 0: 
    print("Error: The number of leaf nodes must be a power of 2.") 
    exit() 
 
# Take user input for the leaf node values 
print(f"Enter {n} values (space-separated):") 
scores = list(map(int, input().split())) 
# Check if the user entered the correct number of values 
if len(scores) != n: 
print(f"Error: You must enter exactly {n} values.") 
exit() 
# Calculate the tree depth 
treeDepth = int(math.log2(n)) 
# Compute and print the optimal value using Minimax 
print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))