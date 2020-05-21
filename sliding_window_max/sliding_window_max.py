'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # For loop up to k times for the window
    # loop over everything
    maximums = []
    for i in range(len(nums)-k+1):
        max = nums[i]
        for j in range(i, i + k):
            if(j < len(nums) and max < nums[j]):
                max = nums[j]
        maximums.append(max)

    return maximums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
