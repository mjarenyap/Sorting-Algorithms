import time

def sort(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

		# print("Iteration", i, ":", arr) # comment this for time testing

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
# arr = input().split(" ")
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)): arr[i] = int(arr[i])
start_time = time.time()
sort(arr)
end_time = time.time()

print(arr)
print("Execution Time: ", end_time - start_time)