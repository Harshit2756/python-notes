

## Heapq - Priority Queue

Gives the smallest element efficiently (min-heap).
time complexity: O(log n) for push/pop, O(n) for heapify. 

### Import:

`import heapq`  
Note: Creates MIN-HEAP (smallest at top)

### Functions:

```python
heap = []
heapq.heappush(heap, 3)         # Push: heap = [3]
heapq.heappush(heap, 1)         # Push: heap = [1, 3]
heapq.heappush(heap, 2)         # Push: heap = [1, 2, 3]
heapq.heappop(heap)             # Pop smallest: returns 1, heap = [2, 3]
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)              # Convert to heap: arr = [1, 1, 4, 3, 5]
heapq.heappushpop(heap, 0)      # Push 0 then pop: returns 0
heapq.heapreplace(heap, 5)      # Pop then push 5: returns 2
heap[0]                         # Get smallest: 3 (without removing)
heapq.nlargest(3, [1,2,3,4,5])   # 3 largest: [5, 4, 3]
heapq.nsmallest(2, [3,1,4,1,5])  # 2 smallest: [1, 1]
```

### Max-Heap Trick:
- Nagate values while pushing/popping to simulate max-heap.

```python
max_heap = []
heapq.heappush(max_heap, -10)   # Push negated: [-10]
heapq.heappush(max_heap, -5)    # Push negated: [-10, -5]
max_val = -heapq.heappop(max_heap)  # Pop and negate: returns 10
```

### When to Use:

-   Priority queue
-   K largest/smallest elements
-   Merge K sorted lists
-   Dijkstra's algorithm

---

## Bisect - Binary Search

### Import:

`import bisect`  
Note: arr must be sorted!

### Functions:

```python
arr = [1, 3, 3, 3, 5, 7]
bisect.bisect_left(arr, 3)      # Leftmost position: 1
bisect.bisect_left(arr, 4)      # Position to insert 4: 4
bisect.bisect_right(arr, 3)     # Rightmost position: 4
bisect.bisect(arr, 3)           # Same as bisect_right: 4
arr = [1, 3, 5]
bisect.insort_left(arr, 2)      # Insert at leftmost: [1, 2, 3, 5]
bisect.insort_right(arr, 3)     # Insert at rightmost: [1, 2, 3, 3, 5]
bisect.insort(arr, 4)           # Same as insort_right: [1, 2, 3, 3, 4, 5]
```

### When to Use:

-   Binary search
-   Maintain sorted list
-   Find insertion position
-   Range queries