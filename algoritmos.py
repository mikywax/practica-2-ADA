import time
import numpy as np
import matplotlib.pyplot as plt

# 1. Bubble Sort (O(n^2))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 2. Mergesort (O(n log n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1; k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1; k += 1
    return arr

# 3. Tree Sort (O(n log n) promedio)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None: return Node(key)
    if key < root.val: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)
    return root

def store_sorted(root, arr, i):
    if root is not None:
        i = store_sorted(root.left, arr, i)
        arr[i] = root.val
        i += 1
        i = store_sorted(root.right, arr, i)
    return i

def tree_sort(arr):
    if not arr: return arr
    root = Node(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])
    store_sorted(root, arr, 0)
    return arr

# 4. Heapsort (O(n log n))
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: largest = l
    if r < n and arr[largest] < arr[r]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# 5. Counting Sort (Exclusivo para Enteros)
def counting_sort(arr):
    if not arr: return arr
    max_val = int(max(arr))
    min_val = int(min(arr))
    range_of_elements = max_val - min_val + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)): count_arr[int(arr[i]) - min_val] += 1
    for i in range(1, len(count_arr)): count_arr[i] += count_arr[i-1]
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[int(arr[i]) - min_val] - 1] = arr[i]
        count_arr[int(arr[i]) - min_val] -= 1
    for i in range(0, len(arr)): arr[i] = output_arr[i]
    return arr
