import time
import random

def sort(arr, intermediate_results):
	for i in range(len(arr)):
		for j in range(1, len(arr)):
			prev = j-1
			if(arr[prev] > arr[j]):
				arr[prev], arr[j] = arr[j], arr[prev]

			output = "Iteration " +  str(i) +  ": " + str(arr)
			print(output) # comment this for time testing
			intermediate_results.write(output + "\n")

def populate(num_size):
	r = []
	for i in range(num_size):
		r.append(random.randint(1, 100))

	return r

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
# arr = input("Input your dataset: ").split(", ")
num_size = int(input("Size of array: "))
arr = populate(num_size)

for i in range(len(arr)): arr[i] = int(arr[i])
intermediate_results = open("bubble_intermediate_results.txt", "w")
intermediate_results.write("Bubble Sort Intermediate Results:\n\n")
intermediate_results.write("Input: " + str(arr) + "\n\n")

print("Input:", arr)
sort(arr, intermediate_results)

intermediate_results.write("\nFinal result:" + str(arr))
print("\nFinal result:", arr)
