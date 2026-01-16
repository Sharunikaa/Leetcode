# 1768. Merge Strings Alternately - LeetCode Problem

## Problem Statement
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternately, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Example 1:**
- Input: `word1 = "abc"`, `word2 = "pqr"`
- Output: `"apbqcr"`
- Explanation: Merge alternately: a+p+b+q+c+r

**Example 2:**
- Input: `word1 = "ab"`, `word2 = "pqrs"`
- Output: `"apbqrs"`
- Explanation: Merge alternately then append: a+p+b+q, then rs from word2

**Example 3:**
- Input: `word1 = "abcd"`, `word2 = "pq"`
- Output: `"apbqcd"`
- Explanation: Merge alternately then append: a+p+b+q, then cd from word1

**Constraints:**
- 1 ≤ word1.length, word2.length ≤ 10⁴
- word1 and word2 consist of lowercase English letters

---

## Approach 1: Two-Pointer with Manual Concatenation

### Step-by-Step Working

1. **Initialize result and pointers:**
   - `res = ""` (result string)
   - `p = 0` (pointer for word1)
   - `q = 0` (pointer for word2)

2. **Merge while both strings have characters:**
   - While `p < len(word1)` AND `q < len(word2)`:
     - Add character from word1: `res += word1[p]`
     - Add character from word2: `res += word2[q]`
     - Move both pointers forward

3. **Append remaining characters:**
   - If word1 is longer: append `word1[p:]`
   - Else if word2 is longer: append `word2[q:]`

4. **Return the merged result**

### Example Walkthrough
```
word1 = "abc", word2 = "pqr"

Step 1: p=0, q=0
  - res += 'a' → res = "a"
  - res += 'p' → res = "ap"
  - p=1, q=1

Step 2: p=1, q=1
  - res += 'b' → res = "apb"
  - res += 'q' → res = "apbq"
  - p=2, q=2

Step 3: p=2, q=2
  - res += 'c' → res = "apbqc"
  - res += 'r' → res = "apbqcr"
  - p=3, q=3

Step 4: p >= len(word1), exit loop
  - No remaining characters
  - Result: "apbqcr" ✓
```

```
word1 = "ab", word2 = "pqrs"

Step 1: p=0, q=0
  - res += 'a' → res = "a"
  - res += 'p' → res = "ap"
  - p=1, q=1

Step 2: p=1, q=1
  - res += 'b' → res = "apb"
  - res += 'q' → res = "apbq"
  - p=2, q=2

Step 3: p >= len(word1), exit loop
  - word2 is longer: len(word2)=4 > len(word1)=2
  - Append word2[2:] = "rs"
  - res = "apbq" + "rs" = "apbqrs" ✓
```

### Why It Works

1. **Two pointers naturally track positions:** p and q independently advance
2. **Alternating addition:** We add from word1 then word2 in each iteration
3. **Remaining characters handled:** Slicing automatically gets leftover characters
4. **Clean logic:** Straightforward and easy to understand

### Complexity Analysis - Two-Pointer

**Time Complexity: O(n + m)**
- Loop runs min(n, m) times: O(min(n,m))
- String concatenation in each iteration: O(1) amortized
- Appending remaining: O(n - min(n,m)) or O(m - min(n,m))
- Total: **O(n + m)** where n = len(word1), m = len(word2)

**Space Complexity: O(n + m)**
- Result string stores all characters: O(n + m)

### Code Implementation
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        p, q = 0, 0
        
        while p < len(word1) and q < len(word2):
            res += word1[p]
            res += word2[q]
            p += 1
            q += 1
        
        if len(word1) > len(word2):
            res += word1[p:]
        elif len(word2) > len(word1):
            res += word2[q:]
        
        return res
```

---

## Approach 2: Pythonic List Building

### Step-by-Step Working

1. **Convert to list for efficiency:**
   - Lists are mutable and more efficient for building strings than concatenation

2. **Use two pointers with list append:**
   - While both pointers are valid:
     - Append word1[p] and word2[q] to result list
     - Increment both pointers

3. **Append remaining using extend:**
   - `result.extend(word1[p:])`
   - `result.extend(word2[q:])`
   - The non-empty slice will be extended

4. **Join and return**

### Complexity Analysis - List Building

**Time Complexity: O(n + m)**
- Same as before, but list append is O(1)
- join() at end: O(n + m)

**Space Complexity: O(n + m)**
- Result list stores all characters

### Code Implementation
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        p, q = 0, 0
        
        while p < len(word1) and q < len(word2):
            result.append(word1[p])
            result.append(word2[q])
            p += 1
            q += 1
        
        result.extend(word1[p:])
        result.extend(word2[q:])
        
        return ''.join(result)
```

---

## Approach 3: Using itertools.zip_longest

### Step-by-Step Working

1. **Use zip_longest from itertools:**
   - Pairs characters from both strings until both are exhausted
   - Fills missing values with fillvalue (empty string)

2. **Flatten the pairs:**
   - zip_longest gives tuples like (char1, char2)
   - Flatten them into a single sequence

3. **Join and return**

### Complexity Analysis - zip_longest

**Time Complexity: O(n + m)**
- zip_longest: O(max(n, m))
- Joining: O(n + m)

**Space Complexity: O(n + m)**
- Result storage

### Code Implementation
```python
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=''))
```

**Explanation of this elegant one-liner:**
- `zip_longest(word1, word2, fillvalue='')` pairs characters, filling with empty string
- `for c1, c2 in ...` iterates through pairs
- `c1 + c2` concatenates pair (empty string won't show up)
- `''.join(...)` concatenates all pairs
- Result is exactly as expected!

---

## Approach 4: Index-Based with min/max

### Step-by-Step Working

1. **Find minimum length:**
   - `min_len = min(len(word1), len(word2))`

2. **Build merged part:**
   - Loop from 0 to min_len
   - At each index i, add word1[i] and word2[i]

3. **Append remainder:**
   - Add word1[min_len:] if word1 is longer
   - Add word2[min_len:] if word2 is longer

4. **Join and return**

### Code Implementation
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        result.append(word1[min_len:])
        result.append(word2[min_len:])
        
        return ''.join(result)
```

---

## Comparison of All Approaches

| Aspect | Two-Pointer | List Building | zip_longest | Index-Based |
|--------|-------------|----------------|------------|-----------|
| **Time** | O(n+m) | O(n+m) | O(n+m) | O(n+m) |
| **Space** | O(n+m) | O(n+m) | O(n+m) | O(n+m) |
| **Code Length** | 12 lines | 11 lines | 1 line | 9 lines |
| **Readability** | ✓ Very clear | ✓ Clear | Less obvious | ✓ Clear |
| **Pythonic** | Good | ✓ Better | Most | Good |
| **Performance** | Good | ✓ Best (no concatenation) | Good | ✓ Best |
| **Best for** | Learning | Production | Brevity | Balance |

---

## Key Insights

1. **All approaches are O(n + m):**
   - Can't avoid processing all characters
   - Linear time is optimal

2. **String concatenation is inefficient:**
   - Using `+=` creates new string each time
   - List building is preferred in Python

3. **zip_longest is clever but less readable:**
   - One-liner is elegant but harder to explain
   - Good for code golf, not interviews

4. **Two-pointer clearly shows the algorithm:**
   - Best for explaining logic
   - Demonstrates understanding of two-pointer technique

---

## Edge Cases to Consider

1. **Equal length strings:**
   ```
   word1 = "abc", word2 = "pqr"
   - Output: "apbqcr"
   - Both fully consumed
   ```

2. **First string is longer:**
   ```
   word1 = "abcd", word2 = "pq"
   - Output: "apbqcd"
   - Remaining: "cd"
   ```

3. **Second string is longer:**
   ```
   word1 = "ab", word2 = "pqrs"
   - Output: "apbqrs"
   - Remaining: "rs"
   ```

4. **Single character each:**
   ```
   word1 = "a", word2 = "b"
   - Output: "ab"
   - Simple merge
   ```

5. **One single, one longer:**
   ```
   word1 = "a", word2 = "pqr"
   - Output: "apqr"
   - One char merged, then remainder
   ```

6. **Very different lengths:**
   ```
   word1 = "a", word2 = "pqrstuvwxyz"
   - Output: "apqrstuvwxyz"
   - One iteration, then entire word2 remainder
   ```

---

## Recommendation

**Use Approach 2 (List Building)** for:
- **Production code:** Most efficient string building
- **Clean and readable:** Easy to understand logic
- **No imports needed:** Pure Python
- **Best performance:** Avoids string concatenation overhead

**Use Approach 1 (Two-Pointer)** for:
- **Interviews:** Shows strong understanding of two-pointer technique
- **Teaching:** Most explicit about the algorithm

**Use Approach 3 (zip_longest)** for:
- **Code brevity:** When conciseness is valued
- **Functional programming style:** If you prefer functional approaches

---

## Visual Representation

```
word1: a b c d
word2: p q r
       ↓ ↓ ↓
       a p b q c r d

Merge process:
1. Take word1[0], word2[0] → "ap"
2. Take word1[1], word2[1] → "apbq"
3. Take word1[2], word2[2] → "apbqcr"
4. Append word1[3] → "apbqcrd"
```

---

## Why Two-Pointer Works Here

1. **Independent advancement:** Each pointer moves independently
2. **Synchronous pairing:** We pair characters at same iteration
3. **Remainder handling:** Whichever runs out first, we append the other
4. **Clean separation:** Merge logic is separate from remainder logic

This is a straightforward two-pointer application without complex conditions or swaps.

