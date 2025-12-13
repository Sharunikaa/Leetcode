# Swap Diagonals - LeetCode Problem

## Problem Statement
Given an n × n matrix, swap the elements of the main diagonal with the elements of the anti-diagonal (secondary/minor diagonal).

- **Main Diagonal:** Elements at indices `[i][i]`
- **Anti-Diagonal (Minor Diagonal):** Elements at indices `[i][n-1-i]`

**Example:**
- Input: 
  ```
  1 2 3
  4 5 6
  7 8 9
  ```
- Output:
  ```
  3 2 1
  4 5 6
  7 8 9
  ```
- Explanation: Diagonal elements (1,5,9) swapped with (3,5,7)

---

## Key Formula: Minor Diagonal Index

### **`[i][n-1-i]`** ← This is the formula for accessing anti-diagonal elements

Where:
- `i` = row index (0 to n-1)
- `n` = size of the matrix (number of rows/columns)
- `n-1-i` = column index for anti-diagonal

**Why this formula works:**
- When `i=0`: column = `n-1-0` = `n-1` (top-right corner)
- When `i=1`: column = `n-1-1` = `n-2` (one step left and down)
- When `i=n-1`: column = `n-1-(n-1)` = `0` (bottom-left corner)

---

## Approach: Direct Swapping

### Step-by-Step Working

1. **Get matrix size:** `n = len(mat)` (number of rows/columns)

2. **Iterate through all rows:** For `i` from 0 to n-1

3. **Swap diagonal elements:** For each row i, swap:
   - Main diagonal element: `mat[i][i]`
   - Anti-diagonal element: `mat[i][n-1-i]`
   
   Using Python's simultaneous assignment:
   ```
   mat[i][i], mat[i][n-1-i] = mat[i][n-1-i], mat[i][i]
   ```

4. **Return the modified matrix**

### Example Walkthrough

```
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

n = 3

i=0:
  Main diagonal:     mat[0][0] = 1
  Anti-diagonal:     mat[0][3-1-0] = mat[0][2] = 3
  After swap: mat[0] = [3, 2, 1]

i=1:
  Main diagonal:     mat[1][1] = 5
  Anti-diagonal:     mat[1][3-1-1] = mat[1][1] = 5
  After swap: mat[1] = [4, 5, 6] (same, since both are center element)

i=2:
  Main diagonal:     mat[2][2] = 9
  Anti-diagonal:     mat[2][3-1-2] = mat[2][0] = 7
  After swap: mat[2] = [9, 8, 7]

Result:
  [[3, 2, 1],
   [4, 5, 6],
   [9, 8, 7]]
```

### Visual Representation

**Before Swap:**
```
[1]  2  [3]        Main:  1, 5, 9
 4  [5]  6         Anti:  3, 5, 7
[7]  8  [9]
```

**After Swap:**
```
[3]  2  [1]        Main:  3, 5, 7
 4  [5]  6         Anti:  1, 5, 9
[9]  8  [7]
```

---

## Complexity Analysis

### Time Complexity: **O(n)**
- Single loop iterates n times (one per row)
- Each iteration: O(1) swap operation
- Total: **O(n)** where n = number of rows

### Space Complexity: **O(1)**
- Swapping done in-place
- Only using a loop counter variable `i`
- No extra data structures: **O(1)**

---

## Important Notes

1. **In-place modification:** The matrix is modified directly without creating a new matrix

2. **Center element in odd-sized matrices:** 
   - For odd n, when `i = (n-1)/2`, the center element swaps with itself
   - This is harmless and still correct

3. **Anti-diagonal formula:** `[i][n-1-i]` is the crucial insight
   - Memorize this for interview questions on matrix traversals

4. **Why it works:**
   - Each diagonal element has a unique position
   - The formula ensures we pair the correct main and anti-diagonal elements
   - Swapping in a single pass without extra space
