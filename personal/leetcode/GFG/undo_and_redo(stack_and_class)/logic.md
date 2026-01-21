# Undo and Redo using Stack

## Problem
Implement undo and redo functionality for a document editor using stacks.

## Solution Approach: Two Stack Pattern

### Data Structure
- **doc**: Main stack storing current document state
- **tmp**: Temporary stack storing undone operations (for redo)

### Operations

1. **append(x)**
   - Add character/string x to the document
   - Push to `doc` stack
   - Clear `tmp` stack (invalidates any redo history when new change is made)

2. **undo()**
   - Remove last operation from `doc` stack
   - Push the removed element to `tmp` stack
   - This allows redo to restore it

3. **redo()**
   - Pop from `tmp` stack (if available)
   - Push back to `doc` stack
   - Only works after undo operations

4. **read()**
   - Return the current document as a string
   - Join all elements in `doc` stack

## Example
```
append('a') -> doc = ['a'], tmp = []
append('b') -> doc = ['a','b'], tmp = []
undo()      -> doc = ['a'], tmp = ['b']
redo()      -> doc = ['a','b'], tmp = []
undo()      -> doc = ['a'], tmp = ['b']
append('c') -> doc = ['a','c'], tmp = [] (redo history cleared)
read()      -> "ac"
```

## Complexity
- **Time**: O(1) for each operation
- **Space**: O(n) where n is total operations
