# 345. Reverse Vowels of a String - LeetCode Problem

## Problem Statement
Given a string `s`, reverse only all the vowels in the string and return it.

**Vowels:** 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase)
- Vowels can appear multiple times
- Non-vowel characters remain in their original positions

**Example 1:**
- Input: `s = "IceCreAm"`
- Output: `"AceCreIm"`
- Explanation: Vowels are ['I', 'e', 'e', 'A']. Reversing them gives ['A', 'e', 'e', 'I']. Result: "AceCreIm"

**Example 2:**
- Input: `s = "leetcode"`
- Output: `"leotcede"`
- Explanation: Vowels are ['e', 'e', 'o', 'e']. Reversing them gives ['e', 'o', 'e', 'e']. Result: "leotcede"

**Constraints:**
- 1 ≤ s.length ≤ 3 × 10⁵
- s consists of printable ASCII characters

---

## Approach 1: Two-Pointer Technique

### Step-by-Step Working

1. **Convert string to list:** `chars = list(s)`
   - Strings are immutable; we need a mutable structure to swap

2. **Create vowel set:** `vowels = set("aeiouAEIOU")`
   - O(1) lookup time for checking vowels

3. **Initialize two pointers:**
   - `left = 0` (start)
   - `right = len(s) - 1` (end)

4. **Iterate while left < right:**
   - **Move left pointer:** If `chars[left]` is not a vowel, increment `left`
   - **Move right pointer:** If `chars[right]` is not a vowel, decrement `right`
   - **Swap:** If both point to vowels, swap them and move both pointers inward

5. **Convert back to string and return**

### Example Walkthrough
```
s = "IceCreAm"
chars = ['I','c','e','C','r','e','A','m']
vowels = {'a','e','i','o','u','A','E','I','O','U'}

Initial: left=0, right=7

Step 1: chars[0]='I' (vowel), chars[7]='m' (not vowel)
  - Move right: right=6

Step 2: chars[0]='I' (vowel), chars[6]='A' (vowel)
  - Swap: ['A','c','e','C','r','e','I','m']
  - left=1, right=5

Step 3: chars[1]='c' (not vowel)
  - Move left: left=2

Step 4: chars[2]='e' (vowel), chars[5]='e' (vowel)
  - Swap: ['A','c','e','C','r','e','I','m'] (no change, both 'e')
  - left=3, right=4

Step 5: left >= right, exit loop

Result: "AceCreIm" ✓
```

### Why It Works
- We only swap vowels with vowels
- Non-vowels stay in their positions
- Moving towards center ensures each vowel is visited at most once
- Two pointers work from opposite ends, naturally reversing

### Complexity Analysis - Two-Pointer

**Time Complexity: O(n)**
- Each character visited at most once by each pointer
- n = length of string

**Space Complexity: O(n)** or O(1) depending on definition
- O(n) for the list conversion (or output string)
- O(1) if not counting output space

### Code Implementation
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(chars) - 1
        
        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return ''.join(chars)
```

---

## Approach 2: Stack-Based Approach

### Step-by-Step Working

1. **Extract all vowels:** 
   - Iterate through string and collect all vowels in a stack
   - `vowel_stack = [char for char in s if char in vowels]`

2. **Reverse the stack:**
   - `vowel_stack.reverse()` or use reversed iterator

3. **Reconstruct string:**
   - Iterate through original string
   - If character is vowel, pop from reversed vowel list
   - If character is non-vowel, keep it as is

4. **Join and return result**

### Example Walkthrough
```
s = "IceCreAm"
vowels = {'a','e','i','o','u','A','E','I','O','U'}

Step 1: Extract vowels
  - vowel_stack = ['I', 'e', 'e', 'A']

Step 2: Reverse stack
  - vowel_stack = ['A', 'e', 'e', 'I']
  - reversed_iter = iterator pointing to ['A', 'e', 'e', 'I']

Step 3: Reconstruct
  - 'I' is vowel → use 'A' from reversed (pop)
  - 'c' is not vowel → keep 'c'
  - 'e' is vowel → use 'e' from reversed (pop)
  - 'C' is not vowel → keep 'C'
  - 'r' is not vowel → keep 'r'
  - 'e' is vowel → use 'e' from reversed (pop)
  - 'A' is vowel → use 'I' from reversed (pop)
  - 'm' is not vowel → keep 'm'
  - Result: "AceCreIm" ✓
```

### Complexity Analysis - Stack Approach

**Time Complexity: O(n)**
- First pass to collect vowels: O(n)
- Reverse: O(v) where v = number of vowels ≤ n
- Second pass to reconstruct: O(n)
- Total: O(n)

**Space Complexity: O(v)**
- Storing vowels in stack/list
- v = number of vowels ≤ n

### Code Implementation
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_list = [char for char in s if char in vowels]
        vowel_list.reverse()
        
        result = []
        vowel_iter = iter(vowel_list)
        
        for char in s:
            if char in vowels:
                result.append(next(vowel_iter))
            else:
                result.append(char)
        
        return ''.join(result)
```

---

## Approach 3: Multiple Passes (Simple but Less Efficient)

### Step-by-Step Working

1. **First pass - find positions and values of vowels**

2. **Second pass - replace vowels with reversed order**

3. **This approach is less efficient but conceptually simple**

### Example Implementation
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        
        # Find all vowel positions
        vowel_positions = [i for i, char in enumerate(chars) if char in vowels]
        
        # Get reversed vowels
        reversed_vowels = [chars[i] for i in reversed(vowel_positions)]
        
        # Place reversed vowels back
        for i, pos in enumerate(vowel_positions):
            chars[pos] = reversed_vowels[i]
        
        return ''.join(chars)
```

### Complexity Analysis - Multiple Passes

**Time Complexity: O(n)**
- Multiple passes through string, but still linear

**Space Complexity: O(v)**
- Storing vowel positions and values
- v = number of vowels

---

## Comparison of All Approaches

| Aspect | Two-Pointer | Stack-Based | Multiple Passes |
|--------|-------------|-------------|-----------------|
| **Time** | O(n) | O(n) | O(n) |
| **Space** | O(n)* | O(v) | O(v) |
| **Code Length** | Short | Moderate | Moderate |
| **Readability** | ✓ Good | ✓ Good | Moderate |
| **In-place** | Yes** | No | No |
| **Single Pass** | ✓ Yes | No (2 passes) | No (3 passes) |
| **Best for** | Production | Balanced approach | Learning |

*: O(n) for list conversion; or O(1) excluding output  
**: Two-pointer pointers, not entire string

---

## Key Insights

1. **Two-Pointer is optimal:**
   - Single pass through string
   - Space-efficient (only pointers)
   - Very clean and intuitive
   - Handles case-sensitivity elegantly with set

2. **Vowel set vs string checking:**
   - Using `set()` gives O(1) lookup
   - Using `in "aeiouAEIOU"` gives O(6) = O(1) practically
   - Both are fast enough; set is theoretically better

3. **Why not just sort vowels?**
   - Can't sort vowels in-place while keeping non-vowels positioned
   - Two-pointer is the natural solution for "reverse only certain elements"

4. **Edge cases handled naturally:**
   - No vowels in string → no swaps, returns original
   - All vowels → all get reversed
   - Single character → no swaps needed
   - Mixed case vowels → handled by case-insensitive set

---

## Edge Cases to Consider

1. **No vowels in string:**
   ```
   s = "bcdfg"
   - No vowels found
   - Output: "bcdfg" (unchanged)
   ```

2. **All vowels:**
   ```
   s = "aeiou"
   - All characters are vowels
   - Output: "uoiea" (completely reversed)
   ```

3. **Single character vowel:**
   ```
   s = "a"
   - Only one vowel
   - Output: "a" (no change, can't reverse single element)
   ```

4. **Mixed case vowels:**
   ```
   s = "AEIOUaeiou"
   - Output: "uoieaUOIEA"
   - Uppercase and lowercase handled together
   ```

5. **Special characters:**
   ```
   s = "a@e#i"
   - Vowels: ['a', 'e', 'i']
   - Reversed: ['i', 'e', 'a']
   - Output: "i@e#a"
   - Special chars unchanged
   ```

---

## Recommendation

**Use Approach 1 (Two-Pointer)** for:
- Production code and interviews
- Best time and space efficiency
- Most elegant and intuitive solution
- Single-pass algorithm

The two-pointer technique is the standard solution for this problem and demonstrates solid algorithmic thinking.

---

## Why Two-Pointer Works Here

The key insight is recognizing that we need to:
1. **Reverse only certain elements** (vowels)
2. **Keep others in place** (consonants)
3. **Work with limited passes**

Two-pointer naturally solves this by:
- Working from opposite ends simultaneously
- Only touching elements when both sides have vowels
- Achieving true reversal without collecting elements separately
