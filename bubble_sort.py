import time

def sort(arr, intermediate_results):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

		output = "Iteration " +  str(i) +  ": " + str(arr)
		print(output) # comment this for time testing
		intermediate_results.write(output + "\n")

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
arr = input("Input your dataset: ").split(" ")
for i in range(len(arr)): arr[i] = int(arr[i])
intermediate_results = open("bubble_intermediate_results.txt", "w")
intermediate_results.write("Bubble Sort Intermediate Results:\n\n")
sort(arr, intermediate_results)

intermediate_results.write("\nFinal result:" + str(arr))
print("\nFinal result:", arr)
