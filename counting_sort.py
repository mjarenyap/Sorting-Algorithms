import time
import random

def sort(arr, intermediate_results):
	c = [0] * (max(arr)+1)

	# place each element in arr to the proper indexes
	for i in arr: c[i] += 1
	print("C Array:", c) # comment this for time testing
	intermediate_results.write("C Array: " + str(c) + "\n")

	# add the previous counts
	for i in range(1, len(c)-1):
		c[i+1] = c[i] + c[i+1]
	print("C Array:", c) # comment this for time testing
	intermediate_results.write("C Array: " + str(c) + "\n")

	# make an array with the same length as arr
	b = [-1] * len(arr)
	for i in arr:
		b[c[i] - 1] = i
		c[i] -= 1

	print("B Array (Sorted):", b) # comment this for time testing
	intermediate_results.write("\nB Array (Sorted): " + str(b) + "\n")

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
intermediate_results = open("counting_intermediate_results.txt", "w")
intermediate_results.write("Counting Sort Intermediate Results:\n\n")
intermediate_results.write("Input: " + str(arr) + "\n\n")

print("Input:", arr)
sort(arr, intermediate_results)
