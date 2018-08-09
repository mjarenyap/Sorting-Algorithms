def quickSort(arr, low, high):
	if low < high:
		swap = low + 1
		pivot = arr[low]

		for i in range(low+1,high):
			if arr[i] <= pivot:
				arr[swap],arr[i] = arr[i],arr[swap]
				swap += 1

		arr[low], arr[swap-1] = arr[swap-1], arr[low]
		quickSort(arr, low, swap-1)
		quickSort(arr, swap, high)

arr = input().split(" ")
quickSort(arr, 0, len(arr))
print(arr)