import time

def quickSort(arr, low, high):
	if low < high:
		swap = low + 1
		pivot = arr[low]

		for i in range(low+1,high):
			if arr[i] <= pivot:
				arr[swap],arr[i] = arr[i],arr[swap]
				swap += 1

		arr[low], arr[swap-1] = arr[swap-1], arr[low]

		print("Updated array: ", arr) # comment this for time testing
		quickSort(arr, low, swap-1)
		quickSort(arr, swap, high)

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
arr = input("Input your dataset: ").split(" ")
for i in range(len(arr)): arr[i] = int(arr[i]) 
start_time = time.time()
quickSort(arr, 0, len(arr))
end_time = time.time()

print(arr)
# print("Execution Time: ", end_time - start_time)