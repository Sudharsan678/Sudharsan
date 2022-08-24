
def sorting(array, low, high):

  p = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= p:
  
      i = i + 1


      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = sorting(array, low, high)

   
    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)


data = list(map(int,input().split()))
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array : ')
print(data)