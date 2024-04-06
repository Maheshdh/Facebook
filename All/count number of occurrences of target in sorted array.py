arr = [4,8, 8, 8, 8, 16, 23, 23, 42]
target = 42
def findCount(arr,target):
  if not arr:
    return 0
  firstIndex = findTarget(arr,target,True)
  if firstIndex == -1:
    return 0
  secondIndex = findTarget(arr,target,False)

  return secondIndex - firstIndex + 1

def findTarget(arr, target, isFirst):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == target:
      if isFirst:
        if mid == 0 or arr[mid-1] != target:
          return mid
        else:
          high = mid - 1
      else:
        if mid == len(arr) -1 or arr[mid+1] != target:
          return mid
        else:
           low = mid + 1
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

print(findCount(arr,target))

  
