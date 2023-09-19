#you are given an array of size n your task is to find the length of the longest subsequence such that 
#each element in that subsequence is triple as of the previous element

def longestTripleSubsequence(arr):
    n = int(input())
    if n == 0:
        return 0

    # Initialize an array to store the length of the longest subsequence ending at each index.
    # Initialize it with 1, as the minimum subsequence length is always 1.
    dp = [1] * n

    # Traverse the array from left to right and update the dp array.
    for i in range(1, n):
        for j in range(i):
            if arr[i] == 3 * arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum value in the dp array, which represents the length of the longest subsequence.
    max_length = max(dp)
    
    return max_length

# Example usage:
arr = [2,3,6,18,54]
result = longestTripleSubsequence(arr)
print("Length of the longest subsequence:", result)
