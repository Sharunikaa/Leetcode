# Group Anagrams - LeetCode Problem

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **anagram** is a word formed by rearranging the letters of another word, using all the original letters exactly once.

**Example:**
- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
- Explanation: "eat", "tea", "ate" are anagrams (same characters rearranged)

**Example:**
- Input: `strs = [""]`
- Output: `[[""]]`

**Example:**
- Input: `strs = ["a"]`
- Output: `[["a"]]`

---

## Approach: Sorted String as Key (defaultdict)

### Key Insight
**Anagrams become identical when sorted!**

For example:
- "eat" → sorted: "aet"
- "tea" → sorted: "aet"
- "ate" → sorted: "aet"

All three map to the same key, so we can group them together using a hash map.

### Step-by-Step Working

1. **Create a defaultdict:** `d = defaultdict(list)`
   - Keys: sorted versions of strings
   - Values: lists of original strings that are anagrams

2. **Iterate through each string** in the input array:
   - Sort the current string: `a = ''.join(sorted(i))`
   - Use sorted string as key in dictionary
   - Append original string to the list at that key: `d[a].append(i)`

3. **Return all groups:** `return list(d.values())`
   - Extract all the grouped lists from the dictionary

### Example Walkthrough

```
strs = ["eat","tea","tan","ate","nat","bat"]

Step 1: Create defaultdict
  d = defaultdict(list)

Step 2: Process each string

String "eat":
  - sorted("eat") = "aet"
  - d["aet"] = ["eat"]

String "tea":
  - sorted("tea") = "aet"
  - d["aet"] = ["eat", "tea"]

String "tan":
  - sorted("tan") = "ant"
  - d["ant"] = ["tan"]

String "ate":
  - sorted("ate") = "aet"
  - d["aet"] = ["eat", "tea", "ate"]

String "nat":
  - sorted("nat") = "ant"
  - d["ant"] = ["tan", "nat"]

String "bat":
  - sorted("bat") = "abt"
  - d["abt"] = ["bat"]

Final Dictionary:
  {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
  }

Step 3: Return values
  d.values() = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### Visual Representation

```
Input: ["eat","tea","tan","ate","nat","bat"]

Group 1 (key="aet"):  eat → tea → ate
Group 2 (key="ant"):  tan → nat
Group 3 (key="abt"):  bat

Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

---

## Why This Works

1. **Anagrams have identical sorted forms:**
   - Different arrangements of same letters
   - When sorted, all become the same string

2. **Dictionary groups by sorted key:**
   - All anagrams map to the same key
   - Automatically grouped in the dictionary's list values

3. **defaultdict advantage:**
   - `defaultdict(list)` automatically creates empty lists for new keys
   - No need for `.get()` or `.setdefault()`
   - Cleaner code

---

## Complexity Analysis

### Time Complexity: **O(n × k log k)**
Where:
- `n` = number of strings in input
- `k` = maximum length of a string

Breakdown:
- Iterating through all strings: O(n)
- Sorting each string: O(k log k)
- Adding to dictionary: O(1) average case
- Total: **O(n × k log k)**

### Space Complexity: **O(n × k)**
Where:
- `n` = number of strings
- `k` = maximum length of a string

Breakdown:
- Dictionary stores all strings: O(n × k)
- Sorted keys: O(n × k) worst case
- Total: **O(n × k)**

---

## Approach 2: Character Frequency Counting (ASCII Array)

### Key Insight
**Anagrams have identical character frequencies!**

Instead of sorting, we count how many times each letter appears (a-z = 26 letters). Two words are anagrams if they have the same character frequency array.

For example:
- "eat" → frequencies: a:1, e:1, t:1
- "tea" → frequencies: a:1, e:1, t:1
- "ate" → frequencies: a:1, e:1, t:1

All three have identical frequency patterns.

### Step-by-Step Working

1. **Create a defaultdict:** `ans = defaultdict(list)`
   - Keys: tuples representing character frequencies
   - Values: lists of original strings that are anagrams

2. **For each string in the array:**
   - Create frequency array: `count = [0] * 26` (for a-z)
   - For each character in the string:
     - Calculate its position: `ord(c) - ord('a')` (a→0, b→1, ..., z→25)
     - Increment the frequency at that position: `count[ord(c) - ord('a')] += 1`
   
3. **Use frequency tuple as key:**
   - Convert count array to tuple: `tuple(count)`
   - Append the original string to the list at that key: `ans[tuple(count)].append(s)`

4. **Return all groups:** `return list(ans.values())`

### Example Walkthrough

```
strs = ["eat","tea","tan","ate","nat","bat"]

Step 1: Create defaultdict
  ans = defaultdict(list)

Step 2: Process "eat"
  - count = [0]*26
  - 'e': count[4] = 1
  - 'a': count[0] = 1
  - 't': count[19] = 1
  - count = [1,0,0,0,1,0,...,1,0,...] (a=1, e=1, t=1)
  - tuple(count) = (1,0,0,0,1,0,...,1,0,...)
  - ans[tuple] = ["eat"]

Step 3: Process "tea"
  - count = [1,0,0,0,1,0,...,1,0,...]  (same as "eat"!)
  - ans[tuple] = ["eat", "tea"]

Step 4: Process "tan"
  - count = [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,...,1,0,...]
  - (a=1, n=1, t=1)
  - Different tuple! 
  - ans[new_tuple] = ["tan"]

Step 5: Process "ate"
  - Same frequency as "eat" and "tea"
  - ans[eat_tuple] = ["eat", "tea", "ate"]

Step 6: Process "nat"
  - Same frequency as "tan"
  - ans[tan_tuple] = ["tan", "nat"]

Step 7: Process "bat"
  - count = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,...] (a=1, b=1, t=1)
  - Different tuple!
  - ans[bat_tuple] = ["bat"]

Final Dictionary:
  {
    (1,0,0,0,1,...,1): ["eat", "tea", "ate"],
    (1,0,0,0,0,...,1,1): ["tan", "nat"],
    (1,1,0,...,1): ["bat"]
  }

Step 8: Return values
  list(ans.values()) = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### Visual Representation

```
Frequency Pattern as Key:

"eat" → [1,0,0,0,1,...,0,0,1,...,0] ─┐
"tea" → [1,0,0,0,1,...,0,0,1,...,0] ─┼─► ["eat", "tea", "ate"]
"ate" → [1,0,0,0,1,...,0,0,1,...,0] ─┘

"tan" → [1,0,0,0,0,...,0,1,1,...,0] ─┐
"nat" → [1,0,0,0,0,...,0,1,1,...,0] ─┼─► ["tan", "nat"]

"bat" → [1,1,0,...,0,0,1,...,0] ────────► ["bat"]
```

### Complexity Analysis - ASCII Array

**Time Complexity: O(n × k)**
Where:
- `n` = number of strings
- `k` = maximum length of a string

Breakdown:
- Iterating through all strings: O(n)
- For each string, counting characters: O(k)
- Converting to tuple: O(26) = O(1)
- Adding to dictionary: O(1) average case
- Total: **O(n × k)** (linear, no sorting overhead!)

**Space Complexity: O(n × k)**
Where:
- Dictionary stores all strings: O(n × k)
- Each frequency tuple: O(26) = O(1)
- Total: **O(n × k)**

---

## Comparison of Both Approaches

| Aspect | Sorted (defaultdict) | Frequency (ASCII) |
|--------|----------------------|-------------------|
| **Time** | O(n × k log k) | O(n × k) |
| **Space** | O(n × k) | O(n × k) |
| **Sorting needed?** | ✓ Yes | ✗ No |
| **Easy to understand?** | ✓ Yes | Moderate |
| **Performance** | Slower | ✓ Faster |
| **Best for** | Quick coding | Optimal solution |

**Recommendation:** Use **Frequency Counting (ASCII)** for interviews—it's faster and shows deeper understanding of anagram properties.

---

## Key Insights

1. **Sorting anagrams is a classic pattern:**
   - Whenever you need to group anagrams, sorted string is the key
   - Works across many anagram problems

2. **defaultdict saves code:**
   - No need for existence checks
   - Automatically handles new keys with default values

3. **Edge cases handled:**
   - Empty array → returns `[]`
   - Single character → returns itself grouped
   - Empty strings → all empty strings grouped together

4. **Order doesn't matter:**
   - Problem allows any order in output
   - Don't need to sort the final result

---

## Code Optimization Tip

Remove the `print(d)` statement in production code:
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            a = ''.join(sorted(i))
            d[a].append(i)
        return list(d.values())
```

This improves performance by avoiding unnecessary print operations.
