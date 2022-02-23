def find_median(arr1, arr2):
  arr3 = []
  m = len(arr1)
  n = len(arr2)
  idx1 = idx2 = 0

  while idx1 < m and idx2 < n:
    if arr1[idx1] <= arr2[idx2]:
      arr3.append(arr1[idx1])
      idx1 += 1
    else:
      arr3.append(arr2[idx2])
      idx2 += 1
  
  if idx1 < m:
    arr3 += arr1[idx1:]
  else:
    arr3 += arr2[idx2:]

  k = m + n
  if k % 2 == 0:
    return (arr3[k//2] + arr3[k//2 - 1]) / 2
  else:
    return arr3[k//2]

arr1 = [9,10,11]
arr2 = [1,4,5,6]

print("The median of two sorted arrays:", find_median(arr1, arr2))

'''
  Algorithm: Create 2 varibles 'idx1' and 'idx2' corresponding to the index of 2 arrays 
  with value 0. Then merge 2 sorted arrays with a while loop. If total length of 2 arrays
  is even, sum 2 values in the middle of merged arrays and divide to 2. If odd, return the
  middle of merged array.

  Complexity: O(m+n)
'''