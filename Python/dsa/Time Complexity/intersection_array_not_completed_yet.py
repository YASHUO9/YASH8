array1 = [2,3,10,4,2,9]
array2= [5,3,1,6,2,4,9]

# Bubble sort in Python

def bubbleSort(array2):
    
  # loop to access each array element
  for i in range(len(array2)):

    # loop to compare array elements
    for j in range(0, len(array2) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array2[j] > array2[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array2[j]
        array2[j] = array2[j+1]
        array2[j+1] = temp




bubbleSort(array2)
print(array2)




# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(array1, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if array1[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif array1[mid] > x:
			return binary_search(array1, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(array1, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array


# Function call
result = [binary_search(array2, 0, len(array2)-1, x) for x in array1]

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")






















