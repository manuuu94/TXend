##array manipulation

def maxSum_contArray(array):
    print(array)
    max_sum_current = max_sum_all = array[0]

    for n in array[1:]:
        #print(n)
        max_sum_current = max(n, max_sum_current+n)
        max_sum_all = max(max_sum_all,max_sum_current)
    return print(f"The max sum of a contigous subarray is: {max_sum_all}")


array = [-2,1,-3,4,-1,2,1,-5,4]
maxSum_contArray(array)

'''
Problem 1: Array Manipulation
Description: Given an array of integers, implement a 
function to find the maximum sum of a contiguous subarray. 
You can use Kadane’s algorithm.
Requirements:
  Input: An array of integers
  Output: Maximum sum of contiguous subarray
  Example: 
   	Input: `[-2,1,-3,4,-1,2,1,-5,4]`
  	Output: `6` (subarray: `[4,-1,2,1]`)
'''