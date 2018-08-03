def sort(arr):
	c = [0] * (max(arr)+1)

	# place each element in arr to the proper indexes
	for i in arr: c[i] += 1

	# add the previous counts
	for i in range(1, len(c)-1):
		c[i+1] = c[i] + c[i+1]

	# make an array with the same length as arr
	b = [-1] * len(arr)
	for i in arr:
		b[c[i] - 1] = i
		c[i] -= 1

	print(b)

# main
# sample input: [64, 34, 25, 12, 22, 11, 90]
arr = input().split(" ")
for i in range(len(arr)): arr[i] = int(arr[i]) 
sort(arr)