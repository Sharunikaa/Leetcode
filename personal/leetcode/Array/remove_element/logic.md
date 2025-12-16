# Remove Element - LeetCode Problem

## Problem Statement
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the elements may be changed, and the elements after the required length don't matter.

Return the number of elements in `nums` which are not equal to `val`.

**Important:** You must modify the array in-place with O(1) extra space.

**Example:**
- Input: `nums = [3,2,2,3]`, `val = 3`
- Output: `2`
- Explanation: After removing 3s, nums becomes `[2,2,_,_]`. The first 2 elements are the answer.

**Example:**
- Input: `nums = [0,1,2,2,3,0,4,2]`, `val = 2`
- Output: `5`
- Explanation: After removing 2s, nums becomes `[0,1,3,0,4,_,_,_]`. The first 5 elements are the answer.

---

## Approach 1: Temporary Array (Brute Force)

### Step-by-Step Working

1. **Create a temporary array:** `tmp = []` to store non-value elements

2. **Iterate through original array:**
   - For each number in nums:
   - If number equals val, skip it (continue)
   - Otherwise, append the number to tmp

3. **Copy back to original array:**
   - Iterate through tmp
   - Copy each element back to nums at index i

4. **Return the count:** Return the length of tmp (count of non-value elements)

### Example Walkthrough

```
nums = [0,1,2,2,3,0,4,2], val = 2

Step 1: Create tmp = []

Step 2: Iterate and filter
  - 0 ≠ 2 → tmp = [0]
  - 1 ≠ 2 → tmp = [0,1]
  - 2 = 2 → skip
  - 2 = 2 → skip
  - 3 ≠ 2 → tmp = [0,1,3]
  - 0 ≠ 2 → tmp = [0,1,3,0]
  - 4 ≠ 2 → tmp = [0,1,3,0,4]
  - 2 = 2 → skip

Step 3: Copy back
  - nums[0] = 0 → [0,_,_,_,_,_,_,_]
  - nums[1] = 1 → [0,1,_,_,_,_,_,_]
  - nums[2] = 3 → [0,1,3,_,_,_,_,_]
  - nums[3] = 0 → [0,1,3,0,_,_,_,_]
  - nums[4] = 4 → [0,1,3,0,4,_,_,_]

Step 4: Return len(tmp) = 5
```

### Visual Representation

```
Original:  [0,1,2,2,3,0,4,2]
                ↓ filter out 2s ↓
Filtered:  [0,1,3,0,4]
                ↓ copy back ↓
Modified:  [0,1,3,0,4,_,_,_]
           
Return: 5 (first 5 elements matter)
```

### Complexity Analysis - Brute Force

**Time Complexity: O(n)**
- First pass to filter: O(n)
- Second pass to copy back: O(n)
- Total: **O(n)**

**Space Complexity: O(n)**
- Temporary array stores up to n elements: **O(n)**
- Violates the O(1) space constraint requirement!

---

## Approach 2: Two Pointers (Optimal - In-place)

### Step-by-Step Working

1. **Initialize pointer:** `pointer = 0` (tracks position to place next non-value element)

2. **Iterate through array** with index i from 0 to len(nums)-1:
   - If `nums[i] != val`:
     - Place nums[i] at position pointer: `nums[pointer] = nums[i]`
     - Increment pointer: `pointer += 1`
   - If `nums[i] == val`, do nothing (skip)

3. **Return pointer count:** The pointer value is the count of non-value elements

### Example Walkthrough

```
nums = [0,1,2,2,3,0,4,2], val = 2

Initial: pointer = 0

i=0: nums[0]=0 ≠ 2
  - nums[0] = 0
  - pointer = 1
  - nums = [0,1,2,2,3,0,4,2], pointer=1

i=1: nums[1]=1 ≠ 2
  - nums[1] = 1
  - pointer = 2
  - nums = [0,1,2,2,3,0,4,2], pointer=2

i=2: nums[2]=2 = 2
  - Skip (do nothing)
  - nums = [0,1,2,2,3,0,4,2], pointer=2

i=3: nums[3]=2 = 2
  - Skip (do nothing)
  - nums = [0,1,2,2,3,0,4,2], pointer=2

i=4: nums[4]=3 ≠ 2
  - nums[2] = 3 (place at pointer position)
  - pointer = 3
  - nums = [0,1,3,2,3,0,4,2], pointer=3

i=5: nums[5]=0 ≠ 2
  - nums[3] = 0
  - pointer = 4
  - nums = [0,1,3,0,3,0,4,2], pointer=4

i=6: nums[6]=4 ≠ 2
  - nums[4] = 4
  - pointer = 5
  - nums = [0,1,3,0,4,0,4,2], pointer=5

i=7: nums[7]=2 = 2
  - Skip
  - nums = [0,1,3,0,4,0,4,2], pointer=5

Return pointer = 5
```

### Visual Representation - Two Pointer Technique

```
Initial Array: [0,1,2,2,3,0,4,2]
pointer: 0
i: 0

                    ↓ pointer    ↓ i
Step 1: [0,1,2,2,3,0,4,2]  → nums[0]=0 ≠ 2, pointer++
                    ↓ pointer        ↓ i
Step 2: [0,1,2,2,3,0,4,2]  → nums[1]=1 ≠ 2, pointer++
                        ↓ pointer    ↓ i
Step 3: [0,1,2,2,3,0,4,2]  → nums[2]=2 = 2, skip

(continuing this process...)

                              ↓ pointer
Final: [0,1,3,0,4,_,_,_]  → pointer=5 is the answer
        └─────────┘
        First 5 elements form the result
```

### Why It Works
- `pointer` marks the boundary of processed elements
- Only non-value elements are written to the "processed" region
- After scanning entire array, pointer points past the last valid element
- Elements after pointer don't matter (could be anything)

### Complexity Analysis - Two Pointers

**Time Complexity: O(n)**
- Single pass through the array: **O(n)**

**Space Complexity: O(1)**
- Only using pointer variable, no extra arrays: **O(1)** ✓
- Satisfies the O(1) space constraint!

---

## Comparison of Both Approaches

| Aspect | Brute Force | Two Pointers |
|--------|------------|--------------|
| **Time** | O(n) | O(n) |
| **Space** | O(n) | O(1) |
| **In-place?** | ✗ No | ✓ Yes |
| **Easy to understand?** | ✓ Yes | Moderate |
| **Meets requirements?** | ✗ No | ✓ Yes |
| **Best for** | Learning | Production/Interview |

**Recommendation:** Use **Two Pointers approach** — it's optimal and meets the O(1) space constraint.

---

## Key Insights

1. **Two Pointers Pattern:**
   - Write pointer (slow): tracks position for next valid element
   - Read pointer (fast): scans through array
   - Powerful technique for in-place array modifications

2. **In-place Modification:**
   - Problem requires O(1) space (only temporary variables)
   - Can't use extra arrays for filtering
   - Two pointers solve this elegantly

3. **Order Doesn't Matter:**
   - Elements after pointer position are irrelevant
   - Array doesn't need to be sorted or organized
   - Allows for efficient single-pass solution

4. **Edge Cases Handled:**
   - All elements are val: returns 0
   - No elements are val: returns n (full length)
   - Empty array: returns 0

---

## Code Optimization Tip

Remove debug print statements from production code:

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer
```

The print statements help visualize the algorithm during learning but hurt performance in actual use.
