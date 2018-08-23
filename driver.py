import time
import random

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(1, len(arr)):
			prev = j-1
			if(arr[prev] > arr[j]):
				arr[prev], arr[j] = arr[j], arr[prev]

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
	# Initialize
	inputArr = []
	resultsArr = [] # 0 - Bubble, 1 - Counting, 2 - Quicksort
	#start_time = end_time = 0
	for i in range(0, 3):
		resultsArr.append([0, 0, 0])

	numSize = input("Enter the array size: ")

	# Open File to write in sortLog
	file = open("sortLog.txt", "w")
	file.write("Input:\n")

	# Write in file the input file
	printArray(file, inputArr, True, numSize)
	file.write("\n\n")

	# Repeat experiment 3 times
	for i in range(0, 3):

		# Bubble Sort
		tempArr = inputArr.copy()
		start_time = time.time()
		bubbleSort(tempArr)
		end_time = time.time()
		resultsArr[0][i] = end_time*1000 - start_time*1000

		# Counting Sort
		tempArr = inputArr.copy()
		start_time = time.time()
		countingSort(tempArr)
		end_time = time.time()
		resultsArr[1][i] = end_time*1000 - start_time*1000

		# Quickort
		tempArr = inputArr.copy()
		start_time = time.time()
		quickSort(tempArr, 0, len(inputArr))
		end_time = time.time()
		resultsArr[2][i] = end_time*1000 - start_time*1000

		# Display sorted array
		if i == 0:
			file.write("Sorted:\n")
			printArray(file, tempArr, False, numSize)
			file.write("\n\n")

	#print(inputArr)
	sortNames = ["Bubble Sort", "Counting Sort", "Quicksort"]
	# Display execution time
	for i in range(0, 3):
		file.write(sortNames[i] + "\n")
		for j in range(0, 3):
			file.write("Trial " + str(j+1) + ": " + str(resultsArr[i][j]) + " ms\n")
		file.write("\n\n")

	file.close()
	#printArray(file, arr, False, numSize)
	print("Results are recorded in sortLog.txt")

main()
