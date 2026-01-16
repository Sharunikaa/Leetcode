# 680. Valid Palindrome II - LeetCode Problem

## Problem Statement
Given a string `s`, return `True` if the string can be a valid palindrome after deleting **at most one character**. Otherwise, return `False`.

A **palindrome** is a word that reads the same backward as forward.

**Example 1:**
- Input: `s = "aba"`
- Output: `True`
- Explanation: Already a palindrome, no deletion needed

**Example 2:**
- Input: `s = "abca"`
- Output: `True`
- Explanation: Delete 'c' to get "aba" which is a palindrome

**Example 3:**
- Input: `s = "abc"`
- Output: `False`
- Explanation: Can't form a palindrome by deleting one character

**Constraints:**
- 1 ≤ s.length ≤ 10⁵
- s consists of lowercase English letters

---

## Approach 1: Two-Pointer with Greedy Deletion

### Step-by-Step Working

1. **Initialize two pointers:**
   - `left = 0` (start)
   - `right = len(s) - 1` (end)

2. **Compare characters from both ends:**
   - While `left < right`:
     - If `s[left] == s[right]`: move both pointers inward
     - If `s[left] != s[right]`: **we found a mismatch!**
       - Try deleting left character: check if `s[left+1...right]` is palindrome
       - Try deleting right character: check if `s[left...right-1]` is palindrome
       - Return True if either is a palindrome

3. **Helper function to check palindrome:**
   - Create `isPalindrome(l, r)` function
   - Check if substring `s[l...r]` is a palindrome using two pointers

4. **If we exit the while loop, string is already palindrome:** return True

### Example Walkthrough
```
s = "abca"

Step 1: left=0, right=3
  - s[0]='a', s[3]='a' → Match! left=1, right=2

Step 2: left=1, right=2
  - s[1]='b', s[2]='c' → Mismatch!
  - Try deleting left: isPalindrome(2, 2) → True ✓
  - Return True

Actually, deleting right would be: isPalindrome(1, 1) → True
Both work, return True
```

```
s = "abc"

Step 1: left=0, right=2
  - s[0]='a', s[2]='c' → Mismatch!
  - Try deleting left: isPalindrome(1, 2) → "bc" → False
  - Try deleting right: isPalindrome(0, 1) → "ab" → False
  - Return False
```

### Why It Works

1. **Greedy approach:** When we find a mismatch, we try both deletions
   - Delete the left character: give right pointer a chance
   - Delete the right character: give left pointer a chance

2. **At most one deletion:** The algorithm only tries deletion when first mismatch occurs
   - If we can't form palindrome with one deletion, it's impossible

3. **Early termination:** If we reach the end without mismatches, it's already palindrome

### Complexity Analysis - Two-Pointer with Greedy

**Time Complexity: O(n)**
- Main two-pointer loop: O(n)
- In worst case, `isPalindrome()` checks O(n) characters
- But we call it at most once (at first mismatch)
- Total: **O(n)** where n = length of string

**Space Complexity: O(1)**
- Only using pointers and variables
- No extra data structures

### Code Implementation - With Helper Function
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Try deleting left or right character
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        
        return True  # Already a palindrome
```

### Code Implementation - With String Slicing (Alternative)
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try deleting left or right character
                skip_left = s[left+1:right+1]
                skip_right = s[left:right]
                return (skip_left == skip_left[::-1]) or (skip_right == skip_right[::-1])
            left += 1
            right -= 1
        return True
```

**Comparison of the two implementations:**

| Aspect | Helper Function | String Slicing |
|--------|-----------------|-----------------|
| **Readability** | More explicit | Compact, Pythonic |
| **Lines of code** | 11 lines | 8 lines |
| **String creation** | No extra strings | Creates 2 substrings at mismatch |
| **Time Complexity** | O(n) | O(n) same |
| **Space Complexity** | O(1) pointers only | O(n) substring creation |
| **Clarity** | Very clear logic | More condensed |

**Note:** The string slicing version is more Pythonic and concise but creates temporary substrings. The helper function version is more memory-efficient and explicit about the logic. Both are O(n) time overall.

---

## Approach 2: Recursive Two-Pointer

### Step-by-Step Working

1. **Create recursive helper function:**
   - `isValidPalindrome(l, r, deletions_left)`
   - Parameters:
     - `l`: left pointer position
     - `r`: right pointer position
     - `deletions_left`: number of deletions we can still make (0 or 1)

2. **Base cases:**
   - If `l >= r`: we've successfully checked all characters → return True
   - If `deletions_left < 0`: used too many deletions → return False

3. **Recursive case:**
   - If `s[l] == s[r]`: move both pointers inward, no deletion used
   - If `s[l] != s[r]`:
     - Try deleting left: recurse with `(l+1, r, deletions_left-1)`
     - Try deleting right: recurse with `(l, r-1, deletions_left-1)`
     - Return True if either option works

4. **Call with initial parameters:** `isValidPalindrome(0, len(s)-1, 1)`

### Complexity Analysis - Recursive

**Time Complexity: O(n)**
- In worst case, we explore two branches but each branch processes O(n) characters total
- Not exponential because we only delete once

**Space Complexity: O(n)**
- Recursion call stack depth can be O(n) in worst case

### Code Implementation
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(l, r, deletions_left):
            if l >= r:
                return True
            
            if deletions_left < 0:
                return False
            
            if s[l] == s[r]:
                return isValidPalindrome(l + 1, r - 1, deletions_left)
            else:
                # Try deleting left or right character
                return isValidPalindrome(l + 1, r, deletions_left - 1) or \
                       isValidPalindrome(l, r - 1, deletions_left - 1)
        
        return isValidPalindrome(0, len(s) - 1, 1)
```

---

## Approach 3: Dynamic Programming (Overkill but Educational)

### Step-by-Step Working

1. **Create DP table:**
   - `dp[i][j][k]` = Can substring `s[i...j]` form palindrome with at most `k` deletions?

2. **Base cases:**
   - `dp[i][i][k]` = True (single character is palindrome)
   - `dp[i][j][0]` = check if `s[i...j]` is already palindrome

3. **Recurrence relation:**
   - If `s[i] == s[j]`: `dp[i][j][k] = dp[i+1][j-1][k]`
   - If `s[i] != s[j]`:
     - Try deleting left: `dp[i+1][j][k-1]`
     - Try deleting right: `dp[i][j-1][k-1]`
     - `dp[i][j][k] = dp[i+1][j][k-1] or dp[i][j-1][k-1]`

4. **Answer:** `dp[0][n-1][1]` where n = length of string

### Complexity Analysis - DP

**Time Complexity: O(n²)**
- DP table has O(n²) states
- Each state computation: O(1)
- Total: O(n²)

**Space Complexity: O(n²)**
- DP table storage

### Code Implementation
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        # dp[i][j][k] = can s[i:j+1] form palindrome with at most k deletions
        dp = [[[False] * 2 for _ in range(n)] for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i][0] = True
            dp[i][i][1] = True
        
        # Fill DP table for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # Characters match
                    if length == 2:
                        dp[i][j][0] = True
                        dp[i][j][1] = True
                    else:
                        dp[i][j][0] = dp[i+1][j-1][0]
                        dp[i][j][1] = dp[i+1][j-1][1]
                else:
                    # Characters don't match
                    # With 1 deletion allowed
                    dp[i][j][1] = (i+1 <= j and dp[i+1][j][1]) or \
                                   (i <= j-1 and dp[i][j-1][1])
                    # With 0 deletions (can't match)
                    dp[i][j][0] = False
        
        return dp[0][n-1][1]
```

---

## Comparison of All Approaches

| Aspect | Two-Pointer | Recursive | Dynamic Programming |
|--------|-------------|-----------|-------------------|
| **Time** | O(n) | O(n) | O(n²) |
| **Space** | O(1) | O(n) call stack | O(n²) DP table |
| **Code Length** | Very short | Moderate | Long |
| **Readability** | ✓ Excellent | Good | Complex |
| **Interview Ready** | ✓ Yes | Yes | Overkill |
| **Practical** | ✓ Best | Good | Educational |
| **Intuitive** | ✓ Yes | Yes | No |

---

## Key Insights

1. **Two-Pointer is optimal:**
   - O(n) time with O(1) space
   - Most elegant and interview-ready
   - Greedy approach works perfectly here

2. **Why greedy deletion works:**
   - When we find first mismatch, we only have two options
   - No need to explore more deletions
   - "At most one" constraint limits possibilities

3. **The trick is the helper function:**
   - Check valid palindrome without deletion (helper)
   - Main function tries both options at mismatch
   - Separation of concerns makes code clean

4. **DP is unnecessary:**
   - While correct, it's much slower (O(n²) vs O(n))
   - Overkill for "at most one" constraint
   - Good example of when NOT to use DP

---

## Edge Cases to Consider

1. **Already a palindrome:**
   ```
   s = "aba"
   - No mismatches found
   - Output: True
   ```

2. **Can be palindrome with one deletion:**
   ```
   s = "abca"
   - Mismatch at end, delete 'c' → "aba"
   - Output: True
   ```

3. **Cannot be palindrome even with deletion:**
   ```
   s = "abc"
   - Mismatch at position 0,2
   - Delete 'a': "bc" → not palindrome
   - Delete 'c': "ab" → not palindrome
   - Output: False
   ```

4. **Single character:**
   ```
   s = "a"
   - Already palindrome
   - Output: True
   ```

5. **Two characters same:**
   ```
   s = "aa"
   - Already palindrome
   - Output: True
   ```

6. **Two characters different:**
   ```
   s = "ab"
   - Delete either one, single char is palindrome
   - Output: True
   ```

7. **Multiple mismatches:**
   ```
   s = "abcd"
   - First mismatch at (0,3): 'a' vs 'd'
   - Try delete 'a': "bcd" → not palindrome
   - Try delete 'd': "abc" → not palindrome
   - Output: False
   ```

8. **Entire string different:**
   ```
   s = "abcdefg"
   - Too many mismatches
   - Output: False
   ```

---

## Recommendation

**Use Approach 1 (Two-Pointer with Greedy Deletion)** because:
- **Optimal time complexity:** O(n)
- **Minimal space:** O(1)
- **Clean and readable:** Easy to understand and explain
- **Interview favorite:** Demonstrates two-pointer mastery
- **Production ready:** Best real-world performance

---

## How to Think About This Problem

1. **Recognize the pattern:**
   - "Valid palindrome" → two-pointer approach
   - "At most one deletion" → try both options when mismatch occurs

2. **Leverage existing logic:**
   - You already know how to check if string is palindrome
   - Extend that to handle one deletion gracefully

3. **The key insight:**
   - When mismatch occurs at (l, r), only two meaningful options:
     - Skip left character and check (l+1, r)
     - Skip right character and check (l, r-1)
   - One of these must work if a valid palindrome exists

4. **Why this greedy approach works:**
   - We're forced to handle mismatch immediately
   - Can't skip past it with valid palindrome
   - Must delete one of the mismatched characters

---

## Common Mistakes to Avoid

1. **Forgetting boundary check in isPalindrome:**
   ```python
   # Wrong: Might access s[left+1] when left+1 > right
   isPalindrome(left+1, right)
   
   # Right: isPalindrome naturally handles l >= r
   while l < r:
       ...
   ```

2. **Trying to delete both characters:**
   - Problem allows "at most one" deletion
   - We try each deletion separately, not both

3. **Not handling single character:**
   - Single character is always palindrome
   - Base case returns True naturally

4. **Checking entire string again:**
   - Only check the substring after one character removed
   - Not the entire string

