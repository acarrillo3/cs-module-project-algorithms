'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # split 0's into one array and nn-zero into another
    zero_arr = []
    non_zero_arr = []
    for i in range(len(arr)):
        if(arr[i] == 0):
            zero_arr.append(0)
        else:
            non_zero_arr.append(arr[i])
    #merge the arrays
    return non_zero_arr + zero_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")