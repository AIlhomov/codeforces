# def insertionSort(arr, t):
#     n = len(arr)  # Get the length of the array
     
#     if n <= 1:
#         return  # If the array has 0 or 1 element, it is already sorted, so return

#     for i in range(1, n):  # Iterate over the array starting from the second element
#         key = arr[i]  # Store the current element as the key to be inserted in the right position
#         j = i-1
#         while j >= 0 and key > arr[j]:  # Move elements greater than key one position ahead
#             arr[j+1] = arr[j]  # Shift elements to the right
#             j -= 1
#         arr[j+1] = key  # Insert the key in the correct position
 



n, t = map(int, input().split())
queue = input() 

queue_list = list(queue)

while t != 0:
    for i in range(len(queue_list)-1):
        if queue[i] == 'B' and queue[i+1] == 'G':
            #queue.replace(queue[i], queue[i+1])
            queue_list[i] = 'G'
            queue_list[i+1] = 'B'
    queue = ''.join(queue_list)
    t -= 1

print(''.join(queue_list))