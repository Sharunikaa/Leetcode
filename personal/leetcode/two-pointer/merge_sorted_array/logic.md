# 88. Merge Sorted Array - LeetCode Problem

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array **in-place**. The final sorted array should be stored inside `nums1`.

**Important constraints:**
- `nums1` has a length of `m + n`, where:
  - First `m` elements are the actual elements to merge
  - Last `n` elements are set to 0 and should be ignored (these are placeholders for nums2)
- `nums2` has length `n`
- Do NOT return anything; modify `nums1` in-place

**Example 1:**
- Input: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
- Output: `[1,2,2,3,5,6]`
- Explanation: Merge [1,2,3] and [2,5,6] → [1,2,2,3,5,6]

**Example 2:**
- Input: `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
- Output: `[1]`

**Example 3:**
- Input: `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`
- Output: `[1]`

**Constraints:**
- nums1.length == m + n
- nums2.length == n
- 0 ≤ m, n ≤ 200
- 1 ≤ m + n ≤ 200
- -10⁹ ≤ nums1[i], nums2[j] ≤ 10⁹

---

## Approach 1: Backward Two-Pointer (Optimal)

### Step-by-Step Working

1. **Initialize three pointers:**
   - `l = m - 1` (last element of actual nums1 data)
   - `r = n - 1` (last element of nums2)
   - `pos = m + n - 1` (last position in nums1)

2. **Compare from the end and place larger element:**
   - While `r >= 0` (still have elements in nums2):
     - If `l >= 0` AND `nums1[l] > nums2[r]`:
       - Place `nums1[l]` at `nums1[pos]`
       - Decrement `l`
     - Else if `r >= 0` AND `nums2[r]` >= `nums1[l]` (or l < 0):
       - Place `nums2[r]` at `nums1[pos]`
       - Decrement `r`
     - Decrement `pos` (move to next position to fill)

3. **End condition:**
   - When `r < 0`, all of nums2 is merged
   - nums1 original elements are already in place (no need to process remaining)

### Why Backward Works (Key Insight!)

**The crucial insight:** 
- nums1 has extra space at the END
- If we work forward, we'd overwrite elements of nums1 that haven't been processed yet
- By working BACKWARD, we fill the unused space without overwriting anything
- No extra space needed!

### Example Walkthrough
```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Initial state:
nums1: [1, 2, 3, 0, 0, 0]
nums2: [2, 5, 6]
        l=2 r=2 pos=5

Step 1: Compare nums1[2]=3 and nums2[2]=6
  - 3 > 6? No
  - Place nums2[2]=6 at nums1[5]
  - nums1: [1, 2, 3, 0, 0, 6]
  - r=1, pos=4

Step 2: Compare nums1[2]=3 and nums2[1]=5
  - 3 > 5? No
  - Place nums2[1]=5 at nums1[4]
  - nums1: [1, 2, 3, 0, 5, 6]
  - r=0, pos=3

Step 3: Compare nums1[2]=3 and nums2[0]=2
  - 3 > 2? Yes
  - Place nums1[2]=3 at nums1[3]
  - nums1: [1, 2, 3, 3, 5, 6]
  - l=1, pos=2

Step 4: Compare nums1[1]=2 and nums2[0]=2
  - 2 > 2? No
  - Place nums2[0]=2 at nums1[2]
  - nums1: [1, 2, 2, 3, 5, 6]
  - r=-1, pos=1

Exit loop (r < 0)
Result: [1, 2, 2, 3, 5, 6] ✓
```

### Complexity Analysis - Backward Two-Pointer

**Time Complexity: O(m + n)**
- Single pass through both arrays
- Each element processed once

**Space Complexity: O(1)**
- Only using pointers (l, r, pos)
- No extra data structures
- Modifying nums1 in-place ✓

### Code Implementation
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1          # Pointer for nums1
        r = n - 1          # Pointer for nums2
        pos = m + n - 1    # Position to fill in nums1
        
        while r >= 0:  # While nums2 has elements
            if l >= 0 and nums1[l] > nums2[r]:
                nums1[pos] = nums1[l]
                l -= 1
            else:
                nums1[pos] = nums2[r]
                r -= 1
            pos -= 1
```

---

## Approach 2: Forward Two-Pointer with Extra Space

### Step-by-Step Working

1. **Create a temporary array:**
   - `temp = []` to store merged result

2. **Compare from the beginning of both arrays:**
   - Two pointers: `i = 0` (nums1), `j = 0` (nums2)
   - While `i < m` AND `j < n`:
     - Compare and add smaller element to temp
     - Advance corresponding pointer

3. **Add remaining elements:**
   - Add remaining from nums1: `temp += nums1[i:m]`
   - Add remaining from nums2: `temp += nums2[j:n]`

4. **Copy back to nums1:**
   - `nums1[:] = temp` (modify in-place)

### Complexity Analysis - Forward Pointer

**Time Complexity: O(m + n)**
- Two passes: merge + copy back

**Space Complexity: O(m + n)**
- Temporary array needed

### Code Implementation
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        temp += nums1[i:m]
        temp += nums2[j:n]
        
        nums1[:] = temp
```

---

## Approach 3: Using Python's Built-in Sort

### Step-by-Step Working

1. **Copy nums2 into nums1's empty space:**
   - `nums1[m:] = nums2`

2. **Sort the entire array:**
   - `nums1.sort()`

### Complexity Analysis - Built-in Sort

**Time Complexity: O((m+n) log(m+n))**
- Sorting dominates

**Space Complexity: O(1)** or **O(m+n)**
- Depending on Python's sort implementation
- (Timsort uses O(n) worst case)

### Code Implementation
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
```

---

## Comparison of All Approaches

| Aspect | Backward Pointer | Forward Pointer | Built-in Sort |
|--------|------------------|-----------------|----------------|
| **Time** | O(m+n) | O(m+n) | O((m+n)log(m+n)) |
| **Space** | O(1) ✓ | O(m+n) | O(1-n) |
| **Code Length** | 10 lines | 13 lines | 2 lines |
| **In-place** | ✓ Yes | No | ✓ Yes |
| **Readability** | Good | ✓ Clear | Very simple |
| **Interview Ready** | ✓ Best | Good | Not ideal |
| **Efficiency** | ✓ Best | Good | Poor |
| **Clever** | ✓ Yes | Standard | Lazy |

---

## Key Insights

1. **Backward pointer is optimal for this specific problem:**
   - Takes advantage of the extra space at the END of nums1
   - O(m+n) time with O(1) space is unbeatable
   - Shows sophisticated problem-solving

2. **Why not forward pointer?**
   - Forward would overwrite nums1 elements we haven't read yet
   - Requires extra space for temporary array

3. **Why not just sort?**
   - O((m+n)log(m+n)) is slower than O(m+n)
   - Shows you don't understand the problem structure
   - Wastes the fact that both arrays are already sorted

4. **The arrays being sorted is crucial:**
   - Forward pointer works because we can maintain two pointers
   - We never need to look back
   - This is a classic merge operation (like in merge sort)

---

## Edge Cases to Consider

1. **One array is empty:**
   ```
   nums1 = [1], m = 1, nums2 = [], n = 0
   - Output: [1]
   - Just keep nums1 as is
   ```

2. **Other array is empty:**
   ```
   nums1 = [0], m = 0, nums2 = [1], n = 1
   - Output: [1]
   - Just copy nums2 to nums1
   ```

3. **All nums1 elements are smaller:**
   ```
   nums1 = [1,2,3,0,0,0], m = 3, nums2 = [4,5,6], n = 3
   - Output: [1,2,3,4,5,6]
   - nums1 stays in place, nums2 fills the end
   ```

4. **All nums2 elements are smaller:**
   ```
   nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3
   - Output: [1,2,3,4,5,6]
   - nums2 fills from the back, nums1 gets pushed forward
   ```

5. **Negative numbers:**
   ```
   nums1 = [-5,-3,0,0,0], m = 2, nums2 = [-4,-1,2], n = 3
   - Output: [-5,-4,-3,-1,0,2]
   - Works the same with negatives
   ```

6. **Duplicate elements:**
   ```
   nums1 = [1,2,2,0,0,0], m = 3, nums2 = [2,5,6], n = 3
   - Output: [1,2,2,2,5,6]
   - Duplicates are handled correctly
   ```

7. **Single elements:**
   ```
   nums1 = [1,0], m = 1, nums2 = [0], n = 1
   - Output: [0,1]
   - Simple case
   ```

---

## Recommendation

**Use Approach 1 (Backward Two-Pointer)** because:
- **Optimal efficiency:** O(m+n) time, O(1) space
- **Interview favorite:** Shows deep problem understanding
- **Takes advantage of problem structure:** Uses the extra space cleverly
- **Classic algorithm:** Demonstrates mastery of merge operations
- **Production ready:** Best performance for all cases

**Use Approach 2 (Forward Pointer)** when:
- Space is not a constraint
- You want more straightforward code
- Working with immutable data structures

**Use Approach 3 (Built-in Sort)** when:
- You need quick solution and don't care about efficiency
- Arrays are not pre-sorted (makes the trade-off worth it)
- Never in an interview! (Shows lack of problem understanding)

---

## Why This Problem is Interesting

1. **Constraints guide the solution:**
   - The fact that nums1 has extra space is the KEY
   - Backward approach directly leverages this
   - Different constraint = different optimal solution

2. **Demonstrates merge algorithm:**
   - Core operation in merge sort
   - Merging two sorted arrays
   - Two-pointer technique is fundamental

3. **Tests if you understand:**
   - Why the constraints are given
   - How to leverage problem structure
   - Trade-offs between time and space

4. **Classic interview pattern:**
   - Two sorted arrays
   - Merge/combine them efficiently
   - Shows algorithmic thinking

---

## Visual Representation

```
Before merge:
nums1: [1, 2, 3, _, _, _]  (m=3)
nums2: [2, 5, 6]           (n=3)
                l  r  pos=5

Backward process (filling from right):
Step 1: max(3,6)=6 → pos 5
nums1: [1, 2, 3, _, _, 6]
        
Step 2: max(3,5)=5 → pos 4
nums1: [1, 2, 3, _, 5, 6]
        
Step 3: max(3,2)=3 → pos 3
nums1: [1, 2, 3, 3, 5, 6]
        
Step 4: max(2,2)=2 → pos 2
nums1: [1, 2, 2, 3, 5, 6]

✓ Done!
```

---

## Common Mistakes to Avoid

1. **Overwriting nums1 elements:**
   ```python
   # Wrong: Using forward pointer without extra space
   # Overwrites nums1[2] before reading it
   ```

2. **Forgetting to check bounds:**
   ```python
   # Wrong: Don't check if l >= 0
   if nums1[l] > nums2[r]:  # ERROR if l < 0
   
   # Right: Check l >= 0 first
   if l >= 0 and nums1[l] > nums2[r]:
   ```

3. **Using `>=` vs `>`:**
   ```python
   # Fine either way, but be consistent
   # nums2[r] >= nums1[l] works when l < 0 (nums2 is selected)
   ```

4. **Forgetting remaining elements:**
   ```python
   # If nums1 has remaining (l >= 0 when r < 0)
   # They're already in place! No action needed.
   # Only nums2 remainder needs careful handling
   ```

5. **Creating unnecessary space:**
   ```python
   # Don't use temp array when not needed
   # The backward pointer approach is O(1) space!
   ```

---

## Related Problems

- **Merge two sorted linked lists** - Similar logic, different data structure
- **Merge k sorted arrays** - Extension to k arrays
- **Merge sort** - Merge operation is a building block
- **K-way merge** - Generalization of merging multiple sorted sequences

