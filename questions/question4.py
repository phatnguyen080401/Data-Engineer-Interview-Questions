def missing_number(n, arr):
  return sum(range(n+1)) - sum(arr)

n = int(input("Length of array: "))

arr = []
for i in range(n):
  num = int(input())
  arr.append(num)

print("The missing number is:", missing_number(n, arr))

'''
  Algorithm: calculate the total from 0 to n (include n), then minus the total 
  of current array. It will return a missing value

  Complexity: O(n)
'''