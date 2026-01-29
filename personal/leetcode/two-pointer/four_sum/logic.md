# Four Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, find all unique quadruplets (four numbers) in the array that add up to the target.

---

# Approach 1: Two Pointer with Nested Loops (Iterative)

## Algorithm
1. **Sort the array**: Start by sorting the array to enable two-pointer technique and easily skip duplicates
2. **First loop (i)**: Iterate through the array, fixing the first number
   - Skip duplicate values to avoid duplicate quadruplets
3. **Second loop (j)**: For each i, iterate to fix the second number
   - Skip duplicates to avoid duplicate quadruplets
4. **Two pointers (l, r)**: Use left and right pointers to find the remaining two numbers
   - Left pointer starts at `j+1`
   - Right pointer starts at `len(nums)-1`
   - Move pointers based on the sum:
     - If sum equals target: add to result, move both pointers, skip duplicates
     - If sum > target: move right pointer left (decrease sum)
     - If sum < target: move left pointer right (increase sum)

## Key Points
- **Sorting**: Enables two-pointer technique and duplicate skipping
- **Duplicate handling**: Skip when `nums[i]==nums[i-1]` and `nums[j]==nums[j-1]` to avoid duplicate results
- **Early termination**: The inner loop condition `i<len(nums)-3` ensures we have at least 4 elements

## Complexity Analysis
- **Time Complexity**: O(n³)
  - Outer loop: O(n)
  - Inner loop: O(n)
  - Two pointers: O(n)
  - Sorting: O(n log n)
- **Space Complexity**: O(1) excluding the output array (only using pointers)

## Example
```
nums = [1, 0, -1, 0, -2, 2]
target = 0

After sorting: [-2, -1, 0, 0, 1, 2]

Quadruplets that sum to 0:
[-2, -1, 1, 2]
[-2, 0, 0, 2]
[-1, 0, 0, 1]
```

---

# Approach 2: Generic k-Sum using Recursion + Backtracking ⭐ (POWERFUL!)

This is a **generic solution that works for k-Sum of any k**, not just 4Sum. It's elegant but requires careful understanding.

## 🧩 Core Idea

> "Fix one number, then recursively solve a smaller sum problem."

```
4Sum → 3Sum → 2Sum (base case with two pointers)
```

---

## Step 0: Initialize

```python
nums.sort()
quad = []       # Current partial combination
res = []        # Final answers
kSum(4, 0, target)  # Find 4 numbers from index 0 that sum to target
```

---

## Step 1: Full Dry-Run with Example

**Input:**
```
nums = [1, 0, -1, 0, -2, 2]
target = 0
```

**After sorting:**
```
nums = [-2, -1, 0, 0, 1, 2]
```

---

## 🔁 LEVEL 1 — k = 4

We iterate: `i` ranges from 0 to 2 (len(nums) - k + 1 = 6 - 4 + 1 = 3)

### ▶️ Iteration 1: i = 0

```
nums[i] = -2
quad = [-2]
Call: kSum(3, 1, 2)
  ↓ "Find 3 numbers starting from index 1 that sum to 2"
```

---

## 🔁 LEVEL 2 — k = 3

Range: `i` from 1 to 3

### ▶️ Iteration 2.1: i = 1

```
nums[i] = -1
quad = [-2, -1]
Call: kSum(2, 2, 3)
  ↓ "Find 2 numbers starting from index 2 that sum to 3"
```

---

## 🔁 LEVEL 3 — k = 2 (BASE CASE - Two Pointers)

```
l = 2 (nums[l] = 0)
r = 5 (nums[r] = 2)
```

**Two-pointer loop:**
```
0 + 2 = 2 < 3  → l++
0 + 2 = 2 < 3  → l++
1 + 2 = 3 == target ✅
```

**Found:** `quad + [1, 2] = [-2, -1, 1, 2]`

Add to `res`. Move pointers: `l++, r--` → loop exits.

**Back to LEVEL 2**

---

### ▶️ Iteration 2.2: i = 2

```
nums[i] = 0
quad = [-2, 0]
Call: kSum(2, 3, 2)
```

**Two-pointer:**
```
l = 3 (0), r = 5 (2)
0 + 2 = 2 == target ✅
```

**Found:** `[-2, 0, 0, 2]`

---

### ▶️ Iteration 2.3: i = 3

```
nums[3] == nums[2] == 0
Skip (duplicate) → continue
```

**Back to LEVEL 1**

---

### ▶️ Iteration 1.2: i = 1

```
nums[i] = -1
quad = [-1]
Call: kSum(3, 2, 1)
```

**LEVEL 2:** i = 2
```
nums[i] = 0
quad = [-1, 0]
Call: kSum(2, 3, 1)
```

**LEVEL 3 - Two pointers:**
```
l = 3 (0), r = 5 (2)
0 + 2 = 2 > 1  → r--
0 + 1 = 1 == target ✅
```

**Found:** `[-1, 0, 0, 1]`

---

### ▶️ Iteration 1.3: i = 2

```
nums[i] = 0
quad = [0]
Call: kSum(3, 3, 0)
```

No valid triples → returns

---

## ✅ Final Result

```
res = [
  [-2, -1, 1, 2],
  [-2, 0, 0, 2],
  [-1, 0, 0, 1]
]
```

---

## 🌳 Recursion Tree Visualization

```
                    kSum(4, 0, 0)
                    /  |  \
                   /   |   \
                  /    |    \
         i=0(-2)/     i=1(-1)  \i=2(0)
               /         |       \
              /          |        \
        kSum(3,1,2)  kSum(3,2,1)  kSum(3,3,0)
           / \          /  \        (empty)
          /   \        /    \
    i=1  /     \ i=2  /      \ i=2
    (-1) /       \ (0)/        \
       /          X          kSum(2,...)
      /            \          (no matches)
   kSum(2,2,3)  kSum(2,3,2)
      |            |
   [1,2]✅      [0,2]✅
    Found      Found
  [-2,-1,1,2] [-2,0,0,2]

        kSum(4,0,0)
             |
        kSum(3,2,1)
             |
        kSum(2,3,1)
             |
          [0,1]✅
           Found
        [-1,0,0,1]
```

---

## 🔑 The Two Critical Lines Explained (VERY IMPORTANT)

```python
quad.append(nums[i])                              # 1. Choose
kSum(k-1, i+1, target-nums[i])                   # 2. Explore
quad.pop()                                        # 3. Un-choose (Backtrack)
```

This is the **standard backtracking pattern**: **Choose → Explore → Un-choose**

### Why these steps?

| Step | What | Why |
|------|------|-----|
| `append(nums[i])` | Add current number to partial solution | Building the path |
| `kSum(...)` | Recursively solve smaller problem | Go deeper down tree |
| `pop()` | Remove the number | Undo the choice so next option can be tried |

### ❌ What if you remove `quad.pop()`?

```
quad = [-2, -1]
next i = 0
quad becomes [-2, -1, 0] ❌ WRONG!
```

The `-1` from the previous branch pollutes the new combination.

---

### Visual Backtracking

**Going DOWN:**
```
quad = []
append -2  → quad = [-2]
append -1  → quad = [-2, -1]
append  1  → quad = [-2, -1, 1]
append  2  → quad = [-2, -1, 1, 2]  ✅ SOLUTION FOUND
```

**Coming BACK UP (backtrack):**
```
pop()  → quad = [-2, -1, 1]
pop()  → quad = [-2, -1]
pop()  → quad = [-2]
Now try next option: [-2, 0, ...]
```

---

## 🧠 One-Sentence Mental Model

> **Recursion explores one choice deeply. Pop() undoes that choice so other options can be tried.**

---

## How it Generalizes to k-Sum

The same algorithm works for **any k**:

```python
def kSum(k, start, target):
    if k == 2:
        # Base case: 2Sum with two pointers
        return two_pointer_logic()
    
    for i in range(start, len(nums) - k + 1):
        if i > start and nums[i] == nums[i-1]:
            continue  # Skip duplicates
        quad.append(nums[i])
        kSum(k-1, i+1, target-nums[i])  # Reduce to (k-1)Sum
        quad.pop()
```

Examples:
- **3Sum**: `kSum(3, 0, target)` → reduces to 2Sum
- **5Sum**: `kSum(5, 0, target)` → reduces to 4Sum → reduces to 3Sum → reduces to 2Sum
- **Any k**: Elegant recursion!

---

## Complexity Analysis

| Metric | Value |
|--------|-------|
| Time Complexity | O(n³) for 4Sum |
| Space Complexity | O(k) for recursion stack depth (k=4, so O(1)) |

---

## Approach 1 vs Approach 2

| Aspect | Iterative (Nested Loops) | Recursive (k-Sum) |
|--------|--------------------------|-------------------|
| Readability | Explicit, easy to follow | Elegant, but harder to visualize |
| Generalization | Only works for 4Sum | Works for any k-Sum |
| Code reusability | Need different code for 3Sum, 5Sum | Single function handles all |
| Performance | Same O(n³) | Same O(n³) |
| When to use | Interview (quick solution) | Show deep understanding |

---

## Key Takeaways

1. **Recursion transforms problems**: 4Sum → 3Sum → 2Sum
2. **Backtracking is crucial**: `append` → `recurse` → `pop`
3. **Base case is two pointers**: Optimal 2Sum solution
4. **Duplicates skipped at every level**: Ensures unique quadruplets
5. **Generalizable to any k**: Powerful pattern!
