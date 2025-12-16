# Majority Element - LeetCode Problem

## Problem Statement
Given an array `nums` of size n, return the **majority element**.

The **majority element** is the element that appears more than ⌊n/2⌋ times. You may assume that the majority element always exists in the array.

**Example:**
- Input: `nums = [3,2,3]`
- Output: `3`
- Explanation: 3 appears 2 times, which is > 3/2 = 1.5

**Example:**
- Input: `nums = [2,2,1,1,1,2,2]`
- Output: `2`
- Explanation: 2 appears 4 times, which is > 7/2 = 3.5

**Constraint:** The majority element appears more than ⌊n/2⌋ times, so it's always present.

---

## Approach 1: Counting with Dictionary

### Key Insight
**Count frequency of each unique element and find the one with maximum count.**

### Step-by-Step Working

1. **Create empty dictionary:** `d = {}` to store element frequencies
2. **Initialize max count:** `m = 0` to track the highest frequency

3. **Count frequencies:**
   - For each unique element in nums (using `set(nums)`):
   - Count its occurrences: `c = nums.count(i)`
   - Store in dictionary: `d[i] = c`
   - Update max count: `m = max(m, c)`

4. **Find majority element:**
   - Iterate through dictionary items
   - Return the element whose count equals the maximum count

### Example Walkthrough

```
nums = [2,2,1,1,1,2,2]

Step 1: Create d = {}, m = 0

Step 2: Get unique elements
  set(nums) = {1, 2}

Step 3: Count frequencies
  Element 1:
    - nums.count(1) = 3
    - d[1] = 3
    - m = max(0, 3) = 3
  
  Element 2:
    - nums.count(2) = 4
    - d[2] = 4
    - m = max(3, 4) = 4

Final: d = {1: 3, 2: 4}, m = 4

Step 4: Find majority
  Iterate through d.items():
    - (1, 3): 3 ≠ 4, continue
    - (2, 4): 4 = 4, return 2

Return: 2
```

### Complexity Analysis - Counting

**Time Complexity: O(n²)**
- Creating set: O(n)
- For each unique element (up to n):
  - Calling nums.count(i): O(n)
- Total: **O(n²)** (can be slow for large arrays)

**Space Complexity: O(n)**
- Dictionary stores up to n unique elements: **O(n)**

---

## Approach 2: Sorting

### Key Insight
**After sorting, the majority element is guaranteed to be at the middle position!**

Why? If an element appears more than n/2 times, it must occupy the position at n//2 after sorting.

For example:
- n=7, majority must appear > 3.5 times (at least 4 times)
- After sorting, position 3 (n//2) will definitely contain the majority element

### Step-by-Step Working

1. **Sort the array:** `nums.sort()`

2. **Return middle element:** `return nums[len(nums)//2]`

### Example Walkthrough

```
nums = [2,2,1,1,1,2,2]

Step 1: Sort
  sorted: [1,1,1,2,2,2,2]

Step 2: Get middle element
  len(nums) = 7
  len(nums)//2 = 3
  nums[3] = 2

Return: 2
```

### Visual Explanation

```
Before sort: [2,2,1,1,1,2,2]
After sort:  [1,1,1,2,2,2,2]
             0 1 2 3 4 5 6
                   ↑ index 3 (n//2)
                   Returns: 2 (majority element)
```

**Why this works:**
- Majority element appears > n/2 times
- After sorting, it occupies at least positions from n//2 onwards
- Position n//2 is guaranteed to be the majority element

### Complexity Analysis - Sorting

**Time Complexity: O(n log n)**
- Sorting the array: **O(n log n)**

**Space Complexity: O(1)** (or O(n) depending on sorting algorithm)
- Sorting in-place (varies by implementation)

---

## Approach 3: Boyer-Moore Voting Algorithm (Most Optimal)

### Key Insight
**Track a candidate element and a count. The majority element survives with positive count.**

This is the most efficient approach but not in the provided files. For reference:

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
```

**Time:** O(n) | **Space:** O(1)

---

## Comparison of All Approaches

| Aspect | Counting | Sorting | Boyer-Moore |
|--------|----------|---------|-------------|
| **Time** | O(n²) | O(n log n) | O(n) |
| **Space** | O(n) | O(1) | O(1) |
| **Easy to understand?** | ✓ Yes | ✓ Yes | Moderate |
| **Modifies array?** | ✗ No | ✓ Yes | ✗ No |
| **Best for** | Learning | Quick coding | Optimal solution |

**Recommendation for interviews:**
1. **Best:** Boyer-Moore (O(n) time, O(1) space) - Shows deep understanding
2. **Good:** Sorting (O(n log n), elegant insight) - Quick and clean
3. **Basic:** Counting (O(n²), straightforward) - Simple but inefficient

---

## Key Insights

1. **Majority element properties:**
   - Appears more than n/2 times (guaranteed)
   - At least one must exist
   - Only one majority element possible

2. **Sorting insight is clever:**
   - Mathematical guarantee that n//2 position has majority element
   - Works because of majority property (>n/2)
   - Trades time complexity for simplicity

3. **Boyer-Moore is optimal:**
   - Takes advantage of majority property
   - Vote cancellation: majority votes beat all other votes combined
   - Linear time with minimal space

4. **Edge cases:**
   - Single element array → that element is majority
   - All same elements → that element is majority
   - Half+1 times → still majority (e.g., [1,2] has 1 appearing once, which is >1)

---

## Why Each Approach Works

### Counting Method
Simply counts every element and returns the one with highest count. Straightforward but inefficient due to repeated `.count()` calls.

### Sorting Method
Exploits the mathematical property that if an element appears >n/2 times, it must be at the center of sorted array. Very elegant.

### Boyer-Moore Method
Uses cancellation principle: each vote from majority is paired with votes from minority. Since majority >n/2, majority votes always win in the end.
