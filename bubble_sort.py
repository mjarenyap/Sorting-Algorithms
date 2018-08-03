def sort(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
arr = input().split(" ")
for i in range(len(arr)): arr[i] = int(arr[i]) 
sort(arr)
print(arr)