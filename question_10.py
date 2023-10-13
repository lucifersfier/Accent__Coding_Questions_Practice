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
##############################


'''Enter integer n
Count number of 1s in binary code of all numbers from 1 to n
Sort array 1 to n according to the number of 1s in their binary code
Print the number of elements in subarray with maximum number of elements in ascending order
'''
def count_ones_in_binary(num):
    # Count the number of 1s in the binary representation of a number.
    count = 0
    while num > 0:
        count += num % 2
        num //= 2
    return count

# Step 1: Input integer n
n = int(input("Enter integer n: "))

# Step 2: Calculate counts of 1s in binary representation and store in a list
counts = [count_ones_in_binary(i) for i in range(1, n + 1)]

# Step 3: Sort numbers based on the counts of 1s
sorted_numbers = sorted(range(1, n + 1), key=lambda x: counts[x - 1])

# Step 4: Find the subarray with the maximum number of elements in ascending order
max_length = 0
current_length = 1
max_subarray_start = 0
current_subarray_start = 0

for i in range(1, n):
    if counts[sorted_numbers[i] - 1] == counts[sorted_numbers[i - 1] - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            max_subarray_start = current_subarray_start
        current_length = 1
        current_subarray_start = i

# Check if the last subarray is the longest
if current_length > max_length:
    max_length = current_length
    max_subarray_start = current_subarray_start

# Step 5: Print the count of elements in the subarray with the maximum number of elements
max_subarray = sorted_numbers[max_subarray_start:max_subarray_start + max_length]
print("Number of elements in the subarray with the maximum number of elements:", max_length)
print("Elements in the subarray:", max_subarray)

#that's it for now will continue later 
