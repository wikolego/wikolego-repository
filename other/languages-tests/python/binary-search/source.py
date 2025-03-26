import bisect as bs
  
def binary_search(arr, x):
    i = bs.bisect_left(arr, x)
    # print(i)

    if i != len(arr):
        return i
    else:
        return -1
  
  
# Test array
arr = [2, 3, 4, 10, 40]
x = 10
  
# Function call
result = binary_search(arr, x)
  
if result != -1:
    print("res:", str(result))
else:
    print("ERROR")