import time
import random

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
	if low < high:
		swap = low + 1
		pivot = arr[low]

		for i in range(low+1,high):
			if arr[i] <= pivot:
				arr[swap],arr[i] = arr[i],arr[swap]
				swap += 1

		arr[low], arr[swap-1] = arr[swap-1], arr[low]

		# print(arr) # comment this for time testing
		quickSort(arr, low, swap-1)
		quickSort(arr, swap, high)

def countingSort(arr):
	c = [0] * (max(arr)+1)

	# place each element in arr to the proper indexes
	for i in arr: c[i] += 1
	# print("C Array:", c) # comment this for time testing

	# add the previous counts
	for i in range(1, len(c)-1):
		c[i+1] = c[i] + c[i+1]
	# print("C Array:", c) # comment this for time testing

	# make an array with the same length as arr
	b = [-1] * len(arr)
	for i in arr:
		b[c[i] - 1] = i
		c[i] -= 1

def printArray(file, arr, isRandom, numSize):
	file.write("[")
	for i in range(0, int(numSize)):
		if isRandom:
			arr.append(random.randint(1, 100000))
		file.write(str(arr[i]))
		if i != int(numSize)-1:
			file.write(", ")
	file.write("]")

def main():
	typeSort = input("Enter what type of sort (1 - Bubble Sort, 2 - Quick Sort, 3 - Counting Sort): ")
	numSize = input("Enter the array size: ")
	arr = []
	start_time = end_time = 0

	file = open("sortLog.txt", "w")
	file.write("Input:\n")

	printArray(file, arr, True, numSize)

	file.write("\n\n")

	if typeSort == str(1):
		file.write("Bubble Sort - Sorted:\n")
		start_time = time.time()
		bubbleSort(arr)
		end_time = time.time()
	elif typeSort == str(2):
		file.write("Quick Sort - Sorted:\n")
		start_time = time.time()
		quickSort(arr, 0, len(arr))
		end_time = time.time()
	elif typeSort == str(3):
		file.write("Counting Sort - Sorted:\n")
		start_time = time.time()
		countingSort(arr)
		end_time = time.time()
		
	printArray(file, arr, False, numSize)
	file.write("\n\n")
	file.write("Execution Time:" + str(end_time - start_time))
	print("Results are recorded in sortLog.txt")
main()