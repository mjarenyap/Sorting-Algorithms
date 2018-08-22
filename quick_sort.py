import time

def quickSort(arr, low, high, intermediate_results):
	if low < high:
		swap = low + 1
		pivot = arr[low]

		for i in range(low+1,high):
			if arr[i] <= pivot:
				arr[swap],arr[i] = arr[i],arr[swap]
				swap += 1

		arr[low], arr[swap-1] = arr[swap-1], arr[low]

		print("Updated array: ", arr) # comment this for time testing
		intermediate_results.write("Updated array: " + str(arr) + "\n")

		quickSort(arr, low, swap-1, intermediate_results)
		quickSort(arr, swap, high, intermediate_results)

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
arr = input("Input your dataset: ").split(" ")
for i in range(len(arr)): arr[i] = int(arr[i])
intermediate_results = open("quick_intermediate_results.txt", "w")
intermediate_results.write("Quick Sort Intermediate Results:\n\n")

quickSort(arr, 0, len(arr), intermediate_results)
intermediate_results.write("\nFinal Result: " + str(arr))
print("\nFinal Result:", arr)