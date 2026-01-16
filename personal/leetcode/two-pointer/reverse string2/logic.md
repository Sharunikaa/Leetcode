# Reverse String II - LeetCode Problem

## Problem Statement
Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

**Rules:**
- If there are fewer than `k` characters left, reverse all of them
- If there are less than `2k` but greater than or equal to `k` characters, reverse the first `k` characters and leave the rest as original

**Example 1:**
- Input: `s = "abcdefg"`, `k = 2`
- Output: `"bacdfeg"`
- Explanation: 
  - First 2k=4 characters: "abcd" → reverse first k=2 → "bacd"
  - Remaining "efg" has less than k characters → reverse all → "gfe"
  - Result: "bacd" + "gfe" = "bacdfeg"

**Example 2:**
- Input: `s = "abcd"`, `k = 2`
- Output: `"bacd"`
- Explanation:
  - First 2k=4 characters: "abcd" → reverse first k=2 → "bacd"

**Constraints:**
- 1 ≤ s.length ≤ 10⁴
- s consists of only lowercase English letters
- 1 ≤ k ≤ 10⁴

---

## Approach 1: String Slicing (Two-Pointer Logic)

### Step-by-Step Working

1. **Initialize empty result:** `res = ""`

2. **Iterate through string with step of 2k:**
   - `for i in range(0, len(s), 2*k):`
   - This gives us starting positions: 0, 2k, 4k, ...

3. **For each 2k-character block:**
   - Extract first k characters: `s[i:i+k]`
   - Reverse them: `s[i:i+k][::-1]`
   - Add to result
   - Extract next k characters (without reversing): `s[i+k:i+2*k]`
   - Add to result

4. **Return accumulated result**

### Example Walkthrough
```
s = "abcdefg", k = 2

i=0 (first 2k=4 characters):
  - s[0:2] = "ab" → reversed = "ba"
  - s[2:4] = "cd" → keep as is = "cd"
  - res = "bacd"

i=4 (next 2k=4 characters, but only 3 left):
  - s[4:6] = "ef" → reversed = "fe"
  - s[6:8] = "g" → keep as is = "g"
  - res = "bacd" + "feg" = "bacdfeg"

Wait, the slicing handles this automatically!
- s[4:6] = "ef" (only gets available chars)
- s[6:8] = "g" (only gets available chars)
```

### Why It Works
- `s[i:i+k][::-1]` reverses the substring, and Python slicing handles out-of-bounds gracefully
- `s[i+k:i+2*k]` gets the remaining characters without reversing
- The loop naturally processes all blocks of 2k characters

### Complexity Analysis - String Slicing

**Time Complexity: O(n)**
- Iterate through string once: O(n)
- String concatenation and slicing: O(n) in total
- Total: **O(n)** where n = length of string

**Space Complexity: O(n)**
- Result string stores all characters: O(n)

### Code Implementation
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        for i in range(0, len(s), 2*k):
            res += s[i:i+k][::-1]      # Reverse first k chars
            res += s[i+k:i+2*k]        # Keep next k chars as is
        return res
```

---

## Approach 2: Convert to List (In-Place Modification)

### Step-by-Step Working

1. **Convert string to list:** `chars = list(s)`
   - Lists are mutable, easier to modify in-place

2. **Iterate through 2k-character blocks:**
   - `for i in range(0, len(chars), 2*k):`

3. **For each block:**
   - Calculate end of first k characters: `end = min(i+k, len(chars))`
   - Reverse using two pointers: `chars[i:end] = chars[i:end][::-1]`

4. **Convert back to string and return**

### Example Walkthrough
```
s = "abcdefg", k = 2
chars = ['a','b','c','d','e','f','g']

i=0:
  - end = min(0+2, 7) = 2
  - Reverse chars[0:2] → ['b','a','c','d','e','f','g']

i=4:
  - end = min(4+2, 7) = 6
  - Reverse chars[4:6] → ['b','a','c','d','f','e','g']
  - chars[6:8] unchanged (only has 'g')

Result: "bacdfeg"
```

### Complexity Analysis - List Approach

**Time Complexity: O(n)**
- Convert to list: O(n)
- Iterate and reverse: O(n)
- Convert back to string: O(n)
- Total: **O(n)**

**Space Complexity: O(n)**
- List storage: O(n)

### Code Implementation
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2*k):
            end = min(i + k, len(chars))
            chars[i:end] = chars[i:end][::-1]
        return ''.join(chars)
```

---

## Approach 3: Manual Two-Pointer Reversal

### Step-by-Step Working

1. **Convert string to list:** `chars = list(s)`

2. **Iterate through 2k-character blocks:**
   - `for i in range(0, len(chars), 2*k):`

3. **For each block, manually reverse using two pointers:**
   - `left = i`
   - `right = min(i+k-1, len(chars)-1)` (ensures we don't go out of bounds)
   - While `left < right`:
     - Swap `chars[left]` and `chars[right]`
     - Move pointers inward

4. **Convert back to string and return**

### Example Walkthrough
```
s = "abcd", k = 2
chars = ['a','b','c','d']

i=0:
  - left = 0, right = min(0+2-1, 3) = min(1, 3) = 1
  - Swap chars[0] and chars[1]: ['b','a','c','d']

i=4:
  - i >= len(chars), loop ends

Result: "bacd"
```

### Complexity Analysis - Manual Two-Pointer

**Time Complexity: O(n)**
- Iterate through all positions: O(n)
- Each character involved in at most one swap: O(n)
- Total: **O(n)**

**Space Complexity: O(n)**
- List storage: O(n)

### Code Implementation
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2*k):
            left = i
            right = min(i + k - 1, len(chars) - 1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return ''.join(chars)
```

---

## Comparison of All Approaches

| Aspect | String Slicing | List Conversion | Manual Two-Pointer |
|--------|-----------------|-----------------|-------------------|
| **Time** | O(n) | O(n) | O(n) |
| **Space** | O(n) | O(n) | O(n) |
| **Code Length** | Very short | Short | Moderate |
| **Readability** | ✓ Best | ✓ Good | Moderate |
| **Pythonic** | ✓ Yes | ✓ Yes | Less |
| **Memory Efficient** | No | No | No |
| **Best for** | Quick solution | Production | Learning |

---

## Key Insights

1. **String Slicing is most Pythonic:**
   - Most concise and readable
   - Python handles boundary conditions automatically
   - Best for interviews and production code

2. **All approaches are O(n) time:**
   - Can't do better than reading all characters
   - The iteration pattern (step of 2k) is key

3. **Space complexity is unavoidable:**
   - Strings are immutable in Python
   - Must create new string or convert to list
   - O(n) space is optimal for this problem

4. **Two-pointer logic is fundamental:**
   - Understanding manual pointer manipulation is important
   - But Python's slicing makes it unnecessary here

---

## Edge Cases to Consider

1. **String shorter than k:**
   ```
   s = "ab", k = 3
   - First block: s[0:3] reversed = "ba"
   - No second block
   - Output: "ba"
   ```

2. **String length equals k:**
   ```
   s = "abc", k = 3
   - First block: s[0:3] reversed = "cba"
   - Next block: s[3:6] = "" (empty)
   - Output: "cba"
   ```

3. **String length equals 2k:**
   ```
   s = "abcd", k = 2
   - First block: s[0:2] reversed = "ba"
   - Second block: s[2:4] = "cd"
   - Output: "bacd"
   ```

4. **Multiple complete 2k blocks:**
   ```
   s = "abcdefgh", k = 2
   - Blocks: "abcd" → "bacd", "efgh" → "fehg"
   - Output: "bacdfehg"
   ```

---

## Recommendation

**Use Approach 1 (String Slicing)** for:
- Clean, readable, Pythonic code
- Interview settings
- Production environments
- Quick problem solving

The string slicing approach perfectly balances simplicity with efficiency.
